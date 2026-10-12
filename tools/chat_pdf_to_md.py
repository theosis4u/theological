#!/usr/bin/env python3
"""Import an AI chat that was printed to PDF into a Markdown file with front matter.

Pipeline: PDF -> visual lines -> user/assistant turns -> cleaned Markdown -> front matter.

Turn detection is layout-based. Many chat sites render the user's messages as
right-aligned "bubbles" (a filled rectangle) and the assistant's replies as plain
full-width text. This script treats a line as a user line when it sits inside a
light-filled rectangle that starts right of --bubble-min-x and reaches the right
margin (--bubble-right). Everything else is the assistant. Tune the thresholds for
your site's print layout (run with --debug to see rectangles and line positions).

Read-only on the source: it only reads the PDF.

Requires: pip install pymupdf

Usage:
  chat_pdf_to_md.py chat.pdf -o out.md --title "Chat title" \
      --source https://example.com/chat/<id> --date 2026-01-31 \
      --project "My project" --topic soteriology [--assistant-label Assistant]
"""
import argparse, json, re, sys

CHROME = re.compile(r'^(Worked for\b.*|Thought for\b.*|\d+ sources?|View Preview|Edit|Copy|Save|Share|'
                    r'Regenerate|Retry|Like|Dislike|More actions|Create share link|Page \d+( of \d+)?|\d{1,3})$')
LIST_RE = re.compile(r'^([*•●▪◦\-–—]|\d+[.)])\s+\S')


def reflow(text):
    """Join wrapped lines into paragraphs; keep list items on their own lines."""
    blocks = []
    for block in re.split(r'\n[ \t]*\n', text):
        ls = [l.strip() for l in block.split('\n') if l.strip() and not CHROME.match(l.strip())]
        if not ls:
            continue
        if any(LIST_RE.match(x) for x in ls):
            merged = []
            for l in ls:
                if LIST_RE.match(l) or not merged:
                    merged.append(re.sub(r'^[•●▪◦–—]\s*', '- ', l))
                else:
                    merged[-1] += ' ' + l
            blocks.append('\n'.join(merged))
        else:
            para = ''
            for l in ls:
                if para.endswith('-') and not para.endswith(' -'):
                    para = para[:-1] + l
                else:
                    para = (para + ' ' + l).strip()
            blocks.append(para)
    return '\n\n'.join(blocks).strip()


def bubbles(page, min_x, right):
    out = []
    for g in page.get_drawings():
        f = g.get('fill')
        if f is None or g.get('color') is not None or not all(v > 0.9 for v in f):
            continue
        r = g['rect']
        if r.x1 >= right and r.x0 >= min_x and r.width >= 60 and r.height >= 10:
            out.append(r)
    return out


def segment(pdf, min_x, right, line_min_x, debug=False):
    import pymupdf
    doc = pymupdf.open(pdf)
    msgs = []
    for page in doc:
        bs = bubbles(page, min_x, right)
        spans = [s for b in page.get_text('dict')['blocks'] if b.get('type') == 0
                 for l in b['lines'] for s in l['spans'] if s['text'].strip()]
        spans.sort(key=lambda s: (round(s['bbox'][1], 1), s['bbox'][0]))
        lines, cur = [], None
        for s in spans:
            x0, y0, x1, y1 = s['bbox']
            if cur and abs(cur['y0'] - y0) <= 4 and x0 >= cur['x1'] - 8:
                cur['x1'] = max(cur['x1'], x1); cur['y1'] = max(cur['y1'], y1); cur['text'] += s['text']
            else:
                if cur: lines.append(cur)
                cur = {'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'text': s['text']}
        if cur: lines.append(cur)
        if debug:
            print(f'page {page.number}: bubbles={[tuple(round(v) for v in r) for r in bs]}', file=sys.stderr)
        for ln in lines:
            t = ln['text'].replace('\xa0', ' ').rstrip()
            cy = (ln['y0'] + ln['y1']) / 2
            user = ln['x0'] >= line_min_x and any(
                r.x0 - 3 <= ln['x0'] <= r.x1 + 3 and r.y0 - 3 <= cy <= r.y1 + 3 for r in bs)
            if debug:
                print(f"  {'U' if user else 'A'} x0={ln['x0']:.0f} {t[:60]}", file=sys.stderr)
            role = 'user' if user else 'assistant'
            if msgs and msgs[-1]['r'] == role:
                msgs[-1]['t'] += '\n' + t
            else:
                msgs.append({'r': role, 't': t})
    out = []
    for m in msgs:
        t = reflow(m['t'])
        if not t:
            continue
        if out and out[-1]['r'] == m['r']:
            out[-1]['t'] += '\n\n' + t
        else:
            out.append({'r': m['r'], 't': t})
    return out


def front_matter(a):
    fm = ['---', f'title: {json.dumps(a.title or "Untitled chat", ensure_ascii=False)}']
    for k in ('source', 'date', 'project', 'topic'):
        v = getattr(a, k)
        if v:
            fm.append(f'{k}: {json.dumps(v, ensure_ascii=False) if k == "project" else v}')
    return '\n'.join(fm + ['---', ''])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('pdf'); ap.add_argument('-o', '--out')
    ap.add_argument('--title'); ap.add_argument('--source'); ap.add_argument('--date')
    ap.add_argument('--project'); ap.add_argument('--topic')
    ap.add_argument('--assistant-label', default='Assistant')
    ap.add_argument('--bubble-min-x', type=float, default=85)
    ap.add_argument('--bubble-right', type=float, default=545)
    ap.add_argument('--line-min-x', type=float, default=95)
    ap.add_argument('--debug', action='store_true')
    a = ap.parse_args()
    msgs = segment(a.pdf, a.bubble_min_x, a.bubble_right, a.line_min_x, a.debug)
    body = [f'# {a.title or "Untitled chat"}']
    for m in msgs:
        body.append(f"## {'User' if m['r'] == 'user' else a.assistant_label}\n\n{m['t']}")
    md = front_matter(a) + '\n\n'.join(body) + '\n'
    if a.out:
        open(a.out, 'w', encoding='utf-8').write(md)
        print(f'{a.out}: {len(msgs)} turns, {len(md)} bytes', file=sys.stderr)
    else:
        sys.stdout.write(md)


if __name__ == '__main__':
    main()

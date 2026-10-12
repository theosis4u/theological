#!/usr/bin/env python3
"""Convert a study Markdown file into Logos-ready simple HTML.

Blockquotes ('> ' lines) become <p class="ql-indent-1"> paragraphs by default (Logos strips <blockquote>),
or <blockquote> with --indent-style blockquote.
Markdown links stay <a href>. Pipe tables become bullet lists (Logos has no tables).

Output: first line <p><strong>{title}</strong></p> (no leading blanks),
<p><br></p> between paragraphs and before headings. Tags: h1-h3,p,strong,em,ul,ol,li.
Usage: md_to_logos_html.py study.md [--title "My Study Note"] > out.html
"""
import argparse, html, re, sys

BOOKS = (r'(?:[123] ?)?(?:Gen(?:esis)?|Exod(?:us)?|Lev(?:iticus)?|Num(?:bers)?|Deut(?:eronomy)?|Josh(?:ua)?|Judg(?:es)?|Ruth|Sam(?:uel)?|Kings|Chron(?:icles)?|Ezra|Neh(?:emiah)?|Esth(?:er)?|Job|Ps(?:alms?)?|Prov(?:erbs)?|Eccl(?:esiastes)?|Song(?: of (?:Songs|Solomon))?|Isa(?:iah)?|Jer(?:emiah)?|Lam(?:entations)?|Ezek(?:iel)?|Dan(?:iel)?|Hos(?:ea)?|Joel|Amos|Obad(?:iah)?|Jonah|Mic(?:ah)?|Nah(?:um)?|Hab(?:akkuk)?|Zeph(?:aniah)?|Hag(?:gai)?|Zech(?:ariah)?|Mal(?:achi)?|Matt(?:hew)?|Mark|Luke|John|Acts|Rom(?:ans)?|Cor(?:inthians)?|Gal(?:atians)?|Eph(?:esians)?|Phil(?:ippians)?|Col(?:ossians)?|Thess(?:alonians)?|Tim(?:othy)?|Titus|Philem(?:on)?|Heb(?:rews)?|Jas|James|Pet(?:er)?|Jude|Rev(?:elation)?)')
REF = re.compile(r'(?<![\w\[/])(' + BOOKS + r')\.? (\d+):(\d+)(?:[-\u2013](\d+))?(?![\w\]])')
BIBLIA = None

def biblia(t):
    # Link plain Bible references (not already inside link text) to Biblia.com.
    def f(m):
        book = m.group(1).replace(' ', '')
        tail = f"{m.group(2)}.{m.group(3)}" + (f"-{m.group(4)}" if m.group(4) else '')
        return f'[{m.group(0)}](https://biblia.com/bible/{BIBLIA}/{book}{tail})'
    parts = re.split(r'(\[[^\]]*\]\([^)]*\)|`[^`]*`)', t)
    return ''.join(p if i % 2 else REF.sub(f, p) for i, p in enumerate(parts))

def inline(t):
    if BIBLIA: t = biblia(t)
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*|__(.+?)__', lambda m: f'<strong>{m.group(1) or m.group(2)}</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)|(?<!\w)_(?!\s)(.+?)(?<!\s)_(?!\w)',
               lambda m: f'<em>{m.group(1) or m.group(2)}</em>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', t)
    return t

def parse_front(text):
    meta = {}
    if text.startswith('---\n'):
        end = text.find('\n---', 4)
        if end != -1:
            for line in text[4:end].splitlines():
                if ':' in line:
                    k, v = line.split(':', 1)
                    meta[k.strip()] = v.strip().strip('\'"')
            text = text[end + 4:].lstrip('\n')
    return meta, text

INDENT = 'ql-indent'

def table_to_list(md):
    out = []
    for l in md.splitlines():
        if l.startswith('|'):
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            if not c or c[0] in ('Verse',) or set(''.join(c)) <= set('-: '):
                continue
            l = f"- **{c[0]}**: " + '; '.join(c[1:])
        out.append(l)
    return '\n'.join(out)

def quote_html(lines):
    paras, cur = [], []
    for l in lines:
        s = re.sub(r'^>\s?', '', l)
        if s.strip():
            cur.append(s.strip())
        elif cur:
            paras.append(' '.join(cur)); cur = []
    if cur: paras.append(' '.join(cur))
    if INDENT == 'ql-indent':
        return '\n'.join(f'<p class="ql-indent-1">{inline(x)}</p>' for x in paras)
    return '<blockquote>' + '<br>'.join(inline(x) for x in paras) + '</blockquote>'

def split_quotes(blocks):
    res = []
    for b in blocks:
        run, isq = [], None
        for l in b.strip().splitlines():
            q = l.lstrip().startswith('>')
            if isq is not None and q != isq:
                res.append(('q' if isq else 't', run)); run = []
            run.append(l); isq = q
        if run: res.append(('q' if isq else 't', run))
    return res

def convert(md, title):
    blocks = re.split(r'\n\s*\n', table_to_list(md).strip())
    out = [f'<p><strong>{html.escape(title)}</strong></p>']
    SP = '<p><br></p>'
    for kind, blines in split_quotes(blocks):
        if kind == 'q':
            if out[-1] != SP and len(out) > 1:
                out.append(SP)
            out.append(quote_html(blines)); out.append(SP)
            continue
        b = '\n'.join(blines).strip()
        if not b or re.fullmatch(r'-{3,}|\*{3,}', b):
            continue
        lines = b.splitlines()
        m = re.match(r'(#{1,6})\s+(.*)', lines[0])
        if m and len(lines) == 1:
            lvl = min(len(m.group(1)), 3)
            if lvl == 1 and len(out) == 1 and m.group(2).strip() == title.strip():
                continue  # skip an H1 that repeats the note title
            if out[-1] != SP and len(out) > 1:
                out.append(SP)
            out.append(f'<h{lvl}>{inline(m.group(2))}</h{lvl}>')
            continue
        if all(re.match(r'\s*([-*+]|\d+[.)])\s+', l) or l.startswith('  ') for l in lines):
            tag = 'ol' if re.match(r'\s*\d+[.)]', lines[0]) else 'ul'
            items = []
            for l in lines:
                mm = re.match(r'\s*(?:[-*+]|\d+[.)])\s+(.*)', l)
                if mm: items.append(mm.group(1))
                elif items: items[-1] += ' ' + l.strip()
            out.append(f'<{tag}>' + ''.join(f'<li>{inline(i)}</li>' for i in items) + f'</{tag}>')
        else:
            out.append(f'<p>{inline(" ".join(l.strip() for l in lines))}</p>')
        out.append(SP)
    while out and out[-1] == SP:
        out.pop()
    return '\n'.join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('file'); ap.add_argument('--title')
    ap.add_argument('--indent-style', choices=['blockquote', 'ql-indent'], default='ql-indent')
    ap.add_argument('--biblia', metavar='VERSION', help='link plain Bible references to Biblia.com in this translation, e.g. kjv1900')
    a = ap.parse_args()
    global BIBLIA; BIBLIA = a.biblia
    global INDENT; INDENT = a.indent_style
    meta, body = parse_front(open(a.file, encoding='utf-8').read())
    title = a.title or meta.get('title') or 'Untitled'
    sys.stdout.write('<!DOCTYPE html>\n<html><head><meta charset="utf-8"><title>'
                     + html.escape(title) + '</title></head><body>'
                     + convert(body, title) + '</body></html>\n')

if __name__ == '__main__':
    main()

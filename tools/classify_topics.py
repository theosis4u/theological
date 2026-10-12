#!/usr/bin/env python3
"""Suggest a topic folder for each Markdown/text file from a keyword map. Outputs a CSV for human review.

It never moves or edits files. Review the CSV, correct the `topic` column, then move files yourself.

Keyword map (JSON, or YAML if PyYAML is installed):
  {"soteriology": ["justification", "grace", "faith alone", "theosis"],
   "christology": ["incarnation", "logos", "monogenes", "two natures"],
   "eschatology": ["revelation", "millennium", "parousia"]}
Matching is case-insensitive on whole words/phrases in the title (weight 3) and body (weight 1).

Usage:
  classify_topics.py SOURCE_DIR --map topics.json [-o suggestions.csv] [--min-score 2] [--ext .md,.txt]
  classify_topics.py --example-map > topics.json
"""
import argparse, csv, json, os, re, sys

EXAMPLE = {
    "scripture-and-canon": ["inerrancy", "inspiration", "canon", "septuagint", "translation"],
    "christology": ["incarnation", "trinity", "logos", "monogenes", "two natures"],
    "soteriology": ["justification", "grace", "salvation", "faith", "works", "election"],
    "atonement": ["atonement", "ransom", "substitution", "propitiation", "christus victor"],
    "ecclesiology-and-sacraments": ["baptism", "eucharist", "communion", "church", "sacrament"],
    "eschatology": ["revelation", "millennium", "parousia", "resurrection", "judgment"],
    "church-history": ["council", "reformation", "fathers", "creed", "schism"],
}


def load_map(path):
    text = open(path, encoding='utf-8').read()
    if path.lower().endswith(('.yml', '.yaml')):
        try:
            import yaml
        except ImportError:
            sys.exit('PyYAML not installed; use a JSON map or `pip install pyyaml`.')
        return yaml.safe_load(text)
    return json.loads(text)


def title_of(text, fn):
    m = re.search(r'(?m)^title:\s*"?(.+?)"?\s*$', text) or re.search(r'(?m)^# (.+)$', text)
    return m.group(1).strip() if m else fn


def score(text, title, kmap):
    res = {}
    for topic, words in kmap.items():
        s, hits = 0, []
        for w in words:
            pat = re.compile(r'(?<!\w)' + re.escape(w.lower()) + r'(?!\w)')
            t, b = len(pat.findall(title.lower())), len(pat.findall(text.lower()))
            if t or b:
                s += 3 * t + b; hits.append(f'{w}:{t + b}')
        if s:
            res[topic] = (s, hits)
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('src', nargs='?'); ap.add_argument('--map'); ap.add_argument('-o', '--out')
    ap.add_argument('--min-score', type=int, default=2); ap.add_argument('--ext', default='.md,.txt')
    ap.add_argument('--example-map', action='store_true')
    a = ap.parse_args()
    if a.example_map:
        print(json.dumps(EXAMPLE, indent=2)); return
    if not a.src or not a.map:
        ap.error('SOURCE_DIR and --map are required')
    kmap, exts = load_map(a.map), tuple(a.ext.split(','))
    rows = []
    for root, dirs, files in os.walk(a.src):
        dirs[:] = sorted(d for d in dirs if not d.startswith('.'))
        for fn in sorted(files):
            if not fn.lower().endswith(exts):
                continue
            p = os.path.join(root, fn)
            text = open(p, encoding='utf-8', errors='replace').read()
            title = title_of(text, fn)
            sc = sorted(score(text, title, kmap).items(), key=lambda kv: -kv[1][0])
            best = sc[0] if sc and sc[0][1][0] >= a.min_score else None
            rows.append({'file': os.path.relpath(p, a.src), 'title': title,
                         'topic': best[0] if best else 'unsorted', 'score': best[1][0] if best else 0,
                         'runner_up': f'{sc[1][0]} ({sc[1][1][0]})' if len(sc) > 1 else '',
                         'theology_likely': 'yes' if best else 'no',
                         'matched': '; '.join(best[1][1]) if best else ''})
    cols = ['file', 'title', 'topic', 'score', 'runner_up', 'theology_likely', 'matched']
    f = open(a.out, 'w', newline='', encoding='utf-8') if a.out else sys.stdout
    w = csv.DictWriter(f, cols); w.writeheader(); w.writerows(rows)
    if a.out:
        f.close(); print(f'{len(rows)} files -> {a.out}', file=sys.stderr)


if __name__ == '__main__':
    main()

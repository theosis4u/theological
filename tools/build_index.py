#!/usr/bin/env python3
"""Build INDEX.md for a study repo from the front matter of its Markdown files.

Groups files by `topic` (or by top-level folder when there is no topic), newest first.
Skips README.md, INDEX.md, PROFILE.md, METHOD.md, files starting with "_", and hidden folders.

Usage: build_index.py [repo_dir] [-o INDEX.md] [--title "Index"]
"""
import argparse, os, re, collections

SKIP = {'README.md', 'INDEX.md', 'PROFILE.md', 'METHOD.md', 'CONTRIBUTING.md', 'LICENSE.md'}


def front(path):
    meta = {}
    with open(path, encoding='utf-8') as f:
        t = f.read()
    if t.startswith('---\n'):
        end = t.find('\n---', 4)
        for line in t[4:end].splitlines() if end != -1 else []:
            if ':' in line:
                k, v = line.split(':', 1); meta[k.strip()] = v.strip().strip('"\'')
    if 'title' not in meta:
        m = re.search(r'(?m)^# (.+)', t)
        meta['title'] = m.group(1).strip() if m else os.path.basename(path)
    return meta


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('repo', nargs='?', default='.')
    ap.add_argument('-o', '--out'); ap.add_argument('--title', default='Index'); a = ap.parse_args()
    groups = collections.defaultdict(list)
    for root, dirs, files in os.walk(a.repo):
        dirs[:] = sorted(d for d in dirs if not d.startswith('.'))
        for fn in files:
            if not fn.endswith('.md') or fn in SKIP or fn.startswith('_'):
                continue
            p = os.path.join(root, fn); rel = os.path.relpath(p, a.repo).replace(os.sep, '/')
            m = front(p)
            topic = m.get('topic') or (rel.split('/')[0] if '/' in rel else 'misc')
            groups[topic].append((m.get('date', ''), m['title'], rel))
    out = [f'# {a.title}', '', f'{sum(map(len, groups.values()))} files.', '']
    for topic in sorted(groups):
        out += [f'## {topic}', '']
        for d, t, rel in sorted(groups[topic], reverse=True):
            out.append(f'- {d + " " if d else ""}[{t}]({rel})')
        out.append('')
    text = '\n'.join(out)
    if a.out:
        open(os.path.join(a.repo, a.out) if not os.path.isabs(a.out) else a.out, 'w', encoding='utf-8').write(text)
    else:
        print(text)


if __name__ == '__main__':
    main()

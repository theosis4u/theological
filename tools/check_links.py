#!/usr/bin/env python3
"""Check internal Markdown links and #anchors in the repo. Exit 1 on any broken link.
Usage: python3 tools/check_links.py [repo_root]"""
import glob, os, re, sys

root = sys.argv[1] if len(sys.argv) > 1 else "."
os.chdir(root)

def slug(h):
    h = re.sub(r"\{:[^}]*\}", "", h).strip().lower()
    return re.sub(r"[^\w\- ]", "", h).replace(" ", "-")

def anchors(path):
    text = re.sub(r"```.*?```", "", open(path, encoding="utf-8").read(), flags=re.S)
    return {slug(h) for h in re.findall(r"^#+ (.*)", text, re.M)}

bad = 0
for f in sorted(glob.glob("**/*.md", recursive=True)):
    if f.startswith(("node_modules/", "_site/")):
        continue
    text = re.sub(r"```.*?```", "", open(f, encoding="utf-8").read(), flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    for u in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"(https?:|mailto:)", u):
            continue
        path, _, anc = u.partition("#")
        target = os.path.normpath(os.path.join(os.path.dirname(f), path)) if path else f
        if not os.path.exists(target):
            print(f"MISSING  {f}: {u}"); bad += 1; continue
        if os.path.isdir(target):
            continue
        if anc and target.endswith(".md") and anc not in anchors(target):
            print(f"ANCHOR   {f}: {u}"); bad += 1
print(f"{bad} broken link(s)")
sys.exit(1 if bad else 0)

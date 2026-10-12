#!/usr/bin/env python3
"""Generic privacy check: flag email addresses, phone numbers, and street addresses in text files.
Allowed: GitHub noreply addresses and example.com/example.org addresses.
Usage: python3 tools/check_privacy.py [files...]  (default: all tracked text files)"""
import re, subprocess, sys

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
ALLOW_EMAIL = re.compile(r"(users\.noreply\.github\.com|@example\.(com|org|net)|@(you|user)\b)", re.I)
PHONE = re.compile(r"(?<![\w/.:-])(?:\+?1[ .-]?)?\(?\d{3}\)?[ .-]\d{3}[ .-]\d{4}(?![\w/-])")
STREET = re.compile(r"\b\d{1,6}\s+(?:[NSEW]\.?\s+)?[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+(?:Street|St|Avenue|Ave|Road|Rd|Drive|Dr|Lane|Ln|Court|Ct|Boulevard|Blvd|Way|Terrace|Circle)\b\.?")
EXTS = (".md", ".html", ".yml", ".yaml", ".py", ".txt", ".json", ".js", ".css")

files = sys.argv[1:] or [f for f in subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout.split() if f.endswith(EXTS)]
hits = 0
for f in files:
    try:
        lines = open(f, encoding="utf-8").read().splitlines()
    except (OSError, UnicodeDecodeError):
        continue
    for i, line in enumerate(lines, 1):
        for m in EMAIL.finditer(line):
            if not ALLOW_EMAIL.search(m.group(0)):
                print(f"EMAIL   {f}:{i}: {m.group(0)}"); hits += 1
        for m in PHONE.finditer(line):
            print(f"PHONE   {f}:{i}: {m.group(0)}"); hits += 1
        for m in STREET.finditer(line):
            print(f"ADDRESS {f}:{i}: {m.group(0)}"); hits += 1
print(f"{hits} possible privacy issue(s)")
sys.exit(1 if hits else 0)

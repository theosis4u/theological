---
title: "Sefaria Linker Demo"
sefaria_linker: true
reftagger: false
---

# Sefaria Linker Demo
{: .no_toc}

## Contents
{: .no_toc}

* Contents
{:toc}

---

## What this page shows

This page turns on Sefaria's free Linker (`sefaria_linker: true`) and turns off the NET Bible pop-ups (`reftagger: false`) so the two don't compete for Bible references. On the [website version](https://theosis4u.github.io/theological/examples/sefaria-linker-demo.html), click a reference below to see the Hebrew and English text from Sefaria.

## Example references

- Torah: Genesis 1:1 and Exodus 20:2.
- Mishnah: Mishnah Avot 1:1.
- Talmud: Berakhot 2a.
- Commentary: Rashi on Genesis 1:1.

## How it works

See [Pop-ups for other scriptures](../guides/logos-github-workflow.md#55-pop-ups-for-other-scriptures). The include is `_includes/sefaria-linker.html`, which loads `https://www.sefaria.org/linker.v3.js` and calls `sefaria.link()` in click-pop-up mode.

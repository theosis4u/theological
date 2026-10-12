---
title: "Quran Pop-up Demo"
quran_popups: true
---

# Quran Pop-up Demo
{: .no_toc}

## Contents
{: .no_toc}

* Contents
{:toc}

---

## What this page shows

This page turns on the opt-in Quran pop-ups (`quran_popups: true` in its front matter). On the [website version](https://theosis4u.github.io/theological/examples/quran-popup-demo.html), hover over or tab to each reference below to see the Arabic text and an English translation. Each reference also links to quran.com. On github.com, scripts are stripped, so you will see plain text.

## Example references

- The Throne Verse: Quran 2:255.
- The opening chapter: Surah 1:1-7.
- The chapter on sincerity: Qur'an 112:1-4.
- A single verse: Sura 36:1.

Ranges show at most ten verses in the pop-up. References inside code are left alone: `Quran 2:255`.

## How it works

See [Pop-ups for other scriptures](../guides/logos-github-workflow.md#55-pop-ups-for-other-scriptures) in the main how-to. The script is `_includes/quran-popups.html`; it calls the free, keyless Al Quran Cloud API, and the default English translation is Pickthall (1930, public domain in the US). Choose another edition with `quran_translation:` in front matter (for example `en.sahih` for Saheeh International, which is under copyright: attribute the translator, as the API's terms ask).

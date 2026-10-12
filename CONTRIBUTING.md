---
title: Contributing
---

# Contributing
{: .no_toc}

## Contents
{: .no_toc}

* Contents
{:toc}

---

Contributions are welcome, especially new tradition packs and corrections to existing ones.

## Adding a tradition pack

1. Copy an existing file in [`traditions/`](traditions/) to `traditions/<tradition-name>.md` (lowercase, hyphens).
2. Keep the same sections, in order:
   - **Authoritative standards** (confessions, catechisms, councils, or statements, and how they are cited)
   - **Key Fathers / theologians** (historic and modern)
   - **Study Bibles and Logos resources** (titles only)
   - **Translation preferences**
   - **Slot text: "your tradition first"** (one indented paragraph for section 4 of the method template)
3. Add a row to the table in [`traditions/README.md`](traditions/README.md).

## Style rules

- **Write as an insider would describe the tradition**, accurately and charitably. No polemic, no comparisons that score points against another tradition.
- **No "house view."** Don't write any tradition's position as "ours" or "the correct view."
- **Only list resources you are confident exist.** Mark anything uncertain _(verify in Logos)_. Never invent titles, editions, quotes, page numbers, or links.
- **No real ref.ly links or library quotations** in examples; use placeholders like `*[Placeholder: quote copied with Share > Copy]*` and `([ref.ly link])`. Never use angle brackets for placeholders outside code; the website treats them as HTML. Public-domain Bible text (e.g. KJV, WEB) may be quoted exactly.
- **No personal details**: no names, handles, emails, churches, locations, machine names, or paths containing a username. Use placeholders like `C:\Users\<you>\`.
- Plain prose, short lists, steps where useful. Gloss Greek or Hebrew terms once.

## Reference and link rules

- **Full Bible references only:** book, chapter, and verse ("John 3:16", "John 3:14–15"), never "v. 16" or "vv. 14–15". Pop-ups and Logos auto-linking need them.
- **Bible references in shared text** link to Biblia.com: `https://biblia.com/bible/<translation>/<Book><ch>.<v>` (e.g. `kjv1900`, `gs-netbible`).
- **Main passages** in examples get a *Compare + NET notes* link: `https://www.biblegateway.com/passage/?search=John%203:16&version=NET;NRSVUE;NKJV;KJV`.
- **Library quotes** keep their `ref.ly` link; add a free source link (CCEL, New Advent, confession sites) where one exists.
- **NET notes:** link to them; don't copy them into the repo (the free NET permission covers text, not notes).
- **Long pages** keep the auto table of contents (`{: .no_toc}` on the title and Contents heading, then `* Contents` and `{:toc}`).
- Read more in the [project history](docs/project-history.md).

## Forking and publishing your own site

1. **Fork** this repo on GitHub (or use the [starter kit](starter-kit/) for a private study repo). Keep personal notes in a private repo; publish only what you choose.
2. **Enable Pages:** **Settings > Pages**, source "Deploy from a branch", branch `main`, folder `/ (root)`. The site appears at `https://<user>.github.io/<repo>/`. Change `title` and `header_pages` in `_config.yml`.
3. **Set the pop-up translation:** edit `bibleVersion` in `_includes/reftagger.html` (e.g. `"NET"`, `"KJV"`, `"ESV"`, `"LEB"`). Keep `convertHyperlinks: true` with `hyperlinkTestList: ["biblia.com"]` if your text uses Biblia links, and `noSearchTagNames: ["code", "pre"]` so headings are tagged. Test one pop-up in a browser.
4. **Before each publish:** run a privacy grep over changed files (your name, family, friends, church, email addresses, handles, places), then wait for the Pages build and open a page to check it.

## Code

Scripts go in `tools/`, use the Python standard library where possible, contain no personal paths, and are documented in `tools/README.md`. Say how you tested them.

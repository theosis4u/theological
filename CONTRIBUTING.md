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

1. Copy an existing pack under [`traditions/`](traditions/README.md) into its family folder (e.g. `traditions/christian/<tradition-name>.md`) or a new family folder `traditions/<family>/README.md` (lowercase, hyphens).
2. Keep the same sections, in order:
   - **Authoritative standards** (confessions, catechisms, councils, or statements, and how they are cited)
   - **Key Fathers / theologians** (historic and modern)
   - **Free online sources** (verified to load; note sites that block automated checks)
   - **Paid or subscription resources (optional)** (real products only, briefly saying what they add, e.g. Logos libraries, specific commercial commentaries, journal access)
   - **Translation preferences**
   - **Slot text: "your tradition first"** (one indented paragraph for section 4 of the method template)
3. Add a row to the table in [`traditions/README.md`](traditions/README.md) (and the family index, e.g. `traditions/christian/README.md`).

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

## Contributing back instead of forking

You are encouraged to improve this shared repo rather than maintain a separate fork.

### Why contribute instead of fork

This is a one-person project, maintained with limited time and a limited weekly AI-assistant budget. Every pack fix, source, prompt, or guide improvement sent back as a pull request benefits everyone who uses it, while forks split the effort and drift out of date. Contributing directly is a win-win: thank you!

### What goes where

- **Your private study repo** (from the [starter kit](starter-kit/)): personal settings such as your tradition, stance, accounts, notes, and anything with personal data.
- **Upstream here, as pull requests:** generic improvements such as pack fixes, new sources, prompts, guides, and tools.

### The pull-request flow

1. Make a small, focused change on a branch. On GitHub, a fork is only the vehicle for the pull request: keep it in sync with this repo and don't run it as a separate project.
2. Run the privacy grep and the link check, and keep tables of contents.
3. Open a pull request that says what changed, why, and how you checked sources.
4. AI assistants may draft such changes, but propose them to the user first and open a pull request only with the user's approval.

### Optional and additive conventions

- **Add, don't overwrite:** add a new pack or section rather than rewriting another tradition's view.
- **Opt-in settings:** new behaviours (stances, modes, tools) are options the user chooses, not new defaults.
- **Tradition-neutral:** no "house view"; describe each view as its adherents would.
- **No personal data**, ever.

### Issues, pull requests, and automatic checks

- **Issue templates:** fix a pack (tradition and branch, what's wrong, and a source), add a source, add a prompt, or report a bug.
- **Pull-request template:** a checklist for no personal data, full references, edition named, the own-sources rule, and additive changes.
- **Checks:** an internal link and anchor check (`tools/check_links.py`) and a generic privacy check that flags email addresses, phone numbers, and street addresses (`tools/check_privacy.py`). Run both locally before opening a pull request; a GitHub Actions workflow to run them automatically on every pull request and push is planned.

### Review by adherents

Changes to a pack should be reviewed by people who belong to that tradition or branch where possible. Packs awaiting such review carry the **needs adherent review** label; each pack family has an open tracking issue inviting review. Say in the pull request whether you are an adherent or an outside summarizer.

## Forking and publishing your own site

1. **Fork** this repo on GitHub only if you need your own site (otherwise contribute upstream, above; for private study, use the [starter kit](starter-kit/)). Keep personal notes in a private repo; publish only what you choose.
2. **Enable Pages:** **Settings > Pages**, source "Deploy from a branch", branch `main`, folder `/ (root)`. The site appears at `https://<user>.github.io/<repo>/`. Change `title` and `header_pages` in `_config.yml`.
3. **Set the pop-up translation:** edit `bibleVersion` in `_includes/reftagger.html` (e.g. `"NET"`, `"KJV"`, `"ESV"`, `"LEB"`). Keep `convertHyperlinks: true` with `hyperlinkTestList: ["biblia.com"]` if your text uses Biblia links, and `noSearchTagNames: ["code", "pre"]` so headings are tagged. Test one pop-up in a browser.
4. **Before each publish:** run a privacy grep over changed files (your name, family, friends, church, email addresses, handles, places), then wait for the Pages build and open a page to check it.

## Pop-up scripts

To add pop-ups for another text source, follow the recipe in [Pop-ups for other scriptures](guides/logos-github-workflow.md#55-pop-ups-for-other-scriptures): one opt-in include per source, a CORS-enabled API with no secret key, translator attribution, and a demo page tested in a real browser.

## Code

Scripts go in `tools/`, use the Python standard library where possible, contain no personal paths, and are documented in `tools/README.md`. Say how you tested them.

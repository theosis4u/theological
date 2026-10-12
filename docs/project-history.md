---
title: "History"
date: 2026-10-12
topic: workflow
---

# Project History and Lessons Learned
{: .no_toc}

## Contents
{: .no_toc}

* Contents
{:toc}

---

## About this page

This page explains what was built in this repo, in roughly the order it was built, and **why** each decision was made. It is meant for people who fork the repo or contribute to it, so they can change things without undoing a choice that solved a real problem. Dates are approximate; the Git history has the details.

## 1. What was built

### 1.1 The core workflow

- **Main how-to** ([logos-github-workflow.md](../guides/logos-github-workflow.md)): Markdown in Git as the source of truth, Logos notes for reading and sharing, an AI assistant for drafting.
  *Why:* plain text is diffable, backed up, and readable by any assistant; Logos is where study partners read, and where the library lives.
- **Converter** (`tools/md_to_logos_html.py`): Markdown to the small HTML subset the Logos note editor accepts.
  *Why:* hand-formatting long notes in Logos was slow, and pasted Markdown loses structure.
- **Export tools** (`tools/note_save_server.py`, `tools/logos_notes_reader.py`): get notes back out of Logos.
  *Why:* notes written in Logos should not be stranded there.

### 1.2 The method, templates, and starter kit

- **Method template** ([ai-theology-method-template.md](../guides/ai-theology-method-template.md)): request types with lengths, source tiers, verification and honesty rules, quoting rules, and a "your tradition first" slot.
  *Why:* the assistant's answers improved most when the rules were written down once instead of repeated in each chat.
- **Starter kit, prompt library, tradition packs, examples.**
  *Why:* so anyone can copy a working setup and adapt it to their own tradition, without a "house view."
- **START-HERE onboarding prompt.**
  *Why:* the fastest way in is to hand the repo to an assistant and let it interview you one question at a time.

### 1.3 Guides for other setups

- **Copilot-only guide**, **starting points** (seeding a repo from old chats, posts, email, notes), **free resources** (no Logos needed), **setup checklist**, **AI coverage test**.
  *Why:* many people have only workplace Copilot, or no Logos, or years of scattered material.

### 1.4 The website and verse pop-ups

- **GitHub Pages** with the built-in Jekyll and the `minima` theme; README as the home page; a short `header_pages` nav.
  *Why:* no build pipeline to maintain, and readers without GitHub accounts get a clean site.
- **Reftagger** pop-ups set to NET, with `convertHyperlinks` for biblia.com links and `noSearchTagNames: ["code", "pre"]` so headings are tagged.
  *Why:* readers can see a verse without leaving the page. Defaults skipped existing links and headings, which hid most of our references.
- **Kramdown auto TOC** (`{:toc}` with `{: .no_toc}` on the title and Contents heading) on every long page.
  *Why:* a hand-written list drifted from the headings and read as confusing; the auto TOC is nested and always current.

### 1.5 Links and references

- **Biblia.com links** for Bible references in shared material, e.g. `https://biblia.com/bible/kjv1900/John3.16`.
  *Why:* `ref.ly` links open the Logos web app, which may show non-owners only a preview or a purchase prompt; Biblia opens with no sign-in.
- **Compare + NET notes** links to Bible Gateway (`version=NET;NRSVUE;NKJV;KJV`) at each main passage.
  *Why:* pop-ups show verse text only; Bible Gateway shows the NET translators' notes and a parallel view for free.
- **Full references everywhere** ("John 3:16", never "v. 16").
  *Why:* Reftagger and Logos auto-linking only recognize book, chapter, and verse.
- **Placeholders without angle brackets** (`*[Placeholder: …]*`).
  *Why:* `<like this>` is parsed as HTML on the site and disappears or breaks the line.

## 2. Decisions about the NET

- Reftagger's `NET` is Biblia's `gs-netbible`. Its wording matched the NET 2nd edition on netbible.org in every verse checked, so it is used for pop-ups.
- `netbible2ed` (the Logos 2nd-edition resource code) is not served to Reftagger or to non-owners on Biblia, so it can't be used for pop-ups.
- NET text is free to quote non-commercially; the **notes are not** covered by that permission. The site links to the notes rather than copying them. A permission request about showing NET notes has been sent to the NET publisher. See [Free resources: The NET Bible](../guides/free-resources.md#the-net-bible-text-notes-and-apis).

## 3. Lessons learned

### 3.1 Logos

- **The note editor strips `<blockquote>`.** Indent quotes with `<p class="ql-indent-1">` (the converter does this).
- **Copy with formatting beats anchors.** *Share > Copy* with citations and hyperlinked citations on gives a citation line and a `ref.ly` link that survive export to Markdown; anchors don't.
- **Paste as rich HTML.** On Linux, `xclip -selection clipboard -t text/html -i note.html` loads the clipboard directly; otherwise open the HTML in a browser and copy.
- **The notes list can lag** after creating a note, and canvas selection and limited view modes can confuse automation. Refresh, and check results by hand.
- **Desktop data copies go stale.** Work on fresh copies of local databases, read-only.

### 3.2 AI assistants

- **Treat AI answers as leads, not sources.** Open and quote the cited resource.
- **Test the Logos Study Assistant's coverage.** In matched-prompt tests, tradition-level questions retrieved owned resources unevenly between traditions; naming a resource or scoping to one book worked better. See the [coverage test](../guides/ai-coverage-test.md).
- **One question at a time** during onboarding gives better profiles than a long questionnaire.

### 3.3 Publishing

- **Private by default, public by choice.** Anonymize, run a privacy grep (names, emails, places, handles), and check the Pages build before calling anything published.
- **Verify every link by fetching it**, and drop what you can't confirm. Some sites block automated fetches, so try a second method before dropping.
- **Free books add up.** Logos, Verbum, and Faithlife Ebooks give away books monthly; a reminder or an assistant routine to check (never to claim without approval) builds a library over time. See [Building a free Logos library](../guides/free-resources.md#building-a-free-logos-library).

- **Avoid structural bias.** The Christian packs once sat at the root of `traditions/` while every other faith sat under a "world religions" subfolder, which made Christianity look like the default. Every family is now a peer folder under [traditions/](../traditions/README.md) (Buddhist, Christian, Hindu, Islam, Judaism, secular, and the rest), listed alphabetically, and the old URLs redirect to the new ones.

## 4. Open items

- NET notes in pop-ups: waiting on the permission request; until then, link out.
- A pop-up for the NET 2nd edition by its Logos code is not possible with Reftagger today.
- Logos and Faithlife URLs and free-book programs change; recheck links periodically.

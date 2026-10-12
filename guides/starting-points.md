---
title: "Starting Points: Seeding a Study Repo from Existing Material"
date: 2026-10-11
topic: workflow
---

# Starting Points: Seeding a Study Repo from Existing Material
{: .no_toc}

## Contents
{: .no_toc}

* Contents
{:toc}

---

## About this guide

You probably already have years of theological material scattered across AI chats, social media, email, Logos, documents, and lecture notes. This guide covers optional ways to collect it, clean it, sort it by topic, and commit it to your **private** study repo (see the [starter kit](../starter-kit/)). Do as many or as few sections as you like; the [common pipeline](#8-the-common-pipeline) at the end applies to all of them.

> **About export paths:** export features change. The steps below summarize each provider's public help pages as of late 2026, with links where available. Check the current page before you start; work and school accounts often have different rules or none.

Haven't set up yet? Run the onboarding prompt in [START-HERE.md](../START-HERE.md) first; it asks which of these sources you want to import.

**General cautions for every source**

- **Read-only on the source.** Export or copy; never delete, edit, or rename originals while collecting.
- **Private by default.** Everything lands in a private repo. Publish only items you deliberately choose, in a separate public repo, after a privacy grep.
- **Other people's words.** Messages, posts, and emails from others belong to them. Summarize rather than reproduce, strip their addresses and personal details, and ask before sharing their words anywhere.
- **Licensed text.** Don't copy book text in bulk from Logos or elsewhere. Keep short quotations with citations.

---

## 1. AI chat history

**What you get:** your past questions and the assistant's answers, often the richest record of how your thinking developed.

**How to collect it:**

| Assistant | Official route (verify on the linked page) |
|---|---|
| ChatGPT | Settings > Data controls > Export data; a ZIP with `conversations.json` and HTML is emailed. Not available for some business workspaces. [OpenAI help](https://help.openai.com/en/articles/7260999-export-your-data-from-chatgpt) |
| Claude | Settings > Privacy > Export data (web or desktop); a download link is emailed. Team/Enterprise exports are owner-only. [Claude help](https://support.claude.com/en/articles/9450526-export-your-claude-data) |
| Grok | xAI account data download (reported to be at `accounts.x.ai` and reachable from Grok's data-control settings) as JSON. Check xAI's current help pages. |
| Microsoft Copilot | No account-wide chat export is documented for consumer Copilot at the time of writing; save, share, or copy one conversation at a time. Work accounts may be governed by your organization. |

If there is no export, or you only want a few chats: open each chat, scroll to the end so it fully loads, and either copy the text or print to PDF. Convert PDFs with [`tools/chat_pdf_to_md.py`](../tools/README.md#chat_pdf_to_mdpy).

**Filtering theology from everything else:** list every chat with its title and date, run [`tools/classify_topics.py`](../tools/README.md#classify_topicspy) or search titles for your keywords, mark each one keep / skip, and then do a **human review pass**. Titles are often misleading.

**Privacy and consent:** chats may contain personal, family, health, or work details unrelated to theology. Remove them or skip the chat.

**Prompt:**

```text
Below is one exported AI chat (JSON or text). Convert it into Markdown:
- YAML front matter: title, source (URL or "export"), source_type: ai-chat, date (YYYY-MM-DD of first message), topic (choose from: <your topic folders>), original_project (<project/folder name or blank>).
- "# <title>", then "## User" / "## Assistant" sections in order.
- Remove interface text; fix line wraps; keep lists, quotes, and links.
- Do not summarize or reword. If a section contains personal details unrelated to the topic (names, addresses, health, work), replace them with [redacted] and list what you redacted at the end, outside the Markdown.
```

## 2. X (Twitter) posts and threads

**What you get:** your own posts, threads, and replies, which are useful for tracking arguments you have made in public.

**How to collect it:**

- **Official archive:** X's "Download an archive of your data" (in account settings) produces a ZIP; your posts are in a JavaScript file such as `data/tweets.js`. See [X help: how to download your X archive](https://help.x.com/en/managing-your-account/how-to-download-your-x-archive). It can take a day or more to arrive.
- **X API or connected apps:** if you have API access or an assistant connected to your X account, you can pull your own posts, threads, and replies by date or keyword. Access tiers and limits change; check X's developer documentation.
- **By hand:** for a few threads, copy the text and keep the post URLs.

**Rebuilding threads:** in the archive, replies to yourself share a conversation and reference the post they reply to. Group them in order to reconstruct each thread.

**Public vs. private:** your public posts are already public, but your *collection* of them (with notes) can still be private. Decide per item.

**Others' posts:** don't republish other people's posts wholesale. Quote briefly, link to the original, and summarize the rest.

**Prompt:**

```text
Below are my own posts exported from X (JSON lines with id, created_at, full_text, in_reply_to). 
1. Keep only posts about theology or Bible study (list the ones you excluded by id).
2. Group replies into threads in chronological order.
3. For each thread, output a Markdown file with front matter: title, source (https://x.com/i/web/status/<first id>), source_type: x-thread, date, topic (from: <your topic folders>).
4. Quote my posts exactly. Where I reply to someone else, summarize their point in one sentence and link it; do not copy their text or handle.
```

## 3. Email threads

**What you get:** longer discussions with study partners, teachers, or correspondents.

**How to collect it:**

- **Through an AI assistant's connected apps:** if you have connected Gmail or Outlook to your assistant, ask it to search by theological keywords or by correspondent and summarize matching threads. It acts with your account's access, so keep requests narrow.
- **Google Takeout:** export Gmail (optionally just certain labels) as `.mbox`. [Google Takeout help](https://support.google.com/accounts/answer/3024190)
- **Outlook:** export to a `.pst` file from the desktop app, or save individual messages. See Microsoft's support pages for "export emails to a .pst file".

**Handling:** search by keywords (book names, doctrines, passages) or by correspondent; **summarize rather than dump**; strip other people's email addresses, phone numbers, and personal details; keep your own words when useful.

**Privacy and consent:** email threads go in the **private repo only**. Get consent before sharing anyone else's words, even with a single friend.

**Prompt:**

```text
Below is an email thread. Produce a Markdown note:
- Front matter: title, source: email, source_type: email-thread, date (first message), topic (from: <your topic folders>).
- Refer to people only as "me" and "Correspondent A/B". Remove all email addresses, phone numbers, signatures, and personal details.
- Summarize each message in 2-4 sentences. Quote my own words exactly only where they state an argument. Quote others only briefly, and mark those quotes "(shared with permission?)" for me to check.
- End with "Open questions" raised in the thread.
```

## 4. Logos notes, highlights, and sermon or class notes

**What you get:** your notes and notebooks, highlight text, and any sermon or class notes kept in Logos.

**How to collect it:**

- **Web app copy:** open each note, copy its body, and save it with [`tools/note_save_server.py`](../tools/README.md#note_save_serverpy); convert with pandoc. See the [workflow guide](logos-github-workflow.md#4-exporting-logos-notes-back-to-markdown).
- **Desktop database:** with Logos closed, copy the notes database and explore it read-only with [`tools/logos_notes_reader.py`](../tools/README.md#logos_notes_readerpy). The schema is undocumented.
- Check Logos's own help for any built-in export or print options for notes and sermon documents.

**Cautions:** notes may include quoted book text; keep quotes short and cited. Shared notebooks may contain others' notes.

**Prompt:**

```text
Below is the HTML of a Logos note. Convert it to Markdown:
- Front matter: title (first line of the note), source: logos-note, source_type: logos-note, date (<date>), topic (from: <your topic folders>), logos_note: "<notebook> / <title>".
- Turn indented paragraphs into ">" quotes, keep the citation line and its ref.ly link under each quote.
- Keep all Bible references and links; do not reword.
```

## 5. Documents: Word, Google Docs, OneNote

**What you get:** papers, handouts, outlines, and study notes.

**How to collect it:**

- **Word:** keep `.docx`; convert with `pandoc -f docx -t gfm file.docx -o file.md`.
- **Google Docs:** File > Download offers Markdown and `.docx`; or export many at once with Google Takeout (Drive).
- **OneNote:** export pages or sections (for example to Word or PDF) from the desktop app where available, then convert. Options vary by version; check Microsoft's help.

**Cautions:** shared documents may contain collaborators' comments and names; remove them unless you have consent.

**Prompt:**

```text
Below is a document converted to Markdown by pandoc. Clean it:
- Add front matter: title, source (<file name or URL>), source_type: document, date (<date>), topic (from: <your topic folders>).
- Fix heading levels, remove leftover styles and comments, keep tables and quotes, keep all wording.
- List any names or personal details of other people at the end so I can decide whether to remove them.
```

## 6. YouTube and lecture transcripts

**What you get:** analysis notes on lectures, debates, and sermons.

**How to collect it:** where the platform offers a transcript (for example YouTube's "Show transcript" on videos that have one), copy it. Respect the platform's terms and the speaker's rights: transcripts are for your **analysis notes**, not for republishing.

**Prompt:**

```text
Below is a lecture transcript from <speaker>, "<title>" (<URL>), <date>.
Write analysis notes, not a transcript:
- Front matter: title, source (URL), source_type: lecture, date, topic (from: <your topic folders>), speaker.
- Outline the main claims with timestamps.
- Quote at most a few short lines exactly, with timestamps.
- List every factual or historical claim that needs checking against primary sources.
```

---

## 7. E-book libraries (optional)

Your highlights and notes in e-book readers are often the best record of what you've studied. **Prefer highlight exports**: they are official, fast, and contain only what you chose. Checked against each provider's help pages and user reports on 2026-10-12; features change, so confirm on the linked pages.

| Library | Best route | What you get | Limits (as reported) |
|---|---|---|---|
| **Kindle** | [Kindle Notebook](https://read.amazon.com/notebook) (`read.amazon.com/notebook`), signed in | Highlights and notes per book, with locations; users report an export option (text, HTML, or CSV) on the book view | No public API. DRM prevents exporting the books themselves. Publishers set a clipping limit (commonly reported as about 10% of a book), so some highlights may be hidden or cut off. A physical Kindle's `My Clippings.txt` holds that device's highlights. |
| **Kindle Cloud Reader** | `read.amazon.com`, signed in | Reading a specific passage for a lookup | Users report some titles aren't available in Cloud Reader; copying is limited by the same clipping limit. |
| **Kobo** | kobo.com: **My Books > Actions > Export Annotations** ([Kobo help](https://help.kobo.com/hc/en-us/articles/29991333812631-Export-annotations-from-your-books)) | Highlights and notes as PDF, HTML, TXT, or Markdown | Only books bought from Kobo or Kobo Plus; may depend on publisher approval; markups aren't exported; files are kept for 30 days. Alternative: copy `.kobo/KoboReader.sqlite` from the eReader and read the `Bookmark` table (community tools such as `export-kobo`; unofficial; work on a copy). |
| **Google Play Books** | In a book, **More > Save annotations to Google Drive** ([Google help](https://support.google.com/googleplay/answer/3165868)) | One Google Doc per book in a Drive folder named "Play Books Notes" by default, which an assistant with a Google Drive connector can read | Highlight text is missing if the publisher disabled copying or the publisher's limit is exceeded. Editing the synced doc can be overwritten; make a copy first. |
| **Apple Books** | In a book, open **Notes**, then Control-click a note > **Share** (Mail, Messages, Notes) ([Apple help](https://support.apple.com/guide/books/share-book-quotes-notes-and-more-ibks3b8c08a0/mac)) | Notes and highlights you share, a few at a time | No web reader and no bulk export in the app; quote sharing is limited (Apple notes up to 200 words, US only). Community Mac tools read the local Books database (unofficial). |
| **Libby / OverDrive** | Title's **Reading Journey > Actions > Export Reading Data** ([Libby help](https://help.libbyapp.com/6151.htm)) | Highlights with notes, chapter, color, and dates, as a web table or spreadsheet (a JSON "Data" option is also reported); works after the loan ends | One title at a time. |
| **DRM-free EPUB or PDF files you own** | Upload the file or put it in your repo or drive | The whole text, which your assistant can read directly | Respect the license: keep purchased books private. |

**Guidance**

- **Signed-in readers are for lookups, not whole books.** An AI assistant with a browser can read a signed-in Kindle or Play Books page, but slowly, page by page. Use it to find or check a specific passage, not to copy a book.
- **You do the sign-ins.** The assistant should never ask for your password; you sign in to the reader yourself (or in the assistant's browser if it offers that), and approve what it opens.
- **Quote briefly, cite, and never republish whole chapters** publicly. Keep highlight exports in your **private** repo.
- **Respect each service's terms of service**, and don't try to bypass DRM or clipping limits.

**Prompt for your assistant**

```text
Here are my highlight exports from [Kindle / Kobo / Play Books / Apple Books / Libby]. Convert each book's highlights into one Markdown file with front matter (title, author, source: "<service> highlights export", source_type: ebook-highlights, date, topic). Keep each highlight as a short quote with its location, and my notes beneath it. Suggest a topic folder for each file. Don't add text that isn't in the export, and flag any highlight that looks cut off.
```

## 8. The common pipeline

1. **Inventory first.** Before converting anything, list what you have: title, date, source, URL or file, size. Don't change any source.
2. **Propose a folder layout** from the inventory and review it before sorting. Start with the starter kit's folders and add topic folders as needed.
3. **Classify.** Run `tools/classify_topics.py` or the classification prompt below, then correct the CSV by hand.
4. **Dedupe** against files already in your repo (same title and date, or same source URL).
5. **Clean** each item with the prompts above. Keep content intact: fix formatting, don't reword.
6. **Add front matter** to every file:

   ```yaml
   ---
   title: "..."
   source: "<URL, file name, or export name>"
   source_type: ai-chat | x-thread | email-thread | logos-note | document | lecture
   date: YYYY-MM-DD
   topic: <folder>
   original_project: "<project, notebook, or label it came from>"
   ---
   ```

7. **Name and place** files as `topic/YYYY-MM-DD-short-slug.md`.
8. **Rebuild the index:** `python3 tools/build_index.py . -o INDEX.md`.
9. **Commit** in batches by source (for example "Import AI chats: soteriology"), in the **private** repo.
10. **Publishing (optional):** copy only chosen items to a separate public repo, after a privacy grep for names, handles, emails, places, and anything else personal.

### Example inventory

| # | Source type | Title | Date | Source | Size | Proposed topic | Keep? |
|---|---|---|---|---|---|---|---|
| 1 | ai-chat | "Grace and works in James 2" | 2025-03-02 | export: conversations.json #41 | 18 turns | soteriology | yes |
| 2 | ai-chat | "Trip packing list" | 2025-03-05 | export #42 | 6 turns | n/a | no |
| 3 | x-thread | "Thread on Psalm 82" | 2025-06-10 | https://x.com/i/web/status/[id] | 7 posts | scripture-and-canon | yes |
| 4 | email-thread | "Notes after Romans 3 call" | 2025-09-14 | mbox: label "Study" | 5 msgs | soteriology | yes (summarize) |
| 5 | logos-note | "Week 2 notes" | 2026-01-20 | notebook "[class]" | 1,900 words | class-notes | yes |

### Topic-classification prompt

```text
Here is an inventory of items (title, date, source type, first 300 characters).
Topic folders: <list your folders, each with a one-line description>.
For each item, return a CSV row: number, suggested topic, confidence (high/medium/low), theology? (yes/no), one-line reason.
Use "unsorted" when unsure. Do not invent content beyond what is shown.
```

### Keyword classifier script

```bash
python3 tools/classify_topics.py --example-map > topics.json   # edit to your folders and keywords
python3 tools/classify_topics.py imports/ --map topics.json -o suggestions.csv
```

It scores title matches higher than body matches, writes `file, title, topic, score, runner_up, theology_likely, matched` to a CSV, and never moves files. Review the CSV, then move files yourself.

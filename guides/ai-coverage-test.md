---
title: "Testing an AI Study Assistant's Coverage of Your Library"
date: 2026-10-11
topic: workflow
---

# Testing an AI Study Assistant's Coverage of Your Library

In-app AI assistants, including the Logos Study Assistant, answer by retrieving passages from resources and summarizing them. Retrieval is never perfect, and coverage can differ by tradition, publisher, or resource type. A resource you own may be cited constantly, rarely, or never. This kit gives you a simple, repeatable way to find out how it behaves with *your* library before you rely on it, and to report problems with useful detail.

The goal is measurement, not accusation. Run the same tests for every tradition you care about, including your own.

## 1. Setup

1. List 4–8 resources you own from **tradition A** and the same number from **tradition B** (for example, a study Bible, a catechism or confession, a collection of early writers, and a commentary from each). Confirm each one opens and is searchable with ordinary Logos search.
2. Pick 3–5 passages or topics both traditions address (for example John 1:1–5, Psalm 23, or baptism in Romans 6).
3. Note your software version, platform (desktop or web), date, and the assistant's scope setting.

## 2. The matched-prompt test

For each topic, ask questions in pairs that differ only in the tradition named. Keep the wording otherwise identical.

| Level | Tradition A prompt | Tradition B prompt |
|---|---|---|
| Tradition-level | "Using only my books, how does the `<A>` tradition interpret `<passage>`?" | "Using only my books, how does the `<B>` tradition interpret `<passage>`?" |
| Named-resource | "What does `<A resource title>` say about `<passage>`?" | "What does `<B resource title>` say about `<passage>`?" |
| Named-writer | "What does `<A writer>` say about `<passage>`, from my library?" | "What does `<B writer>` say about `<passage>`, from my library?" |

Run each pair with the scope set to **Your books**.

### Control: single-book scope

If the assistant lets you limit scope to one resource (or if you open the resource and ask from within it), repeat the named-resource question with only that book in scope. If it answers well with one book in scope but not with "Your books," the content is there and searchable; the problem is in retrieval or ranking across the library. If it fails even with one book, the resource may not be indexed for the assistant.

### Control: ordinary search

Search the same resource for the passage reference or a key phrase with regular Logos search. A hit there plus a miss in the assistant points to the assistant rather than the resource.

Repeat each prompt at least twice (answers can vary), and on both desktop and web if you use both.

## 3. Recording results

Use one row per prompt run:

| # | Date | Platform / version | Scope | Prompt (exact) | Expected resources | Resources actually cited | Used general knowledge? | Correct? | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | Your books | | | | yes / no | yes / partly / no | |

Then summarize per tradition: how many of your owned resources were cited at least once, how many prompts fell back to general knowledge, and whether any answer cited sources from a different tradition than the one asked about.

Save screenshots of answers and the cited-sources panel, and save the answer text with its links (copy it into your repo).

## 4. Interpreting results fairly

- A gap in one tradition may also exist in others; compare before concluding.
- Some resources may not be indexed for AI features at all, by publisher choice or for technical reasons. That is still worth reporting.
- Wording matters: try synonyms the tradition itself uses.
- A small sample is a lead, not proof. Report what you saw and how often.

## 5. Bug-report template

```text
Subject: Study Assistant does not retrieve owned resources for <topic/tradition>

Product: Logos <desktop/web>, version <x.y>, <OS/browser>
Date(s) tested: <dates>
Scope setting: Your books

Summary:
When asked about <topic> with scope "Your books", the assistant <did not cite / cited only> ...
Owned resources expected: <titles>
Resources cited instead: <titles> / general knowledge

Steps to reproduce:
1. Set scope to "Your books".
2. Ask: "<exact prompt>"
3. Observe cited sources.

Controls:
- Ordinary search for "<phrase or reference>" in <resource>: <found / not found>
- Single-resource scope (if available): <result>
- Matched prompt for <other tradition>: <result>

Repeat count: <n> runs, <n> failures
Expected: answer grounded in the owned resources listed above.
Actual: <what happened>
Attachments: screenshots, results table
```

Send it through the in-app feedback option or Faithlife's support channels, and keep a copy in your repo.

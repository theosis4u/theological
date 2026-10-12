# Contributing

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
- **No real ref.ly links or library quotations** in examples; use placeholders like `<ref.ly link from your Logos copy>`. Public-domain Bible text (e.g. KJV, WEB) may be quoted exactly.
- **No personal details**: no names, handles, emails, churches, locations, machine names, or paths containing a username. Use placeholders like `C:\Users\<you>\`.
- Plain prose, short lists, steps where useful. Gloss Greek or Hebrew terms once.

## Code

Scripts go in `tools/`, use the Python standard library where possible, contain no personal paths, and are documented in `tools/README.md`. Say how you tested them.

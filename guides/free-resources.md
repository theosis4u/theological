---
title: "Free Resources"
date: 2026-10-11
topic: workflow
---

# Free Resources for Exegesis and Theology
{: .no_toc}

## Contents
{: .no_toc}

* Contents
{:toc}

---

## About this guide

You don't need Logos to follow this workflow. The free sites below are stable, widely used, and scholarly enough for serious study. Every link was checked on 2026-10-11 and opened without signing in. Sites change, though, so "free" here means free to read at the time of checking. Some offer paid tiers or donations, and modern translations and commentaries remain under copyright.

Use these in place of the Logos library in the [method template](ai-theology-method-template.md) (see "Free-resource mode" in section 3 there).

## 1. Cross-tradition core

### Bible text, notes, and original languages

| Site | Good for |
|---|---|
| [NET Bible](https://netbible.org/) | The NET translation with its extensive translator notes on text, grammar, and translation choices |
| [STEP Bible](https://www.stepbible.org/) (Tyndale House, Cambridge) | Original-language tagging, lexicon entries, and word searches across Hebrew and Greek |
| [Blue Letter Bible](https://www.blueletterbible.org/) | Interlinear with Strong's numbers, lexicons, and many older commentaries |
| [Bible Hub](https://biblehub.com/) | Parallel versions of a verse, interlinears, and quick access to public-domain commentaries |
| [Bible Gateway](https://www.biblegateway.com/) | Reading and comparing many modern translations side by side |
| [Open Scriptures](https://openscriptures.org/) | Open-licensed data projects such as morphologically tagged Hebrew Bible text |
| [eBible.org](https://ebible.org/) | Public-domain and openly licensed Bible texts for download, including the [Brenton Septuagint](https://ebible.org/details.php?id=grcbrent) and the [LXX (Greek)](https://ebible.org/find/details.php?id=grcLXX) |

### Primary sources and history

| Site | Good for |
|---|---|
| [CCEL](https://www.ccel.org/) (Christian Classics Ethereal Library) | Public-domain classics: [Ante-Nicene](https://www.ccel.org/ccel/schaff/anf01) and [Nicene and Post-Nicene Fathers](https://www.ccel.org/ccel/schaff/npnf101), Schaff's [*Creeds of Christendom*](https://www.ccel.org/ccel/schaff/creeds3), Reformation and Puritan works such as Calvin's [*Institutes*](https://www.ccel.org/ccel/calvin/institutes) |
| [Perseus Digital Library](https://www.perseus.tufts.edu/hopper/) | Classical Greek and Latin texts and lexica (including LSJ), useful for word usage outside the Bible |
| [Sefaria](https://www.sefaria.org/) | Jewish texts (Tanakh, Second Temple works, rabbinic literature) for Old Testament and Jewish background |

### Indian philosophy survey

- **Survey anthology:** Sarvepalli Radhakrishnan and Charles A. Moore (eds.), *A Sourcebook in Indian Philosophy* (Princeton University Press, 1957; paperback ISBN 9780691019581; an ebook edition is listed as ISBN 9781400865062). [Borrow free at the Internet Archive](https://archive.org/details/sourcebookinindi00radh) (a 1989 printing, through controlled digital lending: a free account and one-hour borrows) or see the [Princeton page](https://press.princeton.edu/books/paperback/9780691019581/a-sourcebook-in-indian-philosophy). It is a mid-20th-century anthology, and Radhakrishnan writes from a modern Advaita (Neo-Vedanta) perspective, so balance its introductions with each tradition's own sources. Useful for the [Hindu](../traditions/hindu/README.md), [Buddhist](../traditions/buddhist/README.md), and [Jain](../traditions/jain/README.md) packs, and for Carvaka materialism in the [secular](../traditions/secular/README.md) pack.

### Academic and open-access scholarship

| Site | Good for |
|---|---|
| [Tyndale Bulletin](https://tyndalebulletin.org/) | Peer-reviewed biblical studies articles, with an open archive |
| [BiblicalStudies.org.uk](https://biblicalstudies.org.uk/) | Thousands of free articles and out-of-copyright books in biblical studies and theology, often with publisher permission |
| [Internet Archive](https://archive.org/) | Scans of public-domain commentaries, lexicons, and patristic editions |
| [Google Books](https://books.google.com/) | Full view of many public-domain (generally pre-1929) works; searchable inside books |

### Free Logos options

| Option | Notes |
|---|---|
| [Logos free version](https://www.logos.com/basic) | Logos's own page describes a free version with a small library (stated as "25+" resources) and a simple set of study tools, on desktop, web, and mobile. Contents and features may change; check the page. |
| [Free book of the month](https://www.logos.com/free-book-of-the-month) | A rotating free title; it requires a Faithlife account. |
| [Logos web app](https://app.logos.com/) and [Faithlife](https://www.faithlife.com/) | Web access after signing in; Faithlife also offers other apps. Free features vary by account. |

### The NET Bible: text, notes, and APIs

The NET is unusual: its text is free to quote for non-commercial use, and its 60,000 translators' notes are free to *read* online. Findings from testing on 2026-10-11 (tested by request; none of these is an endorsement):

| Source | Edition | Notes? | Access | Example |
|---|---|---|---|---|
| [netbible.org](https://netbible.org/) | 2nd edition (its default text is labelled NET2) | Yes, all notes, in the reader | Free to read. The page loads text and notes from internal endpoints that are undocumented and don't allow other websites to call them. | `https://netbible.org/bible/John+3` |
| [labs.bible.org API](https://labs.bible.org/api_web_service) | Matched NET2 wording in every verse checked | No (`formatting=full` gives note *markers* only) | Free, no key; allows cross-site calls and JSONP (`&callback=`) | `https://labs.bible.org/api/?passage=John%203:16&type=json` |
| Bible Gateway | 2nd-edition-era text (copyright line 1996–2017); one minor spelling difference found in 226 verses | Yes, as footnotes | Free to read; no public API | `https://www.biblegateway.com/passage/?search=John%203:16&version=NET;NRSVUE;NKJV;KJV` |
| Biblia.com / Reftagger (`gs-netbible`) | Matched NET2 wording in the verses checked | No | Free to read; `netbible2ed` needs sign-in or purchase | `https://biblia.com/bible/gs-netbible/John3.16` |
| [bolls.life](https://bolls.life/) (third-party) | Matches NET2 in the verses checked | Yes, in a `comment` field | Free, no key, allows cross-site calls | `https://bolls.life/get-verse/NET/43/3/16/` |
| Logos | *The NET Bible: Full Notes Edition* (2nd ed.) | Yes | Paid resource | — |

**Licensing.** NET Bible text may be quoted without written permission for non-commercial use with "(NET)" and the copyright notice; commercial use has a 500-verse limit (see [Bible.org's copyright page](https://bible.org/netbiblecopyright)). That free permission covers the text **without the notes**, and Bible.org's material may not be reposted on other websites. So link to the notes (netbible.org, Bible Gateway) rather than copying them into a public site or a pop-up. For this repo, a permission request about showing NET notes has been sent to the NET publisher; until permission is granted, the site shows verse text only and links out for notes.

## Building a free Logos library

You can build a useful Logos library at no cost by claiming free books regularly. Checked 2026-10-11; offers and URLs change.

### 1. Choose an account

- **(a) A dedicated assistant account.** If your AI assistant platform can give the assistant its own email inbox (Grok Bot can, for example), have it claim one and use it for a separate free Faithlife account the assistant can operate. This keeps your personal or paid Logos account separate from anything the assistant does.
- **(b) Your own personal email.** Simpler, and books you claim land in your own library.

Either way: **you approve every sign-up**, and passwords go in a password manager, never in a chat, a prompt, or the repo.

### 2. Free books each month

Logos's help page ["How do I get this month's free Logos book?"](https://support.logos.com/hc/en-us/articles/360031310291-How-Do-I-Get-This-Month-s-Free-Logos-Book) lists several monthly offers. The pages below loaded on the check date; offers may require signing in to a free Faithlife account.

| Offer | Link | Notes |
|---|---|---|
| Logos free book of the month | [logos.com/free-book](https://www.logos.com/free-book) | The help page says it refreshes partway through the month, so about two books a month |
| Verbum (Catholic) free book | [logos.com/another-free-book](https://www.logos.com/another-free-book) | Also reachable from [verbum.com/free-book-of-the-month](https://verbum.com/free-book-of-the-month) |
| Subscriber free book | [logos.com/free-book/subscriber](https://www.logos.com/free-book/subscriber) | For Logos subscription holders only |
| Free ebook and audiobook | [logos.com/free-ebook-and-audiobook](https://www.logos.com/free-ebook-and-audiobook) | The older links logos.com/free-ebook and /free-audiobook currently redirect to the monthly sale page |

Lexham Press titles have often appeared among these freebies. There is no separate Lexham free-book page; see "Faithlife's family of sites" below for why. Claiming each month adds up to a sizable library over a few years. Set a **monthly reminder** (for example the 1st and 16th), or ask an assistant with calendar access to remind you; it should never claim or sign up without your approval.

### Faithlife's family of sites

Logos is one of several sites run by the same company, Faithlife, LLC. According to [Faithlife's history page](https://faithlife.com/history) and [fast facts](https://faithlife.com/fast-facts), it began in 1992 as Logos Research Systems and rebranded as Faithlife in 2014. Recent press releases refer to the company as Logos. Each site below loaded on 2026-10-11.

| Site | What it is | Useful for free study? |
|---|---|---|
| [Logos](https://www.logos.com/) and [app.logos.com](https://app.logos.com/) | The Bible software, store, and web app | **Yes:** free version, free-book pages, $0 store search, previews |
| [Verbum](https://verbum.com/) | The Catholic edition of Logos | **Yes, for Catholic resources:** its own monthly free book |
| [Biblia.com](https://biblia.com/) | A free online Bible reader. On the check date it opened to John 1 in the ESV with cross-reference letters and footnotes. | **Yes:** reading and comparing Bible texts in the browser without the Logos app |
| [Faithlife.com](https://faithlife.com/) | Community groups and accounts | **Somewhat:** home of the Free Faithlife Books group |
| [Faithlife Ebooks](https://ebooks.faithlife.com/) | Ebook store and reader, formerly Vyrso (launched 2011, per the fast facts) | **Yes:** its own [$0 search](https://ebooks.faithlife.com/search?query=price%3A0.00) |
| [Proclaim](https://proclaim.logos.com/) | Church presentation software for slides and worship | **No:** not a study tool |

**NET on these sites.** Verse pop-ups (Reftagger) show verse text only. At each main passage, add a *Compare + NET notes* link to Bible Gateway, e.g. `https://www.biblegateway.com/passage/?search=John%203:16&version=NET;NRSVUE;NKJV;KJV`, which shows the passage in parallel with the NET translators' notes as footnotes (a 2nd-edition-era NET text; its copyright line reads 1996–2017). The free NET on Biblia.com is `gs-netbible` (e.g. `https://biblia.com/bible/gs-netbible/John3.16`); `netbible2ed` there requires sign-in or purchase. The full NET 2nd edition with all notes is free to read at [netbible.org](https://netbible.org/) and is available in Logos (*The NET Bible: Full Notes Edition*, 2nd ed.). Use full references in these links.

**Lexham Press**, formerly Faithlife's in-house imprint (publisher of the LEB, the Lexham Bible Dictionary, and the Faithlife Study Bible), was acquired by Baker Publishing Group on September 23, 2025, according to the [Logos newsroom](https://www.logos.com/newsroom/baker-acquires-lexham-press) and [Baker's announcement](https://bakerpublishinggroup.com/pages/baker-publishing-group-acquires-lexham-press-strengthening-partnership-in-christian-publishing). The announcements say Logos keeps the rights to Lexham content within Logos, so the digital titles stay in Logos libraries. Old Lexham free-book addresses now redirect to a Baker bookstore search, which is why this guide has no Lexham free-book page.

**Wordsearch Bible** was acquired from LifeWay in 2020, and its users were moved onto Logos with Logos-compatible editions of the titles they owned ([Baptist Press](https://www.baptistpress.com/resource-library/news/lifeway-sells-wordsearch-to-logos-bible-software-creator-faithlife/); also listed in Faithlife's fast facts). If you used Wordsearch, check your Logos library for those titles.

### 3. Free previews of books you don't own

Users report that the Logos web app and `ref.ly` links **may show a limited preview** of a passage in a book you don't own, sometimes without signing in. On the check date, a public link such as `https://ref.ly/Jn3.16` redirected to the Logos web app (`app.logos.com/books/...`) without requiring sign-in; how much text is shown depends on the book and your account. Treat previews as a way to check a quote's context, quote briefly, and cite the source; don't copy previews in bulk.

### 4. Getting alerted to free books

- **Email:** Logos's help page says you can sign up for free-book notifications at the bottom of the [free book page](https://www.logos.com/free-book).
- **Community group:** the [Free Faithlife Books](https://faithlife.com/free-books) group on Faithlife is a user-run group that posts free books and 100%-off deals from Logos, Verbum, Faithlife Ebooks, and Lexham Press. Following it gives notifications. It's unofficial, so check each offer on the store page.
- **Deals pages:** the [monthly sale](https://www.logos.com/monthly-sale) and [Verbum's monthly page](https://verbum.com/monthly-sale) list the current free book with that month's discounts.

### 5. Searching the store for $0 resources

On the check date, this Logos store search returned items currently priced at $0.00 that you don't already own:

[`https://www.logos.com/search?query=price%3A0.00&limit=60&ownership=unowned`](https://www.logos.com/search?query=price%3A0.00&limit=60&ownership=unowned)

The query `price:0.00` filters by price, and `ownership=unowned` hides what you already have (the filter only works when signed in). The results included study resources such as the Faithlife Study Bible, Lexham Bible Dictionary, Lexham English Bible, the abridged Brown-Driver-Briggs lexicon, and Codex Sinaiticus, along with fiction, videos, and short devotionals. Prices change and some $0 prices may depend on your account, so check the price on the product page before claiming. The same query works on the Faithlife Ebooks store: [`https://ebooks.faithlife.com/search?query=price%3A0.00`](https://ebooks.faithlife.com/search?query=price%3A0.00).

## 2. By tradition

Each list matches a [tradition pack](../traditions/). Descriptions are of what a site offers, not an endorsement of its positions.

### Eastern Orthodox
- [OCA.org](https://www.oca.org/): the Orthodox Church in America's site, with an [Orthodox Faith](https://www.oca.org/orthodoxy/the-orthodox-faith) series on doctrine, Scripture, and worship, plus lives of saints and readings.
- [Greek Orthodox Archdiocese of America](https://www.goarch.org/): daily readings, the liturgical calendar, and articles on faith and worship.
- [OrthodoxWiki](https://orthodoxwiki.org/): community encyclopedia; good for quick orientation, but verify its claims elsewhere.
- [Brenton Septuagint](https://ebible.org/details.php?id=grcbrent) and [LXX Greek text](https://ebible.org/find/details.php?id=grcLXX) on eBible.org: the Old Testament as traditionally read in the Orthodox Church.
- [St. Vladimir's Orthodox Theological Seminary](https://www.svots.edu/): seminary news, lectures, and publications (some free).
- [Ancient Faith Ministries](https://www.ancientfaith.com/): free [podcasts](https://www.ancientfaith.com/podcasts) and talks by Orthodox clergy and scholars.
- [The Confession of Dositheus](https://www.crivoice.org/creeddositheus.html) (CRI/Voice): the English text of the 1672 Synod of Jerusalem's confession.
- [*The Acts and Decrees of the Synod of Jerusalem* (1672)](https://archive.org/details/actsanddecreess00lucagoog) (Internet Archive): a scanned public-domain English translation (London, 1899, via a later reprint), with Greek, of the synod's acts.
- Fathers: CCEL's ANF/NPNF (above).

### Roman Catholic
- [Catechism of the Catholic Church](https://www.vatican.va/archive/ENG0015/_INDEX.HTM) (Vatican): the official text, citable by paragraph number.
- [New Advent](https://www.newadvent.org/): the older *Catholic Encyclopedia*, the [Church Fathers](https://www.newadvent.org/fathers/) in translation, and the *Summa Theologiae*.
- [USCCB Bible](https://bible.usccb.org/): the NABRE with its notes and the daily lectionary readings.

### Reformed / Presbyterian
- [Ligonier: Westminster Confession of Faith](https://www.ligonier.org/learn/articles/westminster-confession-faith): the confession's text online.
- [CCEL: *Creeds of Christendom*, vol. 3](https://www.ccel.org/ccel/schaff/creeds3): historic Protestant confessions in the original languages and English.
- [Monergism](https://www.monergism.com/): a large index of Reformed articles, sermons, and free e-books.
- [Reformed.org](https://reformed.org/): Reformed confessions, catechisms, and classic texts.
- [The Westminster Standard](https://thewestminsterstandard.org/): Reformed confessions and catechisms with proof texts, including the [Westminster Confession](https://thewestminsterstandard.org/the-westminster-confession/) and the [Canons of Dort](https://thewestminsterstandard.org/canons-of-dort/); the Larger Catechism, Belgic Confession, and Heidelberg Catechism are reached from the home page.
- [Christian Reformed Church: Confessions](https://www.crcna.org/welcome/beliefs/confessions): modern-English texts of the [Belgic Confession](https://www.crcna.org/welcome/beliefs/confessions/belgic-confession), [Heidelberg Catechism](https://www.crcna.org/welcome/beliefs/confessions/heidelberg-catechism), and [Canons of Dort](https://www.crcna.org/welcome/beliefs/confessions/canons-dort).
- [Westminster Seminary California: Belgic Confession](https://www.wscal.edu/belgic-confession): the Belgic Confession text.
- [A Puritan's Mind: Westminster Standards](https://www.apuritansmind.com/westminster-standards/): the Westminster Standards with related Puritan materials.
- [Confessional Collective: A. A. Hodge on the Westminster Confession](https://www.confessionalcollective.com/confessions/westminster-confession-of-faith/hodge/): Hodge's classic chapter-by-chapter commentary.
- Calvin's [*Institutes*](https://www.ccel.org/ccel/calvin/institutes) on CCEL.

### Lutheran
- [BookofConcord.org](https://bookofconcord.org/): the Lutheran Confessions online, with historical introductions.
- [Book of Concord (Concordia Publishing House)](https://bookofconcord.cph.org/): the text of *Concordia: The Lutheran Confessions*, a revision of the Triglotta translation.
- [LCMS: Doctrine](https://www.lcms.org/about/beliefs/doctrine): the Lutheran Church–Missouri Synod's doctrinal statements and theological documents. Other Lutheran bodies publish their own.

### Anglican
- [BCP Online](https://www.bcponline.org/): the 1979 (U.S. Episcopal) Book of Common Prayer.
- [Anglicans Online](https://www.anglicansonline.org/): a long-running directory of Anglican resources worldwide.
- [Project Canterbury](https://anglicanhistory.org/): historical Anglican texts and documents.

### Wesleyan / Methodist
- [Wesley Center Online](https://wesley.nnu.edu/) (Northwest Nazarene University): Wesley's sermons, notes, and works, and other holiness texts.
- [UMC: Articles of Religion](https://www.umc.org/en/content/articles-of-religion): the Methodist Articles of Religion.

### Baptist
- [Baptist Faith and Message 2000](https://bfm.sbc.net/): the Southern Baptist confession, with a [comparison chart](https://bfm.sbc.net/comparison-chart/) of the 1925, 1963, and 2000 versions side by side.
- [The 1689 Confession](https://www.the1689confession.com/): the Second London Baptist Confession, with study aids.
- [Reformed Baptist Seminary: 1689 Confession](https://www.rbs.org/2lbc): the full text by chapter and paragraph, with proof texts.
- [Founders Ministries: 1689 Confession](https://founders.org/library/1689-confession/): another full-text edition.
- [The Whosoever Study Bible](https://wsb.bible/): a free KJV study Bible with verse-by-verse commentary from older public-domain commentators, cross-references, and lexicon links; its doctrinal notes take a free-will (non-Calvinist) position, so label it as such.

### Pentecostal
- [Assemblies of God position papers](https://ag.org/Beliefs/Position-Papers): official AG statements on doctrine and practice (e.g. baptism in the Holy Spirit, divine healing).

## Confessions & catechisms quick reference

| Tradition | Document | Free online source |
|---|---|---|
| Eastern Orthodox | Confession of Dositheus (Synod of Jerusalem, 1672) | [CRI/Voice](https://www.crivoice.org/creeddositheus.html); [Acts and Decrees (Internet Archive)](https://archive.org/details/actsanddecreess00lucagoog) |
| Roman Catholic | Catechism of the Catholic Church | [Vatican](https://www.vatican.va/archive/ENG0015/_INDEX.HTM) |
| Reformed / Presbyterian | Westminster Confession of Faith | [The Westminster Standard](https://thewestminsterstandard.org/the-westminster-confession/); [Ligonier](https://www.ligonier.org/learn/articles/westminster-confession-faith); [A Puritan's Mind](https://www.apuritansmind.com/westminster-standards/) |
| Reformed / Presbyterian | Commentary on the WCF (A. A. Hodge) | [Confessional Collective](https://www.confessionalcollective.com/confessions/westminster-confession-of-faith/hodge/) |
| Reformed / Presbyterian | Westminster Larger Catechism | [The Westminster Standard](https://thewestminsterstandard.org/) (from the home page) |
| Reformed | Belgic Confession | [CRC](https://www.crcna.org/welcome/beliefs/confessions/belgic-confession); [WSC](https://www.wscal.edu/belgic-confession) |
| Reformed | Heidelberg Catechism | [CRC](https://www.crcna.org/welcome/beliefs/confessions/heidelberg-catechism) |
| Reformed | Canons of Dort | [CRC](https://www.crcna.org/welcome/beliefs/confessions/canons-dort); [The Westminster Standard](https://thewestminsterstandard.org/canons-of-dort/) |
| Reformed (historic, multiple) | Schaff, *Creeds of Christendom* vol. 3 | [CCEL](https://www.ccel.org/ccel/schaff/creeds3) |
| Lutheran | Book of Concord | [BookofConcord.org](https://bookofconcord.org/); [CPH](https://bookofconcord.cph.org/) |
| Anglican | Book of Common Prayer (1979, includes the Articles of Religion) | [BCP Online](https://www.bcponline.org/) |
| Wesleyan / Methodist | Articles of Religion | [UMC](https://www.umc.org/en/content/articles-of-religion) |
| Baptist | Second London Baptist Confession (1689) | [the1689confession.com](https://www.the1689confession.com/); [RBS](https://www.rbs.org/2lbc); [Founders](https://founders.org/library/1689-confession/) |
| Baptist | Baptist Faith and Message (1925/1963/2000) | [SBC](https://bfm.sbc.net/); [comparison chart](https://bfm.sbc.net/comparison-chart/) |
| Pentecostal | AG Statement of Fundamental Truths and position papers | [AG position papers](https://ag.org/Beliefs/Position-Papers) |

## 3. Using them with an AI assistant

If you already own e-books (Kindle, Kobo, Google Play Books, Apple Books, or library loans through Libby), your highlights can feed your study too; see [E-book libraries](starting-points.md#7-e-book-libraries-optional).

1. **Give it the URLs.** Paste the relevant sites (or this page) and say: "Use these sources for this study."
2. **Ask it to quote and link.** "Quote exactly, give the section or paragraph number, and link the page you quoted."
3. **Require verification.** Assistants can misquote or attribute a line to the wrong page. Open each link and check the quote before you keep it. If the assistant can't browse, paste the passage yourself and ask it to work only from what you pasted.
4. **Prefer primary texts.** Quote the confession, catechism, or Father directly rather than a summary site.
5. **Mind copyright.** Public-domain texts (KJV, ASV, WEB, Brenton, ANF/NPNF translations) can be quoted freely. Modern translations (NIV, ESV, NRSVue, NABRE, NET, and others) and modern commentaries are copyrighted, and publishers set limits on how much may be quoted. Quote short passages with attribution and link to the rest.

## Dropped during checking

Not included because they could not be confirmed as reachable and free on the check date: an online Aquinas edition (aquinas.cc), the DOAJ directory (blocked automated checks), a free Philokalia text, and the *Pneuma* journal (publisher site blocked; generally subscription-based). You may still find them useful; check them yourself.

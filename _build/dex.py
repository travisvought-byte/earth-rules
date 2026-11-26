"""The explorable index: life areas as regions, a consistent topic page, progress you can see.
Imported at the top of build.py so every page in a region gets its region strip and a "Next up" link."""
import re
import importlib

ENTRIES = []
for _m in ("dex_a", "dex_b", "dex_c", "dex_d"):
    ENTRIES += importlib.import_module(_m).ENTRIES
BY_SLUG = {e["slug"]: e for e in ENTRIES}

# id, name, icon, colour, one line, topics. A topic is a new entry slug, or (existing path, title, hint).
REGIONS = [
    ("survival", "Help now", "siren", "#a33a1a", "When things go wrong: who to call and what to do.", [
        ("help.html", "Get help", "Every hotline"), "homelessness", "leaving-abuse", "go-bag",
        ("help-groups.html", "Help groups", "AA, NA, gambling"), "immigration-basics"]),
    ("body", "Body", "heart", "#a8323e", "Keep yourself and the people around you alive and well.", [
        "first-aid", ("body-basics.html", "Sleep and food", "The basics that run everything"),
        ("checkups.html", "Checkups", "What to get and when"), "nutrition-labels", "mental-health-first-aid",
        "sex-ed-consent", ("coverage.html", "Health coverage", "Medicaid, Medicare, VA"), "aging-caregiving"]),
    ("home", "Home", "housing", "#7a5410", "A roof, food on the stove, and things that don't break on you.", [
        ("basics.html", "Basics", "Food, heat, phone, child care"), "cheap-cooking", "cleaning", "home-repairs",
        "home-emergencies", "renting-vs-buying", ("moving.html", "Moving", "The checklist"),
        ("rights/tenants.html", "Renter rights", "What your landlord owes you")]),
    ("people", "People", "peer_support", "#6b3fa0", "Friends, love, family, fights and loss.", [
        ("friends.html", "Making friends", "And keeping them"), ("how-people-work.html", "How people work", "Why we do what we do"),
        "apologize", ("disagree.html", "Disagree well", "Argue without wrecking it"), "dating-red-flags",
        "breakups-divorce", "parenting", "grief", ("when-someone-dies.html", "When someone dies", "What to do, step by step")]),
    ("money", "Money and papers", "dollar", "#1f6a3a", "Earn it, keep it, and handle the paperwork that comes with it.", [
        ("money.html", "Money", "Interest, credit, debt traps"), ("credit.html", "Credit", "Your score and report"),
        ("work.html", "Work", "Job programs that work"), ("taxes.html", "Taxes", "Filing, step by step"),
        "reading-a-bill", "insurance", "car", "identity-theft", ("papers.html", "Papers", "ID, birth certificate"),
        ("fine-print.html", "Fine print", "Read before you sign"), ("rides.html", "Rides", "Getting around"),
        ("business.html", "Start a business", "Value proposition first")]),
    ("brain", "Brain", "chat_q", "#1d5a72", "Think clearly, learn fast, and don't get played.", [
        "learn", "critical-thinking", ("manipulation.html", "Spot the trick", "Persuasion, propaganda, bias"),
        ("scams.html", "Scams", "How they work, how to report"), "ai-fakes",
        ("attention.html", "Attention traps", "Your feed is built to hook you"), "passwords-privacy"]),
    ("civic", "Civic", "ballot", "#2b3f8c", "How the rules get made, and how to push back on them.", [
        ("rights/index.html", "Your rights", "Federal and Ohio"), "voting", ("rights/police.html", "Talking to police", "Your rights in a stop"),
        "how-laws-are-made", "contact-representative", "jury-duty"]),
    ("time", "Your timeline", "calendar", "#5b4a1f", "What's expected of you at each age, and each month of the year.", [
        ("turning-18.html", "Turning 18", "What changes"), ("my-year/index.html", "My year", "Printable checklists by age"),
        ("stages.html", "Life stages", "Age by age"), ("whats-normal.html", "What's normal", "Real numbers on real life"),
        ("calendar.html", "Calendar", "What's due when")]),
]


def _norm(t, page_icons):
    if isinstance(t, str):
        e = BY_SLUG[t]
        return (t + ".html", e["title"], e["hint"], e["icon"])
    path, title, hint = t
    return (path, title, hint, page_icons.get(path, "book"))


def topics(rid, page_icons):
    for r in REGIONS:
        if r[0] == rid:
            return [_norm(t, page_icons) for t in r[5]]


def all_topics(page_icons):
    return [(r, _norm(t, page_icons)) for r in REGIONS for t in r[5]]


def region_icons():
    return {f"regions/{r[0]}.html": r[2] for r in REGIONS} | {e["slug"] + ".html": e["icon"] for e in ENTRIES} | {"explore.html": "navigation"}


def region_cards(ic, page_icons):
    return '<ul class="regions">' + "".join(
        f'<li><a class="regioncard rg-{r[0]}" href="{{P}}regions/{r[0]}.html"><span class="pic">{ic(r[2])}</span><span class="rc-name">{r[1]}</span>'
        f'<span class="rc-line">{r[4]}</span><span class="rc-count" data-slugs="{" ".join(t[0] for t in topics(r[0], page_icons))}">'
        f'<span class="dx-n">0</span> of {len(r[5])} learned</span></a></li>' for r in REGIONS) + "</ul>"


def wrap(path, body, ic, page_icons):
    """Adds the region strip on top and Next up at the bottom of any page that belongs to a region."""
    flat = all_topics(page_icons)
    for i, (r, t) in enumerate(flat):
        if t[0] != path:
            continue
        rid, rname, ricon = r[0], r[1], r[2]
        ts = topics(rid, page_icons)
        n = [x[0] for x in ts].index(path) + 1
        bar = (f'<div class="dexbar rg-{rid}"><a class="dx-region" href="{{P}}regions/{rid}.html">{ic(ricon)}<span>{rname}</span></a>'
               f'<span class="dx-count">Topic {n} of {len(ts)}</span>'
               f'<button type="button" class="learn" data-slug="{path}" aria-pressed="false" hidden>{ic("yes")}<span>Mark as learned</span></button></div>')
        if n < len(ts):
            nx = ts[n]
            label = "Next up"
        else:
            nr, nt = flat[(i + 1) % len(flat)]
            nx, label = nt, f"Next region: {nr[1]}"
        nxt = (f'<nav class="nextup rg-{rid}" aria-label="Next up"><a class="nx" href="{{P}}{nx[0]}">'
               f'<small>{label}</small><b>{nx[1]}</b>{ic("bigarrow")}</a>'
               f'<a class="all" href="{{P}}regions/{rid}.html">All {rname} topics</a></nav>')
        k = body.find('<section aria-labelledby="src-h"')
        body = bar + (body[:k] + nxt + body[k:] if k >= 0 else body + nxt)
        break
    return body


_EXT = re.compile(r'<a href="(https?://[^"]+)">(.*?)</a>', re.S)


def build(page, ic, ext, checklist, checked, tiles, URLS, page_icons):
    def links(h):
        return _EXT.sub(lambda m: ext(m.group(1), m.group(2)), h)

    def numtile(num, label):
        d = "".join(c for c in num if c.isdigit())
        kw = re.search(r"\b([A-Z]{3,})\b", label)
        if len(d) <= 6 and kw and "text" in label.lower():
            return (f"sms:{d}?body={kw.group(1)}", "text_msg", f"Text {kw.group(1)} to {num}", label, "tile-calm")
        return (f"tel:{d}", "phone", num, label, "tile-help" if d == "911" else "tile-calm")

    # ---------- topic pages ----------
    for e in ENTRIES:
        r = next(r for r in REGIONS if r[0] == e["region"])
        b = ('<p class="quickexit-wrap"><a class="quickexit" href="https://www.google.com/">Leave this site fast</a> '
             '<span>Takes you to Google and won\'t come back here with the Back button.</span></p>') if e["slug"] == "leaving-abuse" else ""
        b += f"""<section class="tensec rg-{r[0]}" aria-labelledby="q-h"><h2 id="q-h">In 10 seconds</h2>
<p><strong>What it is:</strong> {links(e["what"])}</p><p><strong>Why it matters:</strong> {links(e["why"])}</p></section>
<section aria-labelledby="st-h"><h2 id="st-h">{ic("yes")} Do this first</h2><ol class="steps">{"".join(f"<li>{links(s)}</li>" for s in e["steps"])}</ol></section>"""
        if e["numbers"]:
            b += f'<section aria-labelledby="nm-h"><h2 id="nm-h">{ic("phone")} Numbers to call</h2>{tiles([numtile(n, l) for n, l in e["numbers"]])}</section>'
        for k, (h, t) in enumerate(e["sections"]):
            b += f'<section aria-labelledby="x{k}"><h2 id="x{k}">{h}</h2>{links(t)}</section>'
        for key, hid, icn, head in (("everywhere", "w-h", "globe", "Everywhere"), ("us", "u-h", "map_pin", "In the United States"), ("ohio", "o-h", "map_pin", "In Ohio")):
            if e[key]:
                b += f'<section aria-labelledby="{hid}"><h2 id="{hid}">{ic(icn)} {head}</h2>{links(e[key])}</section>'
        b += checked([ext(u, t) for u, t in e["sources"]])
        URLS.append(page(e["slug"] + ".html", f'{e["title"]} | Earth Rules', f'{e["what"]} {e["why"]}'[:300],
                         f"EARTH RULES · {r[1].upper()}", e["title"] + ".", e["lead"], b))

    # ---------- region pages ----------
    def progress(slugs, label_id):
        return (f'<div class="dxprog" data-slugs="{" ".join(slugs)}"><p id="{label_id}"><strong>You\'ve learned '
                f'<span class="dx-n">0</span> of {len(slugs)}</strong> <span class="dx-hint">Tap "Mark as learned" on a topic to fill this up. It\'s saved on this device only.</span></p>'
                f'<progress max="{len(slugs)}" value="0" aria-labelledby="{label_id}"></progress></div>')

    def topic_tiles(ts, rid):
        return ('<ul class="tiles dextiles">' + "".join(
            f'<li><a class="tile rg-{rid}" href="{{P}}{p}" data-slug="{p}"><span class="pic">{ic(i)}</span><span class="tl">{t}</span>'
            f'<span class="th">{h}</span><span class="dx-done" hidden>{ic("yes")}<span>Learned</span></span></a></li>'
            for p, t, h, i in ts) + "</ul>")

    for k, r in enumerate(REGIONS):
        rid, rname, ricon, col, line, _ = r
        ts = topics(rid, page_icons)
        nr = REGIONS[(k + 1) % len(REGIONS)]
        b = f"""<section class="regionhead rg-{rid}" aria-labelledby="rp-h"><h2 id="rp-h">{len(ts)} topics in {rname}</h2>{progress([t[0] for t in ts], "rp-l")}</section>
<section aria-labelledby="rt-h"><h2 id="rt-h">{ic(ricon)} Pick one</h2>{topic_tiles(ts, rid)}</section>
<nav class="nextup rg-{nr[0]}" aria-label="Next region"><a class="nx" href="{nr[0]}.html"><small>Next region</small><b>{nr[1]}</b>{ic("bigarrow")}</a><a class="all" href="../explore.html">All regions</a></nav>"""
        URLS.append(page(f"regions/{rid}.html", f"{rname}: everything to know | Earth Rules", f"{line} {len(ts)} topics in plain language.",
                         "EARTH RULES · REGION", rname + ".", line, b))

    # ---------- explore: the whole map ----------
    every = [t[0] for _, t in all_topics(page_icons)]
    starter = ["first-aid.html", "help.html", "money.html", "scams.html", "go-bag.html", "voting.html"]
    st_tiles = [t for _, t in all_topics(page_icons) if t[0] in starter]
    b = f"""<section class="regionhead rg-all" aria-labelledby="ex-h"><h2 id="ex-h">Your progress</h2>{progress(every, "ex-l")}
<p class="dx-rank" aria-live="polite">Rank: <strong class="dx-rank-name">Just starting</strong></p></section>
<section aria-labelledby="ex-r"><h2 id="ex-r">{ic("map_pin")} {len(REGIONS)} regions, {len(every)} topics</h2>{region_cards(ic, page_icons)}</section>
<section aria-labelledby="ex-s"><h2 id="ex-s">{ic("yes")} Start here: the six everyone needs</h2>{topic_tiles([t for p in starter for t in st_tiles if t[0] == p], "all")}</section>
<section aria-labelledby="ex-p"><h2 id="ex-p">{ic("globe")} Where you live</h2><p>Most topics start with what's true everywhere, then the United States, then Ohio. <a href="places/index.html">Tap your part of the world</a> for local numbers and rights.</p></section>"""
    URLS.append(page("explore.html", "Explore everything | Earth Rules",
                     "The whole Earth Rules manual as a map you can explore: body, home, people, money, brain, civic, help and your timeline.",
                     "EARTH RULES · EXPLORE", "Explore everything.", f"{len(REGIONS)} regions. {len(every)} topics. Learn them in any order, and watch your progress fill up.", b))
    return REGIONS

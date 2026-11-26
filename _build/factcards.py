"""Country fact cards: one JSON file per country in _build/countries/, refreshed once a year.
Each figure carries the year it describes and the page it came from."""
import json
import os
import re

DIR = os.path.join(os.path.dirname(__file__), "countries")
CARDS = {}
for _f in sorted(os.listdir(DIR)):
    if _f.endswith(".json"):
        _d = json.load(open(os.path.join(DIR, _f), encoding="utf-8"))
        CARDS[_d["slug"]] = _d

FIELDS = [("population", "peer_support", "People"), ("capital", "map_pin", "Capital city"),
          ("languages", "language", "Languages"), ("money", "dollar", "Money"),
          ("government", "ballot", "Government"), ("religions", "book", "Beliefs"),
          ("life_expectancy", "heart", "How long people live")]

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]


def page_path(slug):
    return "places/us.html" if slug == "united-states" else f"places/{slug}.html"


def href(num):
    """tel: link for a local number. '119 ext. 8' dials 119, pauses, then 8. # is escaped."""
    m = re.match(r"(.*?)\s*ext\.?\s*(\d+)$", num)
    main, extn = (m.group(1), m.group(2)) if m else (num, "")
    d = "".join(c for c in main if c.isdigit() or c in "+*#").replace("#", "%23")
    return f"tel:{d}" + (f",{extn}" if extn else "")


def checked_on(c):
    y, m = c["checked"].split("-")
    return f"{MONTHS[int(m) - 1]} {y}"


def card(slug, ic, ext):
    """The at-a-glance card. Each row: picture, label, plain value, then the year and its source."""
    c = CARDS[slug]
    rows = ""
    for key, icon, label in FIELDS:
        f = c["facts"][key]
        if not f["value"]:
            continue
        url, src = f["src"]
        rows += (f'<li><span class="pic">{ic(icon)}</span><span class="fc-l">{label}</span>'
                 f'<span class="fc-v">{f["value"]}</span>'
                 f'<span class="fc-s">{f["year"]} · {ext(url, src)}</span></li>')
    return (f'<section aria-labelledby="fc-h" class="factcard-wrap"><h2 id="fc-h">{ic("chart")} {c["name"]} at a glance</h2>'
            f'<ul class="factcard">{rows}</ul>'
            f'<p class="fc-note">Each figure shows the year it describes and where it came from. We check these every year. Last checked {checked_on(c)}.</p></section>')


def sources(c, ext):
    seen, out = set(), []
    for f in c["facts"].values():
        url, label = f["src"]
        if url and url not in seen:
            seen.add(url)
            out.append(ext(url, label))
    for url, label in c["help_src"]:
        if url and url not in seen:
            seen.add(url)
            out.append(ext(url, label))
    return out


def by_continent(cont):
    return [c for c in CARDS.values() if c["continent"] == cont]


def tiles_for(cont, prefix=""):
    """Tiles for the continent page. The US keeps its full guide."""
    out = []
    for c in sorted(by_continent(cont), key=lambda c: c["name"]):
        if c["slug"] == "united-states":
            continue
        out.append((f'{prefix}{c["slug"]}.html', "map_pin", c["name"], "Fact card and numbers", ""))
    return out


def build(page, ic, ext, checked, tiles, URLS, continent_names):
    for slug, c in sorted(CARDS.items()):
        if slug == "united-states":
            continue  # its card goes on the existing US guide
        name = c["name"]
        em = tiles([(href(n), "siren", n, l, "tile-help") for n, l in c["emergency"]])
        if c["help"]:
            hl = tiles([(href(n), "crisis", n, l, "tile-calm") for n, l in c["help"]])
        else:
            hl = ""
        hl += (f'<p>{ext("https://findahelpline.com/", "Find A Helpline")} lists free, checked help lines here and in more than 150 other countries.</p>')
        note = f'<p class="lead2">{c["note"]}</p>' if c["note"] else ""
        cont = c["continent"]
        body = f"""{note}{card(slug, ic, ext)}
<section aria-labelledby="em-h"><h2 id="em-h">{ic("siren")} Emergency numbers</h2>{em}
<p>Save these in your phone when you arrive.</p></section>
<section aria-labelledby="hl-h"><h2 id="hl-h">{ic("crisis")} If you're struggling or not safe</h2>{hl}</section>
<section aria-labelledby="mr-h"><h2 id="mr-h">{ic("globe")} More about this part of the world</h2>{tiles([
            (f"{cont}.html", "globe", continent_names[cont], "Rights and numbers nearby", ""),
            ("../world-almanac.html", "chart", "World at a glance", "People, cities, languages", ""),
            ("world.html", "rights_legal", "True everywhere", "Rights every person has", "")])}</section>
{checked(sources(c, ext))}"""
        URLS.append(page(page_path(slug), f"{name}: facts, emergency numbers and help lines | Earth Rules",
                         f"{name} at a glance: people, capital, languages, money, government, beliefs and life expectancy, with the year and source for each, plus emergency and help numbers.",
                         f"EARTH RULES · {name.upper()}", f"{name}.", f"The basics on {name}, in plain words, with the numbers to call.", body))

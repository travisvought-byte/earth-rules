"""Find your belief: a neutral matching quiz, plus a fair profile of each belief system.
Data: one JSON file per belief in _build/beliefs/. Each says, from its own sources, how that tradition answers the 11 questions."""
import html
import json
import os

DIR = os.path.join(os.path.dirname(__file__), "beliefs")
BELIEFS = []
for _f in sorted(os.listdir(DIR)):
    if _f.endswith(".json"):
        BELIEFS.append(json.load(open(os.path.join(DIR, _f), encoding="utf-8")))
BY = {b["slug"]: b for b in BELIEFS}

FAMILY_ORDER = ["Christianity", "Judaism", "Islam", "Baha'i", "Sikhism", "Hinduism", "Buddhism", "Jainism",
                "Taoism", "Shinto", "Paganism", "Unitarian Universalism", "Non-religious"]

# key, icon, question, [(value, answer text)]
QUESTIONS = [
    ("god", "search", "What do you think about God?", [
        ("one", "There is one God who cares about people"),
        ("many", "There are many gods or divine beings"),
        ("everything", "The divine is in everything, or behind all things"),
        ("none", "There is no god"),
        ("unsure", "We can't really know, or it doesn't matter")]),
    ("jesus", "book", "Who was Jesus?", [
        ("god", "God, or the Son of God, who saves people"),
        ("prophet", "A prophet or messenger of God, but not God"),
        ("teacher", "One of many wise teachers"),
        ("notkey", "He isn't part of what I believe")]),
    ("afterlife", "clock", "What happens after we die?", [
        ("heaven", "We are judged, then heaven or hell"),
        ("rebirth", "We are born again and again until we are freed"),
        ("spirit", "Our spirit lives on with the ancestors"),
        ("none", "Nothing. This life is all there is"),
        ("unknown", "No one can know")]),
    ("guide", "document", "What do you trust most to know what's true?", [
        ("scripture", "A holy book"),
        ("tradition", "A holy book plus the teaching of wise leaders over time"),
        ("experience", "What I feel inside, my conscience"),
        ("reason", "Reason, evidence and science")]),
    ("path", "bigarrow", "What matters most for a good life, or after it?", [
        ("grace", "Faith, and God's forgiveness"),
        ("law", "Following God's law and doing what is right"),
        ("practice", "Meditation, discipline and seeing clearly"),
        ("ethics", "Just being a good person. Nothing needs saving")]),
    ("gather", "peer_support", "How much do you want a community?", [
        ("weekly", "I want to gather with others every week"),
        ("sometimes", "On holidays and big life events, and at home the rest"),
        ("alone", "Mostly on my own")]),
    ("leaders", "ballot", "Who should lead a faith community?", [
        ("hierarchy", "Trained clergy, with leaders above them like bishops"),
        ("local", "Each community chooses its own leaders"),
        ("none", "No clergy at all")]),
    ("rules", "sliders", "How many daily rules feel right to you?", [
        ("many", "Many: food, clothes, prayer times"),
        ("some", "A few set practices"),
        ("few", "Very few")]),
    ("prayer", "comfort", "How would you rather connect?", [
        ("pray", "Pray, talking to God"),
        ("meditate", "Meditate, or sit in quiet thought"),
        ("ritual", "Ceremonies and offerings"),
        ("none", "I don't need prayer or ritual")]),
    ("others", "globe", "What about other beliefs?", [
        ("one", "There is one true path"),
        ("many", "Many paths can lead to the truth"),
        ("nopath", "No spiritual path is needed")]),
    ("nature", "heart", "What is nature to you?", [
        ("created", "Made by God, and ours to care for"),
        ("sacred", "Sacred in itself. The seasons matter"),
        ("natural", "Nature. Science explains it")]),
]


def _esc(s):
    return html.escape(s, quote=False)


def profile_path(slug):
    return f"beliefs/{slug}.html"


def page_icons():
    d = {profile_path(b["slug"]): b["icon"] for b in BELIEFS}
    d.update({"beliefs/index.html": "book", "find-your-belief.html": "search"})
    return d


def build(page, ic, ext, checked, tiles, URLS):
    # ---------- the quiz ----------
    qhtml = ""
    for n, (key, icon, q, opts) in enumerate(QUESTIONS, 1):
        radios = "".join(
            f'<label class="bq-opt"><input type="radio" name="{key}" value="{v}"><span>{_esc(t)}</span></label>'
            for v, t in opts)
        radios += f'<label class="bq-opt bq-skip"><input type="radio" name="{key}" value="" checked><span>Skip, or not sure</span></label>'
        qhtml += (f'<fieldset class="bq"><legend><span class="pic">{ic(icon)}</span>'
                  f'<span class="bq-n">Question {n} of {len(QUESTIONS)}</span><span class="bq-q">{_esc(q)}</span></legend>{radios}</fieldset>')

    data = {b["slug"]: {"n": b["name"], "f": b["family"], "l": b["line"], "d": b["dims"]} for b in BELIEFS}
    data_js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")

    groups = ""
    for fam in FAMILY_ORDER + sorted({b["family"] for b in BELIEFS} - set(FAMILY_ORDER)):
        bs = [b for b in BELIEFS if b["family"] == fam]
        if bs:
            groups += f'<h3>{_esc(fam)}</h3>' + tiles([(f'{{P}}{profile_path(b["slug"])}', b["icon"], b["name"], "", "") for b in bs])

    quiz = f"""
<section aria-labelledby="hw-h" class="panel"><h2 id="hw-h">{ic("chat_q")} How this works</h2>
<ul><li>Answer what you really think, not what you were told to think. Skip anything you're not sure about.</li>
<li>You'll see which belief systems are closest to your answers, and how close.</li>
<li>Each one is described the way its own members describe it. None is ranked above another, and not believing is a full answer too.</li>
<li>Your answers stay on your device. Nothing is saved or sent.</li></ul></section>
<form id="bq-form" class="bqform" novalidate>
{qhtml}
<p><button type="submit" class="bq-go">{ic("search")}<span>Show my closest matches</span></button></p>
</form>
<section id="bq-results" aria-labelledby="bq-rh" aria-live="polite" hidden tabindex="-1"><h2 id="bq-rh">{ic("chart")} Your closest matches</h2>
<p class="bq-sum"></p><ol class="bq-list"></ol>
<p>A match means a tradition teaches what you said, not that you have to join it. Read about any of them, visit, ask questions, and take your time.</p></section>
<noscript><p>The quiz needs JavaScript. You can still read about every belief system below.</p></noscript>
<section aria-labelledby="all-h"><h2 id="all-h">{ic("book")} Every belief system in this guide</h2>{groups}</section>
<section aria-labelledby="hc-h"><h2 id="hc-h">{ic("shield")} A good community, of any kind</h2>
<p>A healthy group lets you ask questions, keep your friends and family, keep your own money, and leave when you want to. If a group, religious or not, pressures you on any of those, read <a href="{{P}}manipulation.html">Spot the trick</a>.</p>
<p>Your rights: in the United States you are free to believe anything or nothing, and to change your mind. See <a href="{{P}}religions.html">Religions of the world</a> for how the law protects that.</p></section>
<script type="application/json" id="bq-data">{data_js}</script>
<script src="{{P}}assets/belief-quiz.js" defer></script>"""
    srcs = []
    seen = set()
    for b in BELIEFS:
        for u, t in b["sources"][:1]:
            if u not in seen:
                seen.add(u)
                srcs.append(ext(u, t))
    quiz += checked(srcs)
    URLS.append(page("find-your-belief.html", "Find your belief: a fair quiz about faith and non-belief | Earth Rules",
                     "Answer 11 plain questions about God, death, truth and community and see which belief systems are closest to what you think. Fair to every faith, including none.",
                     "EARTH RULES · WORLD AND CULTURE", "Find your belief.",
                     "What do you believe? What makes sense to you? Answer 11 questions and see which traditions are closest.", quiz))

    # ---------- the list page ----------
    URLS.append(page("beliefs/index.html", "Belief systems, side by side | Earth Rules",
                     "Fair, plain profiles of 25 belief systems, from Catholic Christianity to atheism, each with a way to find that community near you.",
                     "EARTH RULES · BELIEFS", "Belief systems.", "Each one in its own words, with a way to find it near you.",
                     f'<p class="lead2"><a href="{{P}}find-your-belief.html">Take the quiz</a> to see which are closest to what you believe.</p>' + groups))

    # ---------- profiles ----------
    labels = {k: (q, dict(o)) for k, _, q, o in QUESTIONS}
    for b in BELIEFS:
        rows = ""
        for k, _, q, _o in QUESTIONS:
            w = b["dims"].get(k, {})
            main = [labels[k][1][v] for v, x in w.items() if x >= 1 and v in labels[k][1]]
            some = [labels[k][1][v] for v, x in w.items() if 0 < x < 1 and v in labels[k][1]]
            cell = _esc("; ".join(main)) + "."
            if some:
                cell += f' <span class="bq-some">Some also say: {_esc("; ".join(some))}.</span>'
            rows += f'<tr><th scope="row">{_esc(q)}</th><td>{cell}</td></tr>'
        fol = b["followers"]
        fol_html = ""
        if fol["value"]:
            fol_html = (f'<ul class="factcard"><li><span class="pic">{ic("peer_support")}</span><span class="fc-l">How many</span>'
                        f'<span class="fc-v">{_esc(fol["value"])}</span><span class="fc-s">{_esc(fol["year"])} · {ext(fol["src"][0], _esc(fol["src"][1]))}</span></li></ul>')
        if b["find"]:
            find = tiles([(u, "map_pin", _esc(t.split(" (")[0])[:60], "Opens their finder", "tile-calm") for u, t in b["find"]])
            find += "<p>These finders are run by the groups themselves or by free directories. Earth Rules doesn't check every listing.</p>"
        else:
            find = "<p>There's no single group or place for this. Many people find others who think the same way through friends, books or local meetups.</p>"
        body = f"""<p class="lead2">{_esc(b["line"])}</p>
<section aria-labelledby="ab-h"><h2 id="ab-h">{ic(b["icon"])} In their own words</h2>{b["summary"]}{fol_html}</section>
<section aria-labelledby="bl-h"><h2 id="bl-h">{ic("yes")} What they believe</h2><ul>{"".join(f"<li>{_esc(x)}</li>" for x in b["beliefs"])}</ul></section>
<section aria-labelledby="pr-h"><h2 id="pr-h">{ic("calendar")} What they do</h2><ul>{"".join(f"<li>{_esc(x)}</li>" for x in b["practices"])}</ul></section>
<section aria-labelledby="fd-h"><h2 id="fd-h">{ic("map_pin")} Find this community near you</h2>{find}</section>
<section aria-labelledby="qa-h"><h2 id="qa-h">{ic("chat_q")} How it answers the quiz</h2>
<table><caption>How {_esc(b["name"])} answers each question</caption><tr><th scope="col">Question</th><th scope="col">Answer</th></tr>{rows}</table></section>
<p><a href="{{P}}find-your-belief.html">Take the quiz</a> · <a href="index.html">All belief systems</a></p>
{checked([ext(u, _esc(t)) for u, t in b["sources"]])}"""
        URLS.append(page(profile_path(b["slug"]), f'{b["name"]}: what they believe and how to find them | Earth Rules',
                         b["line"][:300], f'EARTH RULES · {b["family"].upper()}', b["name"] + ".",
                         f'Part of the {b["family"]} family.' if b["family"] not in ("Non-religious", b["name"]) else "A fair, plain look.", body))

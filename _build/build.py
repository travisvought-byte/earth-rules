#!/usr/bin/env python3
"""Builds the Earth Rules static site. Run: python3 _build/build.py (from the site root)."""
import os, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://earthrules.org"
NAME = "Earth Rules"
CHECKED = "November 25, 2026"

NAV = [("index.html", "Home"), ("help.html", "Get help"), ("explore.html", "Explore"), ("rights/index.html", "Rights"),
       ("calendar.html", "Calendar"), ("places/index.html", "Places"), ("about.html", "About")]

# One big picture at the top of every page, so the page can be recognized without reading.
PAGE_ICONS = {
    "index.html": "globe", "help.html": "phone", "calendar.html": "calendar", "stages.html": "children",
    "whats-normal.html": "chart", "taxes.html": "document", "credit.html": "dollar", "moving.html": "housing",
    "friends.html": "heart", "checkups.html": "medical", "turning-18.html": "idcard", "about.html": "book",
    "privacy.html": "lock", "404.html": "search", "states/index.html": "map_pin", "states/ohio.html": "map_pin",
    "rights/index.html": "rights_legal", "rights/everyone.html": "peer_support", "rights/police.html": "shield",
    "rights/patients.html": "medical", "rights/tenants.html": "housing", "rights/workers.html": "work_school",
    "rights/consumers.html": "store", "rights/voters.html": "ballot", "rights/students.html": "school",
    "rights/veterans.html": "veterans", "rights/disability.html": "service_dog",
    "money.html": "dollar", "help-groups.html": "peer_support", "coverage.html": "medical", "papers.html": "idcard",
    "basics.html": "food", "work.html": "wrench", "rides.html": "transportation", "business.html": "store",
    "how-people-work.html": "globe", "places/index.html": "map_pin", "places/world.html": "globe", "places/us.html": "map_pin", "places/north-america.html": "globe", "places/south-america.html": "globe", "places/europe.html": "globe", "places/africa.html": "globe", "places/asia.html": "globe", "places/oceania.html": "globe",
    "manipulation.html": "megaphone", "scams.html": "siren", "attention.html": "device", "disagree.html": "chat_q",
    "fine-print.html": "search", "when-someone-dies.html": "comfort", "body-basics.html": "clock",
    "my-year/index.html": "calendar", "my-year/18-29.html": "calendar", "my-year/30-39.html": "calendar",
    "my-year/40-49.html": "calendar", "my-year/50-64.html": "calendar", "my-year/65.html": "calendar",
}

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dex
PAGE_ICONS.update(dex.region_icons())
import factcards as _fc
import beliefs
PAGE_ICONS.update(beliefs.page_icons())
PAGE_ICONS.update({_fc.page_path(s): "map_pin" for s in _fc.CARDS if s != "united-states"})

# Big tap-to-call buttons that sit at the top of every page.
HELPBAR = ('<nav class="helpbar" aria-label="Get help now"><span class="hb-t">Get help now</span>'
           '<a class="hb red" href="tel:911">{i911}<span><span class="sr">Call </span><b>911</b><small>Emergency</small></span></a>'
           '<a class="hb green" href="tel:988">{i988}<span><span class="sr">Call </span><b>988</b><small>Crisis, talk</small></span></a>'
           '<a class="hb blue" href="tel:211">{i211}<span><span class="sr">Call </span><b>211</b><small>Food, rent, bills</small></span></a>'
           '<a class="hb more" href="{P}help.html">{imore}<span><b>More</b><small>help</small></span></a></nav>')


def ic(name):
    return ('<svg class="ic" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">'
            f'<use href="{{P}}assets/icons.svg#{name}"/></svg>')


def ext(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}<span class="sr"> (opens in a new tab)</span></a>'


def page(path, title, desc, kicker, h1, lead, body, crumbs=None):
    depth = path.count("/")
    P = "../" * depth
    body = dex.wrap(path, body, ic, PAGE_ICONS)
    nav = "".join(f'<a href="{P}{h}">{t}</a>' for h, t in NAV)
    url = SITE + "/" + ("" if path == "index.html" else path)
    crumbs = crumbs or [(NAME, SITE + "/")] + ([] if path == "index.html" else [(h1, url)])
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList",
          "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]}
    gc = ('<script>window.goatcounter={path:function(){return "/earthrules.org"+location.pathname},'
          'referrer:function(){try{var u=new URL(document.referrer);return u.origin+u.pathname}catch(e){return ""}}};</script>'
          '<script data-goatcounter="https://vhg-guide.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>')
    pic = ic(PAGE_ICONS.get(path, "book"))
    helpbar = HELPBAR.format(i911=ic("siren"), i988=ic("crisis"), i211=ic("phone"), imore=ic("bigarrow"), P="{P}")
    out = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{NAME}"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{url}"><meta name="theme-color" content="#17423b">
<link rel="icon" href="{P}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{P}assets/site.css">
<style>.sr{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}</style>
<script type="application/ld+json">{json.dumps(ld)}</script>
<script>document.documentElement.classList.add("navjs")</script>
{gc}
</head>
<body><a class="skip" href="#main">Skip to main content</a>
{helpbar}
<header><nav id="site-nav" aria-label="Main"><a class="brand" href="{P}index.html">{NAME}</a><button type="button" class="navtoggle" aria-expanded="false" aria-controls="site-nav">Menu</button>{nav}</nav>
<small>{kicker}</small><div class="hero"><span class="pic">{pic}</span><h1>{h1}</h1></div><p>{lead}</p>
<button type="button" class="readaloud" hidden>{ic("speaker")}<span>Read aloud</span></button></header>
<main id="main">
{body}
<footer><p>{NAME} is a free guide to the things everyone is expected to know and do, created and maintained by <a href="https://travisvought.com/">Travis Vought</a>. <a href="mailto:travis@vethomeguard.org?subject=Earth%20Rules%20correction">Report a mistake</a> · <a href="{P}about.html">About and sources</a> · <a href="{P}privacy.html">Privacy</a></p>
<p>General information from official and published sources, with the date each was checked. It is not legal, tax, financial or medical advice. Rules change and differ by state, so confirm with the source before you act.</p></footer>
</main><script src="{P}assets/nav.js" defer></script><script src="{P}assets/read.js" defer></script><script src="{P}assets/dex.js" defer></script></body></html>
"""
    out = out.replace("{P}", P)
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(out)
    return url


def checked(src_list):
    items = "".join(f"<li>{s}</li>" for s in src_list)
    return f'<section aria-labelledby="src-h"><h2 id="src-h">Sources</h2><ul class="src">{items}</ul><p class="checked">Checked {CHECKED}.</p></section>'


def checklist(items):
    return '<ul class="check">' + "".join(f"<li>{ic(i)}<span>{t}</span></li>" for i, t in items) + "</ul>"


URLS = []

# ---------------- Home ----------------
# Picture tiles: one big symbol and one to three words each, so the site can be used without reading much.
TILE_GROUPS = [
    ("Help now", [("help.html", "phone", "Get help", "Call or text someone", "tile-help"),
                  ("basics.html", "food", "Food and bills", "Food, heat, phone", ""),
                  ("help-groups.html", "peer_support", "Help groups", "Drinking, drugs, betting", ""),
                  ("rides.html", "transportation", "Rides", "Bus, Medicaid, seniors", ""),
                  ("rights/police.html", "shield", "Police", "Stopped or arrested", "")]),
]


def tiles(items):
    return '<ul class="tiles">' + "".join(
        f'<li><a class="tile {c}" href="{h}"><span class="pic">{ic(i)}</span><span class="tl">{t}</span><span class="th">{d}</span></a></li>'
        for h, i, t, d, c in items) + "</ul>"


home = f"""
<p class="lead2">Tap a picture.</p>
{"".join(f'<section aria-labelledby="tg{n}"><h2 id="tg{n}">{g}</h2>{tiles(t)}</section>' for n, (g, t) in enumerate(TILE_GROUPS))}
<section aria-labelledby="rg-h"><h2 id="rg-h">Explore your life</h2><p class="lead2">{len(dex.REGIONS)} regions. Learn them in any order and watch your progress fill up. <a href="explore.html">See the whole map</a>.</p>{dex.region_cards(ic, PAGE_ICONS)}</section>
<section aria-labelledby="why-h" class="panel"><h2 id="why-h">Why this exists</h2><p>Nobody hands you a manual. School covers the quadratic formula and skips how to file a tax return, build credit, change your address or make a friend after college. Earth Rules puts those things in one place, in plain words, with a link to the official source for every rule and the date it was checked.</p><p>Where someone already explains a topic well, such as the IRS, USA.gov or Khan Academy, we link to them instead of rewriting it.</p></section>
"""
URLS.append(page("index.html", "Earth Rules: the user manual for being a person",
                 "A free, plain guide to what everyone is expected to know and do: taxes, credit, moving, checkups, making friends, what's normal, and a yearly calendar of what comes due.",
                 "EARTH RULES", "The user manual for being a person.",
                 "What you have to do, what's yours, and where to get help. Tap a picture to start.",
                 home))

# ---------------- Calendar ----------------
months = [
    ("January", ["Employers must send W-2s, and most 1099s are due to you, by January 31.", "Fourth-quarter estimated tax is due January 15 if you are self-employed.", "HealthCare.gov open enrollment ends January 15; enrolling after December 15 starts coverage February 1."]),
    ("February", ["Gather tax papers and choose how to file. Free options are on the taxes page.", "Check your credit reports; you can get them free every week."]),
    ("March", ["If you expect a refund, filing early gets it to you sooner.", "Spring clock change: test smoke and carbon monoxide alarms."]),
    ("April", ["Federal income tax returns are due April 15, and most states, including Ohio, use the same day.", "First-quarter estimated tax is due April 15.", "Last day to put money in an IRA for the year before.", "Need more time? An extension gives you until October 15 to file, but not to pay."]),
    ("May", ["Renew anything that expires in summer before travel season: passport, license, registration."]),
    ("June", ["Second-quarter estimated tax is due June 15."]),
    ("July", ["Mid-year check: is enough tax being withheld? The IRS withholding estimator will tell you."]),
    ("August", ["Back to school: immunization records and school forms.", "Many employers start benefits open enrollment in the fall; watch for the notice."]),
    ("September", ["Third-quarter estimated tax is due September 15."]),
    ("October", ["October 15 is the last day to file if you got an extension.", "Medicare open enrollment runs October 15 to December 7.", "Flu season starts; ask a pharmacist or doctor about a flu shot."]),
    ("November", ["HealthCare.gov open enrollment starts November 1.", "Fall clock change: test smoke and carbon monoxide alarms.", "Election day is the first Tuesday after the first Monday. Check your registration a month ahead."]),
    ("December", ["Pick a HealthCare.gov plan by December 15 for coverage that starts January 1.", "Medicare open enrollment ends December 7.", "Use or lose: check flexible spending account deadlines and any year-end benefits."]),
]
mhtml = '<div class="grid">' + "".join(
    f'<div class="month"><h3>{m}</h3><ul>' + "".join(f"<li>{x}</li>" for x in xs) + "</ul></div>" for m, xs in months) + "</div>"
every = checklist([
    ("medical", "A checkup and dental cleaning. See which screenings fit your age on the <a href=\"checkups.html\">checkups page</a>."),
    ("funding", "Look at all three credit reports. Weekly free reports are on the <a href=\"credit.html\">credit page</a>."),
    ("document", "Check who is named as beneficiary on retirement accounts and life insurance."),
    ("map_pin", "Renew your vehicle registration. In many states it follows your birthday; see <a href=\"states/index.html\">your state</a>."),
    ("shield", "Review your insurance: car, renters or home, and health."),
])
cal = f"""
<section aria-labelledby="m-h"><h2 id="m-h">Month by month</h2><p>Dates are for the federal government. When a date lands on a weekend or holiday it moves to the next business day.</p>{mhtml}</section>
<section aria-labelledby="e-h"><h2 id="e-h">Once a year, any time</h2>{every}</section>
{checked([ext("https://www.irs.gov/filing", "IRS: filing and due dates"), ext("https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes", "IRS: estimated taxes"), ext("https://www.healthcare.gov/", "HealthCare.gov"), ext("https://www.medicare.gov/", "Medicare.gov"), ext("https://www.irs.gov/individuals/tax-withholding-estimator", "IRS tax withholding estimator")])}
"""
URLS.append(page("calendar.html", "The yearly calendar: what comes due each month | Earth Rules",
                 "Month by month: tax deadlines, estimated taxes, health insurance and Medicare open enrollment, renewals and yearly checkups.",
                 "EARTH RULES · CALENDAR", "What comes due, month by month.",
                 "The deadlines nobody reminds you about, in the order they arrive.", cal))

# ---------------- Turning 18 ----------------
t18 = f"""
<section aria-labelledby="l-h"><h2 id="l-h">The checklist</h2>{checklist([
 ("ballot", "Register to vote. In many states, including Ohio, you can register before 18 if you will be 18 by the next general election. " + ext("https://vote.gov/", "Vote.gov") + " sends you to your state's form."),
 ("shield", "Selective Service: almost all men ages 18 through 25, citizens and immigrants, must be registered, within 30 days of turning 18. A 2025 law moves the government to automatic registration; until your registration shows on " + ext("https://www.sss.gov/", "SSS.gov") + ", register yourself. It takes a few minutes."),
 ("document", "Get a state ID or driver's license if you don't have one. Keep your birth certificate and Social Security card in a safe place, not your wallet."),
 ("funding", "Open a bank account in your own name, and start credit carefully. See the <a href=\"credit.html\">credit page</a>."),
 ("medical", "Health insurance: you can usually stay on a parent's plan until 26."),
 ("work_school", "First job: you'll fill out a W-4 for tax withholding and an I-9 to show you can work. Keep your pay stubs."),
 ("book", "Learn the basics free: " + ext("https://www.khanacademy.org/college-careers-more/financial-literacy", "Khan Academy financial literacy") + " and " + ext("https://edu.gcfglobal.org/en/", "GCFGlobal") + "."),
])}</section>
<section aria-labelledby="j-h"><h2 id="j-h">Jury duty</h2><p>Once you're on the voter or license rolls, you can be summoned for jury duty. A summons is a court order: answer it, and ask the court about a postponement if the date doesn't work.</p></section>
{checked([ext("https://vote.gov/", "Vote.gov"), ext("https://www.sss.gov/", "Selective Service System"), ext("https://www.healthcare.gov/young-adults/children-under-26/", "HealthCare.gov: coverage to age 26"), ext("https://www.militarytimes.com/news/your-military/2026/04/08/automatic-registration-for-us-military-draft-eligible-men-to-begin-in-december/", "Military Times: automatic Selective Service registration (April 2026)")])}
"""
URLS.append(page("turning-18.html", "Turning 18: the checklist | Earth Rules",
                 "What to do when you turn 18: register to vote, Selective Service, ID, bank account, health insurance and your first job papers.",
                 "EARTH RULES · TURNING 18", "Turning 18: the checklist.", "The handful of things that become yours to handle.", t18))

# ---------------- Taxes ----------------
tx = f"""
<section aria-labelledby="w-h"><h2 id="w-h">Do I have to file?</h2><p>It depends on your income, age and filing status, and the limits change every year. If tax was taken out of your pay, file anyway: it's the only way to get it back. The IRS has a free tool that answers the question: {ext("https://www.irs.gov/help/ita/do-i-need-to-file-a-tax-return", "Do I need to file?")}.</p></section>
<section aria-labelledby="f-h"><h2 id="f-h">Ways to file for free</h2>{checklist([
 ("device", ext("https://www.irs.gov/filing/irs-free-file-do-your-taxes-for-free", "IRS Free File") + ": brand-name software, free if your income is under the year's limit."),
 ("peer_support", ext("https://www.irs.gov/individuals/free-tax-return-preparation-for-qualifying-taxpayers", "VITA and TCE") + ": trained volunteers prepare your return for free if you have a low or moderate income, a disability, limited English, or are 60 or older (TCE)."),
 ("differs", "IRS Direct File is not being offered for the 2026 filing season."),
])}</section>
<section aria-labelledby="k-h"><h2 id="k-h">What to have ready</h2>{checklist([
 ("document", "W-2s from each job and any 1099s (side work, interest, unemployment)."),
 ("document", "Your Social Security number, and those of anyone you claim."),
 ("funding", "Bank account and routing numbers for a direct-deposit refund."),
 ("document", "Last year's return, if you have it."),
])}</section>
<section aria-labelledby="d-h"><h2 id="d-h">Deadlines and after</h2><p>Returns are due April 15. An extension moves the filing date to October 15 but not the payment, so pay what you expect to owe by April 15. Keep your return and papers for at least three years. Most states have their own income tax return too; see <a href="states/index.html">your state</a>.</p><p class="note">The IRS does not start contact with a text, email or social media message demanding payment. Those are scams.</p></section>
{checked([ext("https://www.irs.gov/filing", "IRS: filing"), ext("https://www.irs.gov/individuals/free-tax-return-preparation-for-qualifying-taxpayers", "IRS: VITA and TCE"), ext("https://www.law360.com/tax-authority/amp/articles/2407761", "Law360: Direct File not offered in 2026")])}
"""
URLS.append(page("taxes.html", "Filing your taxes, free | Earth Rules",
                 "Do you have to file, free ways to file, what to have ready, deadlines and extensions, and how long to keep your papers.",
                 "EARTH RULES · TAXES", "Filing your taxes, free.", "What you need, where to file without paying, and the dates that matter.", tx))

# ---------------- Credit ----------------
cr = f"""
<section aria-labelledby="c1"><h2 id="c1">What credit is</h2><p>A credit report is the record of how you've paid loans and cards. A credit score is a number built from that record, often on a 300 to 850 scale. Landlords, lenders, insurers and some employers look at one or both.</p></section>
<section aria-labelledby="c2"><h2 id="c2">Check yours, free</h2><p>The three national bureaus, Equifax, Experian and TransUnion, each keep a report on you. You can see all three free every week at {ext("https://www.annualcreditreport.com/", "AnnualCreditReport.com")}, the only official site for this. If something is wrong, dispute it with the bureau that shows it.</p></section>
<section aria-labelledby="c3"><h2 id="c3">Build it, and protect it</h2>{checklist([
 ("clock", "Pay every bill on time. Payment history weighs the most."),
 ("chart", "Keep card balances low compared with your limits."),
 ("clock", "Keep your oldest account open; age of credit helps."),
 ("lock", "Freeze your credit at each bureau if you aren't applying for anything. It's free and you can lift it any time."),
])}</section>
<section aria-labelledby="c4"><h2 id="c4">Learn more</h2><p>{ext("https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/", "The CFPB's credit reports and scores guide")} and {ext("https://www.khanacademy.org/college-careers-more/financial-literacy", "Khan Academy's free financial literacy course")} go deeper.</p></section>
{checked([ext("https://www.annualcreditreport.com/", "AnnualCreditReport.com"), ext("https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/", "Consumer Financial Protection Bureau")])}
"""
URLS.append(page("credit.html", "Credit basics: check, build and protect your credit | Earth Rules",
                 "What credit reports and scores are, how to see yours free every week, how to build credit and how to freeze it.",
                 "EARTH RULES · CREDIT", "Credit, in plain words.", "Check it, build it and lock it, for free.", cr))

# ---------------- Moving ----------------
mv = f"""
<section aria-labelledby="m1"><h2 id="m1">Before you move</h2>{checklist([
 ("send", "Forward your mail with the " + ext("https://www.usps.com/manage/forward.htm", "Postal Service change of address") + "."),
 ("shield", "Renters insurance for the new place; landlords often require it."),
 ("document", "Read the lease before you sign: rent, deposit, who fixes what, how to end it."),
 ("camera", "Photograph the old and new place on move-out and move-in day to protect your deposit."),
])}</section>
<section aria-labelledby="m2"><h2 id="m2">After you move</h2>{checklist([
 ("map_pin", "Update your driver's license and vehicle registration. Deadlines are short: Ohio gives you 10 days for an address change and new residents 30 days to get an Ohio license. See <a href=\"states/index.html\">your state</a>."),
 ("ballot", "Update your voter registration at " + ext("https://vote.gov/", "Vote.gov") + "."),
 ("document", "Tell the IRS with Form 8822 if you won't file a return soon, and update banks, employer, insurance and any benefits."),
 ("medical", "Moving can open a special enrollment period for health coverage at " + ext("https://www.healthcare.gov/", "HealthCare.gov") + "."),
])}</section>
{checked([ext("https://www.usps.com/manage/forward.htm", "USPS change of address"), ext("https://codes.ohio.gov/ohio-revised-code/section-4507.09", "Ohio Revised Code 4507.09"), ext("https://www.irs.gov/forms-pubs/about-form-8822", "IRS Form 8822")])}
"""
URLS.append(page("moving.html", "Moving checklist: before and after | Earth Rules",
                 "Everything to do when you move: forward mail, update your license, registration and voter record, and protect your deposit.",
                 "EARTH RULES · MOVING", "Moving: the checklist.", "The address changes people forget, and the deadlines that come with them.", mv))

# ---------------- Friends ----------------
fr = f"""
<section aria-labelledby="f1"><h2 id="f1">It takes time, and that's normal</h2><div class="grid">
<div class="stat"><span class="n">About 50 hours</span>together to go from acquaintance to casual friend.</div>
<div class="stat"><span class="n">About 90 hours</span>to become friends.</div>
<div class="stat"><span class="n">200+ hours</span>to become close friends.</div></div>
<p class="src">From a 2018 University of Kansas study of adults who had recently moved and of college freshmen. Time spent hanging out counted more than time spent working side by side.</p></section>
<section aria-labelledby="f2"><h2 id="f2">What works</h2>{checklist([
 ("clock", "Go to the same thing every week: a class, a league, a congregation, a volunteer shift. Seeing the same faces is how the hours add up."),
 ("chat_q", "Be the one who asks. Most people are waiting to be invited, and people tend to underestimate how much others enjoy talking with them."),
 ("send", "Follow up within a few days. \"That was fun, want to do it again Thursday?\" is enough."),
 ("peer_support", "Keep the friends you have. A short check-in every few weeks keeps a friendship from fading."),
 ("yes", "Expect some invitations to go nowhere. That's the average, not a verdict on you."),
])}</section>
<section aria-labelledby="f0"><h2 id="f0">Why it's harder after school</h2><p>School and early jobs hand you the same people every day. Adult life doesn't. People move, work long hours, raise kids and stay home with their phones. The friendships that used to happen by accident now take a plan.</p></section>
<section aria-labelledby="f3"><h2 id="f3">If it's become loneliness</h2><p>You're far from alone: in 2023 the US Surgeon General reported that about half of US adults say they've felt lonely, and that loneliness harms health about as much as smoking. Start small: one regular thing with the same people. Local groups and activities are listed through <a href="tel:211">211</a>. If it has become hard to get through the day, call or text <a href="tel:988">988</a>, any time.</p></section>
{checked([ext("https://news.ku.edu/2018/03/06/study-reveals-number-hours-it-takes-make-friend", "University of Kansas: hours it takes to make a friend (Hall, 2018)"), ext("https://www.hhs.gov/sites/default/files/surgeon-general-social-connection-advisory.pdf", "US Surgeon General: our epidemic of loneliness and isolation (2023)"), ext("https://988lifeline.org/", "988 Suicide and Crisis Lifeline"), ext("https://www.211.org/", "211")])}
"""
URLS.append(page("friends.html", "How to make friends as an adult | Earth Rules",
                 "What research says it takes to make a friend as an adult, and the habits that work: showing up regularly, inviting, following up.",
                 "EARTH RULES · PEOPLE", "Making friends as an adult.", "It's a skill, it takes hours, and almost everyone finds it harder after school.", fr))

# ---------------- What's normal ----------------
wn = f"""
<section aria-labelledby="n1"><h2 id="n1">The numbers</h2><div class="grid">
<div class="stat"><span class="n">$87,460</span>Median U.S. household income in 2025. Half of households made more, half less. <span class="src">Census Bureau, September 2026</span></div>
<div class="stat"><span class="n">40</span>Median age of a first-time home buyer, a record high. In 1981 it was 29. <span class="src">National Association of Realtors, 2026</span></div>
<div class="stat"><span class="n">22%</span>Share of home buyers who were buying their first home. <span class="src">National Association of Realtors, 2026</span></div>
<div class="stat"><span class="n">7 or more hours</span>Recommended sleep a night for adults. <span class="src">CDC</span></div>
</div></section>
<section aria-labelledby="n2"><h2 id="n2">How to read an average</h2><p>A median is the middle: half above, half below. It varies a lot by place, age and household size, so a number far from it is not a failure. Income in your state and county can be very different from the national figure; Census publishes it for every county.</p></section>
{checked([ext("https://www.census.gov/library/publications/2026/demo/p60-289.html", "Census Bureau: Income in the United States, 2025"), ext("https://www.nar.realtor/newsroom/first-time-home-buyer-share-inches-up-to-22-median-age-remains-at-record-high-of-40", "NAR: 2026 Profile of Home Buyers and Sellers"), ext("https://www.cdc.gov/sleep/", "CDC: sleep")])}
"""
URLS.append(page("whats-normal.html", "What's normal: averages for income, home buying and more | Earth Rules",
                 "The real averages: median household income, the age people buy a first home, recommended sleep, and how to read an average.",
                 "EARTH RULES · WHAT'S NORMAL", "What's normal, by the numbers.", "Averages from official sources, so you can see where you stand without guessing.", wn))

# ---------------- Checkups ----------------
ck_rows = [("Blood pressure", "Adults 18 and older"), ("Depression", "Adults"), ("Anxiety", "Adults under 65"),
           ("Hepatitis C", "Once, ages 18 to 79"), ("HIV", "Ages 15 to 65"),
           ("Cervical cancer", "Ages 21 to 65, on a schedule set with your clinician"),
           ("Prediabetes and type 2 diabetes", "Ages 35 to 70 who are overweight"),
           ("Breast cancer (mammogram)", "Every 2 years, ages 40 to 74"), ("Colorectal cancer", "Ages 45 to 75"),
           ("Lung cancer", "Ages 50 to 80 with a heavy smoking history who smoke now or quit within 15 years")]
table = '<table><caption>Common screenings recommended by the U.S. Preventive Services Task Force</caption><thead><tr><th scope="col">Screening</th><th scope="col">Who</th></tr></thead><tbody>' + "".join(
    f"<tr><th scope=\"row\">{a}</th><td>{b}</td></tr>" for a, b in ck_rows) + "</tbody></table>"
ckp = f"""
<section aria-labelledby="k1"><h2 id="k1">Screenings by age</h2>{table}<p class="src">These are general recommendations for people without symptoms. Your clinician may advise something different based on your history.</p></section>
<section aria-labelledby="k2"><h2 id="k2">Every year</h2>{checklist([
 ("medical", "A checkup with a primary care clinician, and a dental cleaning."),
 ("medical", "Ask which vaccines you're due for; CDC posts the adult schedule and pharmacies can give most of them."),
])}</section>
<section aria-labelledby="k3"><h2 id="k3">Reading about a condition</h2><p>{ext("https://medlineplus.gov/", "MedlinePlus")}, from the National Library of Medicine, explains conditions, tests and medicines in plain language. It's a place to learn, not a diagnosis. Bring your questions to a doctor, nurse or pharmacist.</p></section>
{checked([ext("https://www.uspreventiveservicestaskforce.org/uspstf/recommendation-topics/uspstf-a-and-b-recommendations", "USPSTF A and B recommendations"), ext("https://medlineplus.gov/", "MedlinePlus"), ext("https://www.cdc.gov/vaccines/", "CDC vaccines")])}
"""
URLS.append(page("checkups.html", "Checkups and screenings by age | Earth Rules",
                 "Which health screenings are recommended at which age, what to do every year, and where to read about a condition in plain language.",
                 "EARTH RULES · BODY AND MIND", "Checkups and screenings by age.", "General guidance from the U.S. Preventive Services Task Force. Your own clinician has the final word.", ckp))

# ---------------- Help ----------------
HELP_BIG = [
    ("tel:911", "siren", "Call 911", "Danger, fire, someone hurt", "tile-help"),
    ("tel:988", "crisis", "Call 988", "Crisis, sad, want to die. Veterans press 1.", "tile-calm"),
    ("sms:988", "text_msg", "Text 988", "Same help, by text", "tile-calm"),
    ("tel:211", "phone", "Call 211", "Food, rent, bills, rides", "tile-blue"),
]
hp = f"""
<section aria-labelledby="h1x"><h2 id="h1x">Call or text now</h2><p>Free. Any time, day or night.</p>
<ul class="tiles big">{"".join(f'<li><a class="tile {c}" href="{h}"><span class="pic">{ic(i)}</span><span class="tl">{t}</span><span class="th">{d}</span></a></li>' for h, i, t, d, c in HELP_BIG)}</ul></section>
<section aria-labelledby="h2x"><h2 id="h2x">More help</h2>
<ul class="tiles">
<li><a class="tile" href="https://www.211.org/" target="_blank" rel="noopener"><span class="pic">{ic("food")}</span><span class="tl">Food and rent</span><span class="th">211.org</span><span class="sr"> (opens in a new tab)</span></a></li>
<li><a class="tile" href="https://www.lsc.gov/about-lsc/what-legal-aid/get-legal-help" target="_blank" rel="noopener"><span class="pic">{ic("rights_legal")}</span><span class="tl">Free lawyer</span><span class="th">Legal aid near you</span><span class="sr"> (opens in a new tab)</span></a></li>
<li><a class="tile" href="https://www.consumerfinance.gov/" target="_blank" rel="noopener"><span class="pic">{ic("dollar")}</span><span class="tl">Money trouble</span><span class="th">Debt, bills, scams</span><span class="sr"> (opens in a new tab)</span></a></li>
<li><a class="tile" href="https://www.usa.gov/benefits" target="_blank" rel="noopener"><span class="pic">{ic("benefits")}</span><span class="tl">Benefits</span><span class="th">Government help</span><span class="sr"> (opens in a new tab)</span></a></li>
</ul></section>
<section aria-labelledby="h3x"><h2 id="h3x">What each one does</h2>{checklist([
 ("siren", "<strong>911</strong> sends police, fire or an ambulance. Use it when someone is in danger right now."),
 ("crisis", "<strong>988</strong> is the Suicide and Crisis Lifeline. Call or text when things feel too heavy, for you or someone else. Veterans, press 1."),
 ("phone", "<strong>211</strong> connects you to local help: food, rent, utilities, rides and programs near you. You can also search at " + ext("https://www.211.org/", "211.org") + "."),
 ("rights_legal", ext("https://www.lsc.gov/about-lsc/what-legal-aid/get-legal-help", "Legal Services Corporation") + " finds free civil legal aid near you."),
 ("dollar", ext("https://www.consumerfinance.gov/", "Consumer Financial Protection Bureau") + " helps with debt collectors, bank problems and complaints."),
 ("benefits", ext("https://www.usa.gov/benefits", "USA.gov benefits") + " is the government's benefit finder by life event, such as a death, retirement or disability."),
])}</section>
{checked([ext("https://988lifeline.org/", "988 Lifeline"), ext("https://www.211.org/", "211"), ext("https://www.usa.gov/benefits", "USA.gov"), ext("https://www.lsc.gov/", "Legal Services Corporation")])}
"""
URLS.append(page("help.html", "Get help now: crisis lines, local help and legal aid | Earth Rules",
                 "Where to turn: 911, 988, 211, the USA.gov benefit finder, free legal aid and money help.",
                 "EARTH RULES · GET HELP", "Get help now.", "Tap a picture to call. It's free.", hp))

# ---------------- Life stages ----------------
st = [("school", "Turning 18", "Vote, Selective Service, ID, first bank account, first job papers.", "turning-18.html"),
      ("work_school", "Your twenties", "Taxes, credit, renting, your own health insurance by 26, retirement savings at your first job.", "taxes.html"),
      ("children", "Starting a family", "Birth certificate and Social Security number for the baby, insurance changes within the special enrollment window, a will.", "help.html"),
      ("housing", "Buying a home", "The median first-time buyer is 40. Credit, down payment and what normal looks like.", "whats-normal.html"),
      ("medical", "Mid-life", "Screenings start: colorectal at 45, mammograms from 40, diabetes from 35 if overweight.", "checkups.html"),
      ("benefits", "Retirement", "Medicare at 65, Social Security timing, and USA.gov's retirement benefit finder.", "help.html")]
sth = '<div class="grid">' + "".join(
    f'<a class="card" href="{h}"><div class="iconrow">{ic(i)}<h3>{t}</h3></div><p>{d}</p></a>' for i, t, d, h in st) + "</div>"
URLS.append(page("stages.html", "Life stages: what to do and when | Earth Rules",
                 "What to expect and what to do at each stage of adult life, from turning 18 to retirement.",
                 "EARTH RULES · LIFE STAGES", "Life stages.", "What changes at each stage, and what becomes yours to handle.",
                 f'<section aria-labelledby="s1"><h2 id="s1">Pick a stage</h2>{sth}<p>More guides for each stage are on the way.</p></section>'))

# ---------------- States ----------------
URLS.append(page("states/index.html", "Rules by state | Earth Rules",
                 "The rules that change by state: licenses, registration, state taxes and voting. Ohio first, more states coming.",
                 "EARTH RULES · STATES", "Rules by state.", "Licenses, registration, state taxes and voting change from state to state.",
                 '<section aria-labelledby="sx"><h2 id="sx">Choose a state</h2><div class="grid"><a class="card" href="ohio.html"><div class="iconrow">' + ic("map_pin") + '<h3>Ohio</h3></div><p>License, registration, state tax, voting and where to get help.</p></a></div><p>More states are being added one at a time, each checked against the state\'s own pages.</p></section>'))

oh = f"""
<section aria-labelledby="o1"><h2 id="o1">Driving and your car</h2>{checklist([
 ("map_pin", "Moved within Ohio? Tell the BMV within 10 days (Ohio Revised Code 4507.09). You can do it online at " + ext("https://bmv.ohio.gov/", "the Ohio BMV") + "."),
 ("map_pin", "New to Ohio? Get an Ohio driver's license within 30 days of becoming a resident."),
 ("clock", "License renewal: choose a 4-year or 8-year license. People 65 and older get 4 years."),
])}</section>
<section aria-labelledby="o2"><h2 id="o2">Taxes</h2><p>Ohio has a state income tax, due the same day as the federal return. Many cities and school districts add their own. Free filing: {ext("https://tax.ohio.gov/", "Ohio Department of Taxation")}.</p></section>
<section aria-labelledby="o3"><h2 id="o3">Voting</h2><p>Register at least 30 days before an election, at {ext("https://www.ohiosos.gov/", "the Ohio Secretary of State")}. You can register at 17 if you will be 18 by the general election.</p></section>
<section aria-labelledby="o5"><h2 id="o5">Your rights in Ohio</h2><p>Every page in <a href="../rights/index.html">Your rights</a> lists what Ohio adds to federal law: as a renter, worker, patient, voter, veteran and more.</p></section>
<section aria-labelledby="o4"><h2 id="o4">Help</h2>{checklist([
 ("benefits", ext("https://benefits.ohio.gov/", "Ohio Benefits") + ": food, health coverage and cash assistance applications."),
 ("rights_legal", ext("https://www.ohiolegalhelp.org/", "Ohio Legal Help") + ": free legal information and help finding a lawyer."),
 ("phone", "Dial <a href=\"tel:211\">211</a> for local help anywhere in Ohio."),
])}</section>
{checked([ext("https://codes.ohio.gov/ohio-revised-code/section-4507.09", "Ohio Revised Code 4507.09"), ext("https://bmv.ohio.gov/", "Ohio BMV"), ext("https://tax.ohio.gov/", "Ohio Department of Taxation"), ext("https://www.ohiosos.gov/", "Ohio Secretary of State")])}
"""
URLS.append(page("states/ohio.html", "Ohio: licenses, taxes, voting and help | Earth Rules",
                 "Ohio's rules in one place: BMV address changes, new resident license deadline, renewal, state income tax, voter registration and help.",
                 "EARTH RULES · OHIO", "Ohio.", "The Ohio rules most people run into, with the official link for each.", oh))

# ---------------- About / privacy / 404 ----------------
ab = f"""
<section aria-labelledby="a1"><h2 id="a1">What this is</h2><p>Earth Rules is a free guide to the things everyone is expected to know and do as an adult: the yearly deadlines, the one-time steps, the people skills and the averages. It starts with the United States and Ohio and will add every state, then other countries.</p></section>
<section aria-labelledby="a2"><h2 id="a2">Who runs it</h2><p>Earth Rules is created and maintained by Travis Vought. There is no paid placement. Organizations we link to are not partners unless this page says so.</p></section>
<section aria-labelledby="a3"><h2 id="a3">Where the information comes from</h2><p>Every page lists its sources, mostly official government pages, and the date they were checked. Health pages give general information from public health agencies and point you to a clinician. If something is wrong, email <a href="mailto:travis@vethomeguard.org?subject=Earth%20Rules%20correction">travis@vethomeguard.org</a>.</p></section>
<section aria-labelledby="a4"><h2 id="a4">Accessibility</h2><p>The site is built to WCAG 2.1 AA: it works with a keyboard alone, has a skip link, labels every icon with text beside it, and keeps color contrast high. If anything is hard to use, email us and we will fix it.</p></section>
"""
URLS.append(page("about.html", "About Earth Rules: who runs it and where the facts come from | Earth Rules",
                 "Who runs Earth Rules, where its information comes from, and how it is made accessible.",
                 "EARTH RULES · ABOUT", "About Earth Rules.", "Who runs it, where the facts come from, and how to report a mistake.", ab))
pv = """<section aria-labelledby="p1"><h2 id="p1">Privacy</h2><ul><li>There is no sign-in, and nothing you choose on this site is saved or sent anywhere.</li><li>A visit counter, GoatCounter, counts page views without cookies. It records the page, the site you came from, your browser and screen size, and an approximate country. It does not store your IP address.</li><li>The site is hosted on GitHub Pages, which may keep server logs, including IP addresses, for security.</li><li>Links to other sites go to organizations with their own privacy practices.</li></ul></section>"""
URLS.append(page("privacy.html", "Privacy | Earth Rules", "What Earth Rules collects: a cookie-free visit counter and nothing else.",
                 "EARTH RULES · PRIVACY", "Privacy.", "What this site collects, which is very little.", pv))
page("404.html", "Page not found | Earth Rules", "That page isn't here.", "EARTH RULES", "That page isn't here.",
     "It may have moved.", '<section><p><a href="/">Go to the home page</a>.</p></section>')

# ---------------- Your rights ----------------
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rights
rights.build(page, ic, ext, checklist, checked, URLS)
import life
life.build(page, ic, ext, checklist, checked, tiles, URLS)
import mind
mind.build(page, ic, ext, checklist, checked, tiles, URLS)
dex.build(page, ic, ext, checklist, checked, tiles, URLS, PAGE_ICONS)
import places
places.build(page, ic, ext, checklist, checked, tiles, URLS)
import factcards
factcards.build(page, ic, ext, checked, tiles, URLS, {c[0]: c[1] for c in places.CONTINENTS})
beliefs.build(page, ic, ext, checked, tiles, URLS)

# ---------------- sitemap, robots, CNAME, favicon ----------------
with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
            "".join(f"<url><loc>{u}</loc></url>\n" for u in URLS) + "</urlset>\n")
with open(os.path.join(ROOT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
with open(os.path.join(ROOT, "CNAME"), "w") as f:
    f.write("earthrules.org\n")
with open(os.path.join(ROOT, "favicon.svg"), "w") as f:
    f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="#17423b"/><path d="M14 26c8-2 10 6 18 4s8-10 16-8M12 40c10-3 14 5 22 2s10-8 18-6" stroke="#f0d79a" stroke-width="4" fill="none" stroke-linecap="round"/></svg>')
print(len(URLS), "pages")

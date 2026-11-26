"""Places: the tap-your-continent world map and one starter page per continent. Imported by build.py."""

CONTINENTS = [
    # slug, name, hint, label x, label y, shape paths (simplified, not to scale)
    ("north-america", "North America", "US, Canada, Mexico", 205, 150,
     ["M70,85 L190,55 L300,48 L355,72 L330,110 L300,132 L292,172 L252,202 L232,240 L252,268 L228,280 L196,252 L165,216 L130,172 L95,140 Z",
      "M345,28 L425,22 L412,72 L372,92 Z"]),
    ("south-america", "South America", "Brazil, Argentina and more", 305, 360,
     ["M258,288 L312,280 L365,312 L350,362 L314,410 L288,462 L270,456 L276,400 L254,342 Z"]),
    ("europe", "Europe", "112 and 116 123", 515, 108,
     ["M448,92 L500,58 L565,62 L585,100 L562,142 L520,152 L470,146 L452,122 Z"]),
    ("africa", "Africa", "South Africa, Nigeria and more", 530, 255,
     ["M452,176 L532,164 L592,186 L612,232 L582,302 L556,362 L520,366 L504,302 L474,256 L448,216 Z"]),
    ("asia", "Asia", "India, China, Japan and more", 755, 135,
     ["M592,58 L700,38 L850,48 L935,90 L902,140 L862,172 L822,222 L760,242 L722,212 L682,232 L642,202 L604,176 L588,140 L600,100 Z"]),
    ("oceania", "Oceania", "Australia, New Zealand", 845, 348,
     ["M790,320 L860,300 L902,330 L892,382 L830,392 L790,366 Z",
      "M928,386 L946,380 L942,412 L924,416 Z",
      "M820,276 L872,270 L862,292 Z"]),
]


def build(page, ic, ext, checklist, checked, tiles, URLS):
    def tel(num, label=None):
        digits = "".join(c for c in num if c.isdigit())
        return f'<a href="tel:{digits}">{label or num}</a>'

    # ---------- the map ----------
    shapes = ""
    for slug, name, hint, lx, ly, paths in CONTINENTS:
        d = "".join(f'<path d="{p}"/>' for p in paths)
        shapes += (f'<a href="{slug}.html" class="wm-{slug}" tabindex="-1">{d}'
                   f'<text x="{lx}" y="{ly}" text-anchor="middle">{name}</text></a>')
    worldmap = (f'<figure class="worldmap"><svg viewBox="0 0 1000 480" aria-hidden="true" focusable="false">'
                f'<rect class="sea" x="0" y="0" width="1000" height="480" rx="18"/>{shapes}</svg>'
                f'<figcaption>Tap your part of the world. The same places are listed below.</figcaption></figure>')
    cont_tiles = tiles([(f"{slug}.html", "globe", name, hint, "") for slug, name, hint, *_ in CONTINENTS])

    pl = f"""
<section aria-labelledby="pl0"><h2 id="pl0">{ic("globe")} Tap where you are</h2>{worldmap}{cont_tiles}</section>
<section aria-labelledby="pl1"><h2 id="pl1">{ic("map_pin")} Or go straight to</h2>{tiles([
 ("world.html", "globe", "Anywhere", "What's true everywhere", ""),
 ("us.html", "map_pin", "United States", "Federal rules", ""),
 ("../states/ohio.html", "map_pin", "Ohio", "State rules", ""),
])}</section>
<section aria-labelledby="pl2"><h2 id="pl2">How this guide is built</h2>
<p>Every section starts with what's true everywhere. Then it narrows to your part of the world, your country, and your state or province. The United States and Ohio come first. More countries are added one at a time, each checked against that place's own official pages.</p></section>
"""
    URLS.append(page("places/index.html", "Where you are: pick your part of the world | Earth Rules",
                     "Tap your continent on the map. Earth Rules starts with what's true everywhere, then your part of the world, your country and your state.",
                     "EARTH RULES · PLACES", "Where are you?", "Tap your part of the world. Each one has its emergency numbers, help lines and rights.", pl))

    # ---------- shared pieces for each continent ----------
    def numbers(rows, caption="The numbers to call for police, fire or an ambulance"):
        body = "".join(f"<tr><td>{c}</td><td>{n}</td></tr>" for c, n in rows)
        return (f'<table><caption>{caption}</caption><tr><th scope="col">Country</th><th scope="col">Number</th></tr>{body}</table>'
                '<p>Save the number in your phone when you arrive. If it isn\'t listed here, the government of the country you\'re in lists it on its own site.</p>')

    findhelp = ext("https://findahelpline.com/", "Find A Helpline")
    everyone = f"""<section aria-labelledby="ev-h"><h2 id="ev-h">{ic("rights_legal")} Rights everyone has</h2>
<p>In 1948 the United Nations agreed on the {ext("https://www.un.org/en/about-us/universal-declaration-of-human-rights", "Universal Declaration of Human Rights")}. It says every person, in every country, is born free and equal in dignity and rights. Countries don't all live up to it, but it's the common starting point.</p>
<h3>If you're arrested away from home</h3>
<p>You can ask the police to tell your country's consulate. They have to tell you that you can ask. This comes from a treaty almost every country has signed, the Vienna Convention on Consular Relations.</p></section>"""
    common_src = [ext("https://www.un.org/en/about-us/universal-declaration-of-human-rights", "United Nations: Universal Declaration of Human Rights"),
                  ext("https://legal.un.org/ilc/texts/instruments/english/conventions/9_2_1963.pdf", "Vienna Convention on Consular Relations, Article 36"),
                  ext("https://www.iasp.info/crisis-centres-helplines/", "International Association for Suicide Prevention: helplines")]

    def ukadvice(country, slug):
        return ext(f"https://www.gov.uk/foreign-travel-advice/{slug}/getting-help", f"UK travel advice: emergency services in {country}")

    def continent(slug, name, lead, nums, crisis, rights, countries, sources):
        import dex
        alm = dex.ALMANAC.get(slug)
        alm_html, alm_src = "", []
        if alm:
            alm_html = (f'<section aria-labelledby="al-h"><h2 id="al-h">{ic("chart")} {name} at a glance</h2>{alm["html"]}'
                        f'<p><a href="{{P}}world-almanac.html">The whole world at a glance</a></p></section>')
            alm_src = [ext(u, t) for u, t in alm["sources"]]
        body = f"""
<section aria-labelledby="em-h"><h2 id="em-h">{ic("siren")} Emergency numbers</h2>{nums}</section>
<section aria-labelledby="cr-h"><h2 id="cr-h">{ic("crisis")} If you're thinking about suicide or can't cope</h2>{crisis}
<p>{"For any other country, " if crisis else ""}{findhelp} lists free, checked help lines in more than 150 countries. It's run by ThroughLine and backed by the International Association for Suicide Prevention.</p></section>
{everyone}
<section aria-labelledby="rg-h"><h2 id="rg-h">{ic("globe")} Rights in {name}</h2>{rights}</section>
{alm_html}
<section aria-labelledby="ct-h"><h2 id="ct-h">{ic("map_pin")} Countries in this guide</h2>{countries}</section>
{checked(sources + alm_src + common_src)}
"""
        URLS.append(page(f"places/{slug}.html", f"{name}: emergency numbers, help lines and rights | Earth Rules",
                         f"Starter guide for {name}: emergency numbers by country, crisis help lines, and the rights that apply there.",
                         f"EARTH RULES · {name.upper()}", f"{name}.", lead, body))

    none_yet = '<p>No full country guide here yet. They\'re added one at a time. Until then, the numbers above and <a href="world.html">what\'s true everywhere</a> still apply.</p>'
    american_conv = ext("https://treaties.un.org/pages/showdetails.aspx?objid=08000002800f10e1", "UN treaty record: American Convention on Human Rights")
    court_sj = ext("https://www.ohchr.org/sites/default/files/Documents/Publications/training9chapter3en.pdf", "UN human rights office: the Inter-American system")

    # ---------- North America ----------
    continent("north-america", "North America", "One number for any emergency: 911, in the United States, Canada and Mexico.",
        numbers([("United States", tel("911")), ("Canada", tel("911")), ("Mexico", tel("911"))],
                "911 reaches police, fire and ambulance in all three countries"),
        checklist([
            ("crisis", f"<strong>United States:</strong> call or text {tel('988')}. Veterans press 1."),
            ("crisis", f"<strong>Canada:</strong> call or text {tel('988', '9-8-8')}, any time, in English or French."),
            ("crisis", f"<strong>Mexico:</strong> Línea de la Vida, {tel('800 911 2000')}."),
        ]),
        "<p>Mexico has joined the American Convention on Human Rights, a treaty that lets people take a country to the Inter-American Court of Human Rights in San José, Costa Rica. The United States signed it in 1977 but never ratified it, and Canada hasn't joined. In those two countries, your rights come from their own constitutions and laws.</p>",
        f'{tiles([("us.html", "map_pin", "United States", "Full guide", ""), ("../states/ohio.html", "map_pin", "Ohio", "Full guide", "")])}<p>Canada and Mexico are next on the list.</p>',
        [ukadvice("the USA", "usa"), ukadvice("Canada", "canada"), ukadvice("Mexico", "mexico"),
         ext("https://988.ca/get-help/help-right-now", "9-8-8 Canada"), ext("https://988lifeline.org/", "988 Suicide and Crisis Lifeline (US)"),
         ext("https://www.conasama.salud.gob.mx/cnps/Img/suicidio.pdf", "Mexico CONASAMA: Línea de la Vida"),
         american_conv, ext("https://history.state.gov/historicaldocuments/frus1977-80v02/d118", "U.S. State Department history: 1977 signature"),
         ext("https://sencanada.ca/en/content/sen/committee/381/huma/rep/rep18may05-e", "Senate of Canada: the American Convention"), court_sj])

    # ---------- South America ----------
    continent("south-america", "South America", "Each country has its own numbers, and police, fire and ambulance are often separate.",
        numbers([("Brazil", f"Police {tel('190')} or {tel('911')} · Ambulance {tel('192')} · Fire {tel('193')}"),
                 ("Argentina", f"Police {tel('911')} or {tel('101')} · Ambulance {tel('107')} · Fire {tel('100')}"),
                 ("Colombia", f"Police and ambulance {tel('123')} · Fire {tel('119')}"),
                 ("Chile", f"Ambulance {tel('131')} · Fire {tel('132')} · Police {tel('133')}"),
                 ("Peru", f"Police {tel('105')} · Ambulance {tel('106')} · Fire {tel('116')}")]),
        "",
        "<p>Many countries in the Americas have joined the American Convention on Human Rights, also called the Pact of San José (1969). If a country's own courts fail you, the Inter-American system can hear the case, and its court sits in San José, Costa Rica.</p>",
        none_yet,
        [ukadvice("Brazil", "brazil"), ukadvice("Argentina", "argentina"), ukadvice("Colombia", "colombia"),
         ukadvice("Chile", "chile"), ukadvice("Peru", "peru"), american_conv, court_sj])

    # ---------- Europe ----------
    continent("europe", "Europe", "112 works free from any phone in every European Union country.",
        numbers([("Every EU country", tel("112")), ("United Kingdom", f"{tel('999')} or {tel('112')}")],
                "112 reaches police, fire and ambulance across the EU")
        + "<p>Some EU countries also keep their own older numbers, but 112 always works there.</p>",
        checklist([
            ("crisis", f"<strong>116 123</strong> is set aside across the EU for emotional support lines."),
            ("crisis", f"<strong>UK and Ireland:</strong> Samaritans on {tel('116 123')}, free from any phone, 24 hours a day."),
        ]),
        "<p>46 countries have signed the European Convention on Human Rights, including every EU country and the UK. If your own country's courts don't fix a rights problem, you can take it to the European Court of Human Rights in Strasbourg, France, and its rulings bind the country involved.</p>",
        none_yet,
        [ext("https://europa.eu/youreurope/citizens/travel/security-and-emergencies/emergency/", "Your Europe: 112"),
         ext("https://www.gov.uk/guidance/999-and-112-the-uks-national-emergency-numbers", "GOV.UK: 999 and 112"),
         ext("https://www.legislation.gov.uk/eudn/2007/116/annex", "EU Decision 2007/116/EC: the 116 numbers"),
         ext("https://www.samaritans.org/how-we-can-help/contact-samaritan/", "Samaritans"),
         ext("https://www.echr.coe.int/general-presentation", "European Court of Human Rights"),
         ext("https://www.echr.coe.int/documents/d/echr/50Questions_ENG", "European Court of Human Rights: 50 questions")])

    # ---------- Africa ----------
    continent("africa", "Africa", "Numbers differ by country, and in many places an ambulance can be slow to come.",
        numbers([("South Africa", f"Police {tel('10111')} · Ambulance and fire {tel('10177')} · From a mobile {tel('112')}"),
                 ("Nigeria", f"{tel('112')} for police, fire and ambulance. There's no national ambulance service."),
                 ("Kenya", f"{tel('999')} for police, fire and ambulance"),
                 ("Egypt", f"Police {tel('122')} · Ambulance {tel('123')} · Fire {tel('180')} · Tourist police {tel('126')}")]),
        "",
        "<p>54 of the African Union's 55 countries have joined the African Charter on Human and Peoples' Rights. The African Commission in Banjul, The Gambia, hears complaints. The African Court in Arusha, Tanzania, can rule on them, but only a handful of countries let a person bring a case there directly.</p>",
        none_yet,
        [ukadvice("South Africa", "south-africa"), ukadvice("Nigeria", "nigeria"), ukadvice("Kenya", "kenya"), ukadvice("Egypt", "egypt"),
         ext("https://achpr.au.int/en/charter/african-charter-human-and-peoples-rights", "African Commission: the African Charter"),
         ext("https://achpr.au.int/en/commission/secretariat", "African Commission: where it is"),
         ext("https://www.african-court.org/afchpr/basic-information-2/", "African Court on Human and Peoples' Rights")])

    # ---------- Asia ----------
    continent("asia", "Asia", "The biggest continent, with many different numbers. Look yours up when you arrive.",
        numbers([("India", f"{tel('112')} for police, fire and ambulance"),
                 ("China", f"Police {tel('110')} · Ambulance {tel('120')} · Fire {tel('119')}"),
                 ("Japan", f"Police {tel('110')} · Fire and ambulance {tel('119')}"),
                 ("South Korea", f"Police {tel('112')} · Fire and ambulance {tel('119')}"),
                 ("Philippines", f"{tel('911')} for police, fire and ambulance"),
                 ("Indonesia", f"Police {tel('110')} or {tel('112')} from a mobile · Ambulance {tel('118')} or {tel('119')} · Fire {tel('113')}. Official lists differ, so check locally.")]),
        "",
        "<p>Asia has no region-wide human rights treaty or court. Southeast Asian countries agreed the ASEAN Human Rights Declaration in 2012, but it's a statement, with no court behind it. Several Arab countries have joined the Arab Charter on Human Rights, which has a committee but no court yet. In most of Asia, your rights come from each country's own laws.</p>",
        none_yet,
        [ukadvice("India", "india"), ukadvice("China", "china"), ukadvice("Japan", "japan"),
         ukadvice("South Korea", "south-korea"), ukadvice("the Philippines", "philippines"), ukadvice("Indonesia", "indonesia"),
         ext("https://www.indonesia.travel/gb/en/general-information/staying-safe-in-indonesia", "Indonesia Travel: staying safe"),
         ext("https://asean.org/asean-human-rights-declaration/", "ASEAN Human Rights Declaration"),
         ext("http://lasportal.org/en/humanrights/Pages/default.aspx", "League of Arab States: human rights"),
         ext("https://bangkok.ohchr.org/sites/default/files/wp_files/2023/11/Summary-Report-for-HR75-Asia-Pacific-Regional-Dialogue.pdf", "UN human rights office: Asia-Pacific dialogue, 2023")])

    # ---------- Oceania ----------
    continent("oceania", "Oceania", "Australia uses 000. New Zealand uses 111.",
        numbers([("Australia", f"{tel('000')}. {tel('112')} also works, but only from a mobile. {tel('106')} is the text phone line for people who are deaf or can't speak."),
                 ("New Zealand", f"{tel('111')} for police, fire and ambulance")]),
        checklist([
            ("crisis", f"<strong>Australia:</strong> Lifeline on {tel('13 11 14')}, or text {'<a href=\"sms:0477131114\">0477 13 11 14</a>'}, any time."),
            ("crisis", f"<strong>New Zealand:</strong> call or text {tel('1737')}, free, any time."),
        ]),
        "<p>Oceania has no regional human rights treaty or court. Your rights come from each country's own laws, with the Universal Declaration above as the common starting point.</p>",
        none_yet,
        [ext("https://www.triplezero.gov.au/", "Triple Zero (Australia)"),
         ext("https://www.infrastructure.gov.au/media-communications/phone/triple-zero/using-other-emergency-numbers", "Australian Government: 112 and 106"),
         ukadvice("New Zealand", "new-zealand"),
         ext("https://www.lifeline.org.au/131114", "Lifeline Australia"), ext("https://www.1737.org.nz/how-1737-works", "1737 New Zealand"),
         ext("https://bangkok.ohchr.org/sites/default/files/wp_files/2023/11/Summary-Report-for-HR75-Asia-Pacific-Regional-Dialogue.pdf", "UN human rights office: Asia-Pacific dialogue, 2023")])

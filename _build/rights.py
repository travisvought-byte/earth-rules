"""Your rights: by situation and by place. Imported by build.py."""


def build(page, ic, ext, checklist, checked, URLS):
    # ---------- source helpers ----------
    def amend(n, label=None):
        return ext(f"https://constitution.congress.gov/constitution/amendment-{n}/", label or f"U.S. Constitution, Amendment {n}")

    def usc(t, s, label=None):
        return ext(f"https://www.law.cornell.edu/uscode/text/{t}/{s}", label or f"{t} U.S. Code § {s}")

    def cfr(t, s, label=None):
        return ext(f"https://www.law.cornell.edu/cfr/text/{t}/{s}", label or f"{t} CFR § {s}")

    def orc(s, label=None):
        return ext(f"https://codes.ohio.gov/ohio-revised-code/section-{s}", label or f"Ohio Revised Code {s}")

    def ohcon(s, label=None):
        return ext(f"https://codes.ohio.gov/ohio-constitution/section-{s}", label or f"Ohio Constitution, Article I, Section {s.split('.', 1)[1]}")

    def case(name, vol, pg, year):
        return ext(f"https://supreme.justia.com/cases/federal/us/{vol}/{pg}/", f"<cite>{name}</cite> ({year})")

    def rights(items):
        """items: (icon, 'You have the right to ...', 'plain explanation', 'source html')"""
        out = '<ul class="check rights">'
        for i, r, how, src in items:
            out += (f'<li>{ic(i)}<span><strong>{r}</strong> {how}'
                    f'<span class="cite">Source: {src}</span></span></li>')
        return out + "</ul>"

    def say(lines):
        return '<div class="note say"><p><strong>What to say</strong></p><ul>' + "".join(f"<li>{x}</li>" for x in lines) + "</ul></div>"

    def where(fed, oh):
        return (f'<section aria-labelledby="us-h"><h2 id="us-h">{ic("globe")} Everywhere in the United States</h2>{fed}</section>'
                f'<section aria-labelledby="oh-h"><h2 id="oh-h">{ic("map_pin")} In Ohio, you also have these</h2>{oh}</section>')

    CR = ("EARTH RULES · YOUR RIGHTS", [("Earth Rules", "https://earthrules.org/"), ("Your rights", "https://earthrules.org/rights/")])

    def rp(slug, title, desc, h1, lead, body):
        url = f"https://earthrules.org/rights/{slug}.html"
        URLS.append(page(f"rights/{slug}.html", f"{title} | Earth Rules", desc, CR[0], h1, lead, body,
                         crumbs=CR[1] + [(h1.rstrip("."), url)]))

    enforce_note = ('<p class="note">A right works best when you name it. Say it out loud, put it in writing, keep copies, '
                    'and write down dates and names. Free legal help in Ohio: ' + ext("https://www.ohiolegalhelp.org/", "Ohio Legal Help") +
                    '. Anywhere else, dial <a href="tel:211">211</a> and ask for legal aid.</p>')

    # ================= Everyone =================
    everyone_fed = rights([
        ("megaphone", "You have the right to speak, worship or not, gather peacefully and petition the government.",
         "The government can't punish you for your views or your religion. Private employers and websites are not the government, so their own rules can still apply.", amend(1)),
        ("lock", "You have the right to be secure in your person, home, papers and belongings.",
         "Government searches and seizures must be reasonable, and most need a warrant signed by a judge.", amend(4)),
        ("rights_legal", "You have the right to due process.",
         "No government can take your life, liberty or property without fair procedures: notice of what's happening and a real chance to be heard.", amend(5) + "; " + amend(14)),
        ("peer_support", "You have the right to equal protection of the laws.",
         "Every person, citizen or not, is covered. The Fourteenth Amendment says \"any person,\" and the Supreme Court has read it that way since 1886.", amend(14) + "; " + case("Yick Wo v. Hopkins", 118, 356, 1886)),
        ("shield", "You have the right to keep and bear arms.",
         "States and cities set rules on carrying, buying and where weapons can go, so check the law where you are.", amend(2)),
        ("no", "You have the right to be free from slavery and forced labor.",
         "The only exception the Constitution writes in is punishment for a crime after conviction.", amend(13)),
        ("book", "You have rights that aren't written down in a list.",
         "The Ninth Amendment says naming some rights does not deny or shrink the others the people keep.", amend(9)),
    ])
    everyone_oh = rights([
        ("book", "You have inalienable rights, and Ohio's Constitution says so first.",
         "Article I, Section 1 begins: \"All men are, by nature, free and independent, and have certain inalienable rights,\" including enjoying and defending life and liberty, owning property and seeking happiness and safety.", ohcon("1.1")),
        ("megaphone", "You have the right to speak, write and publish your views on any subject.",
         "You are responsible for abuse of that right, such as defamation.", ohcon("1.11")),
        ("lock", "You have the right to be secure in your person, house, papers and possessions.",
         "Ohio's own search and seizure protection sits alongside the federal one.", ohcon("1.14")),
        ("peer_support", "You have the right not to be treated differently because of race, color, religion, sex, military status, national origin, disability, age or ancestry.",
         "This covers jobs, housing and businesses open to the public in Ohio.", orc("4112.02")),
    ])
    rp("everyone", "Rights every person has", "The rights every person in the US has, from speech and religion to due process and equal protection, plus Ohio's own Bill of Rights.",
       "Rights every person has.", "These are yours because you're a person. They limit what any government can do to you.",
       where(everyone_fed, everyone_oh) + enforce_note + checked([
           amend(1), amend(4), amend(9), amend(14), case("Yick Wo v. Hopkins", 118, 356, 1886), ohcon("1.1"), orc("4112.02")]))

    # ================= Police, arrest, court =================
    police_fed = rights([
        ("chat_q", "You have the right to remain silent.",
         "You don't have to answer questions about where you've been, where you're going or what you did. To use it, say so out loud; silence alone may not count.",
         amend(5) + "; " + case("Berghuis v. Thompkins", 560, 370, 2010)),
        ("rights_legal", "You have the right to a lawyer, and to a free one if you can't afford it.",
         "Once you ask for a lawyer, questioning is supposed to stop until one is there. If you're charged with a crime that can mean jail, the court appoints a lawyer at no cost.",
         amend(6) + "; " + case("Miranda v. Arizona", 384, 436, 1966) + "; " + case("Gideon v. Wainwright", 372, 335, 1963)),
        ("lock", "You have the right to refuse consent to a search.",
         "Police may still search if they have a warrant or another legal reason, but your \"no\" matters later in court. Don't physically resist; say it.", amend(4)),
        ("clock", "You have the right to ask whether you are free to go.",
         "If you're not under arrest or being detained, you can calmly walk away. A traffic stop can last only as long as its purpose needs.",
         amend(4) + "; " + case("Rodriguez v. United States", 575, 348, 2015)),
        ("document", "You have the right to know the charges against you.",
         "You also have the right to a speedy and public trial, a jury, to see and question the witnesses against you, and to call your own.", amend(6)),
        ("funding", "You have the right to bail that isn't excessive, and to be free from cruel and unusual punishment.", "", amend(8)),
        ("no", "You have the right not to be tried twice for the same crime.", "", amend(5)),
        ("phone", "You have the right to tell your consulate if you're not a US citizen.",
         "If you're arrested, ask the police to notify your country's consulate.", ext("https://travel.state.gov/content/travel/en/consularnotification.html", "State Department: consular notification")),
    ])
    police_oh = rights([
        ("chat_q", "You have the right to stay silent beyond your name, address and date of birth.",
         "In a public place, if an officer reasonably suspects you of a crime or of witnessing a serious one, Ohio requires you to give those three things. Nothing more is required. Drivers must also show a license when asked.",
         orc("2921.29") + "; " + orc("4507.35")),
        ("rights_legal", "You have the right to a lawyer, a speedy public trial by an impartial jury, and to meet the witnesses against you face to face.",
         "You can't be forced to testify against yourself.", ohcon("1.10")),
        ("clock", "You have the right to a trial within set time limits.",
         "For a felony, trial must start within 270 days of arrest. Each day you're held in jail on that charge alone counts as three.", orc("2945.71")),
        ("funding", "You have the right to bail in most cases.",
         "Ohio judges set bail and its conditions; excessive bail is barred.", ohcon("1.9")),
        ("ballot", "You keep your right to vote if you're charged but not convicted, and it comes back when you leave prison.",
         "People held in jail awaiting trial, or for a misdemeanor, can vote absentee. After release from a felony sentence, re-register.", orc("2961.01")),
    ])
    victims = rights([
        ("shield", "If a crime is committed against you in Ohio, you have the right to be treated with fairness and respect for your safety, dignity and privacy.",
         "You also have the right to notice of public court dates, to be present, to be heard at release, plea, sentencing and parole hearings, to reasonable protection from the accused, to restitution, and to written notice of these rights.", ohcon("1.10a", "Ohio Constitution, Article I, Section 10a (Marsy's Law)")),
        ("document", "In a federal case, you have similar rights.", "These include being protected from the accused, notified of hearings, heard, and paid restitution.", usc(18, 3771)),
    ])
    pol_say = say(["\"I'm going to remain silent.\"", "\"I want a lawyer.\"", "\"I don't consent to a search.\"", "\"Am I free to go?\""])
    rp("police", "Stopped, arrested or accused: your rights", "Your rights if police stop you, search you, arrest you or charge you with a crime, plus the rights of crime victims, in the US and in Ohio.",
       "Stopped, arrested or accused.", "You have rights at every step: on the street, in a car, in custody and in court.",
       pol_say + where(police_fed, police_oh) +
       f'<section aria-labelledby="vic-h"><h2 id="vic-h">{ic("shield")} If you are the victim</h2>{victims}</section>' +
       '<p class="note">Keep your hands visible, stay calm, and don\'t run or physically resist, even if you believe the stop is wrong. Challenge it later with a lawyer. Write down badge numbers and car numbers when you can.</p>' +
       enforce_note + checked([amend(4), amend(5), amend(6), amend(8), case("Miranda v. Arizona", 384, 436, 1966), case("Gideon v. Wainwright", 372, 335, 1963),
                               case("Berghuis v. Thompkins", 560, 370, 2010), case("Rodriguez v. United States", 575, 348, 2015),
                               orc("2921.29"), orc("2945.71"), ohcon("1.10"), ohcon("1.10a", "Ohio Constitution, Article I, Section 10a"), usc(18, 3771)]))

    # ================= Patients =================
    pat_fed = rights([
        ("document", "You have the right to see and get a copy of your medical records.",
         "Your provider or health plan must act within 30 days, with one 30-day extension if they tell you why in writing. Fees are limited to a reasonable cost.", cfr(45, "164.524")),
        ("document", "You have the right to ask for a correction to your records.", "If they say no, you can add your own statement of disagreement.", cfr(45, "164.526")),
        ("crisis", "You have the right to emergency care whether or not you can pay.",
         "Any hospital with an emergency department that takes Medicare must screen you and stabilize an emergency, or transfer you safely, before asking about money.", usc(42, "1395dd")),
        ("funding", "You have the right to be protected from most surprise medical bills.",
         "For emergency care, and for out-of-network doctors at an in-network hospital, you pay only your in-network share. Uninsured or paying yourself? You have the right to a good faith estimate before care.",
         ext("https://www.cms.gov/nosurprises", "CMS: No Surprises Act")),
        ("language", "You have the right to a free interpreter.",
         "Health programs that receive federal money must provide language help and sign language interpreters at no cost to you.", usc(42, 18116, "42 U.S. Code § 18116 (ACA Section 1557)")),
        ("document", "You have the right to make your own care decisions in advance.",
         "Hospitals and nursing homes in Medicare must tell you about your right to write an advance directive.", usc(42, "1395cc", "42 U.S. Code § 1395cc(f)")),
        ("lock", "You have the right to privacy for your health information.", "Most providers can't share it without your permission, outside of treatment, billing and a few other uses.", cfr(45, "164.502")),
    ])
    pat_oh = rights([
        ("document", "You have the right to inspect your records free, or get a copy, within a reasonable time.", "Ohio caps what providers can charge for copies.", orc("3701.74") + "; " + orc("3701.741")),
        ("document", "You have the right to name someone to make health decisions if you can't.", "That's a health care power of attorney.", orc("1337.12")),
        ("document", "You have the right to decide in writing about life support at the end of life.", "That's a living will.", orc("2133.02")),
        ("housing", "If you live in a nursing home, you have a written bill of rights.", "It covers dignity, privacy, visitors, your own money and belongings, and taking part in your care plan.", orc("3721.13")),
        ("medical", "If you're in mental health treatment, you have specific rights.", "These include humane care, privacy, contact with family and friends, and talking with a lawyer.", orc("5122.29")),
    ])
    rp("patients", "Your rights as a patient", "Your rights in health care: your records, emergency care, surprise bills, interpreters, advance directives and privacy, in the US and in Ohio.",
       "Your rights as a patient.", "Your body, your records, your decisions.",
       where(pat_fed, pat_oh) +
       '<p class="note">Problem with records or privacy? File with ' + ext("https://www.hhs.gov/hipaa/filing-a-complaint/index.html", "HHS Office for Civil Rights") + ' within 180 days.</p>' +
       enforce_note + checked([cfr(45, "164.524"), cfr(45, "164.526"), usc(42, "1395dd"), ext("https://www.cms.gov/nosurprises", "CMS: No Surprises Act"), usc(42, 18116), orc("3701.74"), orc("1337.12"), orc("2133.02"), orc("3721.13"), orc("5122.29")]))

    # ================= Tenants =================
    ten_fed = rights([
        ("housing", "You have the right to rent or buy a home without discrimination.",
         "Landlords and sellers can't turn you away, charge you more or treat you differently because of race, color, religion, sex, national origin, familial status (kids under 18) or disability.", usc(42, 3604)),
        ("service_dog", "You have the right to reasonable accommodations for a disability.",
         "That includes an assistance animal in a no-pets building, or a reserved parking space, when you need it.", usc(42, 3604, "42 U.S. Code § 3604(f)")),
        ("veterans", "If you're on active duty, you have the right to end a lease early for orders.",
         "That covers a permanent change of station or a deployment of 90 days or more.", usc(50, 3955)),
    ])
    ten_oh = rights([
        ("wrench", "You have the right to a safe place that's kept up.",
         "Your landlord must make repairs, keep the place fit to live in, and keep electrical, plumbing, heating and sanitation working.", orc("5321.04")),
        ("door_out", "You have the right to notice before your landlord comes in.",
         "Twenty-four hours is presumed reasonable, except in an emergency.", orc("5321.04", "Ohio Revised Code 5321.04(A)(8)")),
        ("funding", "You have the right to pay rent to the court instead of the landlord when repairs aren't made.",
         "Give written notice. If it isn't fixed within a reasonable time, or 30 days at most, and your rent is current, you can deposit rent with the clerk of court. Some small landlords are exempt.", orc("5321.07")),
        ("funding", "You have the right to your security deposit back, or a written list of deductions, within 30 days.",
         "Give your landlord a forwarding address in writing. If they wrongfully keep money, you can recover it plus an equal amount in damages and attorney fees.", orc("5321.16")),
        ("shield", "You have the right to complain without retaliation.",
         "Your landlord can't raise rent, cut services or evict you for reporting code violations or asking for repairs.", orc("5321.02")),
        ("lock", "You have the right not to be locked out or have utilities shut off to force you out.", "Only a court can order an eviction.", orc("5321.15") + "; " + orc("1923.04")),
        ("peer_support", "Ohio adds ancestry and military status to the list of protected classes in housing.", "", orc("4112.02")),
    ])
    rp("tenants", "Your rights as a renter", "Your rights as a tenant: fair housing, repairs, notice before entry, your deposit, rent escrow and eviction, in the US and in Ohio.",
       "Your rights as a renter.", "A lease is a deal between two sides. These are yours no matter what it says.",
       where(ten_fed, ten_oh) +
       '<p class="note">Housing discrimination: report to ' + ext("https://www.hud.gov/reporthousingdiscrimination", "HUD") + ' within one year, or to the ' + ext("https://civ.ohio.gov/", "Ohio Civil Rights Commission") + '. If you get an eviction notice, go to every court date: that\'s where you have the right to be heard.</p>' +
       enforce_note + checked([usc(42, 3604), usc(50, 3955), orc("5321.02"), orc("5321.04"), orc("5321.07"), orc("5321.15"), orc("5321.16"), orc("1923.04"), orc("4112.02")]))

    # ================= Workers =================
    work_fed = rights([
        ("funding", "You have the right to at least the minimum wage, and overtime pay.",
         "The federal minimum is $7.25 an hour. Most hourly workers earn time and a half after 40 hours in a week.", usc(29, 206) + "; " + usc(29, 207)),
        ("peer_support", "You have the right to work free of discrimination.",
         "That covers race, color, religion, sex (including pregnancy, sexual orientation and gender identity), national origin, age 40 and over, disability and genetic information. Most of these laws apply at employers with 15 or more workers.",
         usc(42, "2000e-2") + "; " + case("Bostock v. Clayton County", 590, 644, 2020) + "; " + usc(29, 623) + "; " + usc(42, 12112)),
        ("funding", "You have the right to equal pay for equal work, regardless of sex.", "", usc(29, 206, "29 U.S. Code § 206(d)")),
        ("medical", "You have the right to job-protected leave for a new child or a serious health condition.",
         "Up to 12 weeks unpaid a year, if your employer has 50 or more employees nearby and you've worked there a year and 1,250 hours.", usc(29, 2612)),
        ("children", "You have the right to reasonable accommodations for pregnancy, and break time and a private place to pump.", "", usc(42, "2000gg-1") + "; " + usc(29, "218d")),
        ("chat_q", "You have the right to talk with coworkers about pay and working conditions, and to organize.",
         "This protects most private-sector workers, union or not, but not supervisors.", usc(29, 157)),
        ("shield", "You have the right to a safe workplace and to report hazards.",
         "Your employer can't punish you for a safety complaint. A retaliation complaint must reach OSHA within 30 days.", usc(29, 660, "29 U.S. Code § 660(c)") + "; " + ext("https://www.osha.gov/workers/file-complaint", "OSHA: file a complaint")),
        ("veterans", "You have the right to your job back after military service.", "", usc(38, 4312)),
    ])
    work_oh = rights([
        ("funding", "You have the right to Ohio's higher minimum wage: $11.00 an hour in 2026.",
         "It applies at employers with more than $405,000 in yearly gross receipts. Tipped workers get at least $5.50 plus tips that reach the full minimum. It rises with inflation each January, to $11.40 on January 1, 2027.",
         ext("https://codes.ohio.gov/ohio-constitution/section-2.34a", "Ohio Constitution, Article II, Section 34a") + "; " + ext("https://com.ohio.gov/divisions-and-programs/industrial-compliance/wage-and-hour/guides-and-resources/ohio-minimum-wage-laws/", "Ohio Department of Commerce: minimum wage")),
        ("peer_support", "You have the right to work free of discrimination at Ohio employers with four or more workers.",
         "Ohio adds military status and ancestry to the federal list.", orc("4112.02")),
        ("ballot", "You have the right to take a reasonable amount of time to vote without being fired or threatened.", "", orc("3599.06")),
    ])
    rp("workers", "Your rights at work", "Your rights as a worker: minimum wage and overtime, discrimination, family leave, pregnancy, organizing and safety, in the US and in Ohio.",
       "Your rights at work.", "You trade your time for pay. The terms have a floor, and these rights are it.",
       where(work_fed, work_oh) +
       '<p class="note">Unpaid wages: ' + ext("https://www.dol.gov/agencies/whd/contact/complaints", "Wage and Hour Division") + ', free and confidential. Discrimination: ' + ext("https://www.eeoc.gov/how-file-charge-employment-discrimination", "EEOC") + ' within 300 days in Ohio, or the ' + ext("https://civ.ohio.gov/", "Ohio Civil Rights Commission") + '. Deadlines are short, so act soon.</p>' +
       enforce_note + checked([usc(29, 206), usc(29, 207), usc(42, "2000e-2"), case("Bostock v. Clayton County", 590, 644, 2020), usc(29, 2612), usc(29, 157), usc(38, 4312),
                               ext("https://codes.ohio.gov/ohio-constitution/section-2.34a", "Ohio Constitution, Article II, Section 34a"), orc("4112.02"), orc("3599.06")]))

    # ================= Consumers =================
    con_fed = rights([
        ("document", "You have the right to see your credit reports and fix mistakes.",
         "The credit bureau generally has 30 days to investigate a dispute. Free weekly reports are at " + ext("https://www.annualcreditreport.com/", "AnnualCreditReport.com") + ".", usc(15, "1681i")),
        ("chat_q", "You have the right to make a debt collector prove the debt.",
         "Dispute it in writing within 30 days of their first notice, and they must stop collecting until they send proof.", usc(15, "1692g")),
        ("no", "You have the right to tell a debt collector to stop contacting you.",
         "Put it in writing. They also can't harass you, call before 8 a.m. or after 9 p.m., or lie to you.", usc(15, "1692c") + "; " + usc(15, "1692d")),
        ("funding", "You have the right to dispute a credit card billing error.", "Write to the card company within 60 days of the statement.", usc(15, 1666)),
        ("door_out", "You have the right to cancel a door-to-door sale of $25 or more within three business days.", "", cfr(16, "429.1")),
        ("phone", "You have the right to stop telemarketing calls.", "Add your number free at " + ext("https://www.donotcall.gov/", "DoNotCall.gov") + ".", usc(47, 227)),
    ])
    con_oh = rights([
        ("shield", "You have the right to deal with businesses that don't deceive you.", "Unfair or deceptive sales practices are illegal, and you can sue or complain to the Attorney General.", orc("1345.02")),
        ("door_out", "You have the right to cancel a home sale until midnight of the third business day.", "The seller must tell you about it and refund you within 10 business days.", orc("1345.22") + "; " + orc("1345.23")),
        ("transportation", "You have the right to a refund or replacement for a new car that can't be fixed.", "That's Ohio's lemon law.", orc("1345.72")),
    ])
    rp("consumers", "Your rights as a consumer", "Your rights with credit reports, debt collectors, billing errors, door-to-door sales and telemarketers, in the US and in Ohio.",
       "Your rights as a consumer.", "When you buy, borrow or owe, these rights come with you.",
       where(con_fed, con_oh) +
       '<p class="note">Complaints: ' + ext("https://www.consumerfinance.gov/complaint/", "Consumer Financial Protection Bureau") + ' for banks, credit and debt; ' + ext("https://filecomplaint.ohioattorneygeneral.gov/", "Ohio Attorney General") + ' for businesses in Ohio.</p>' +
       enforce_note + checked([usc(15, "1681i"), usc(15, "1692g"), usc(15, "1692c"), usc(15, 1666), cfr(16, "429.1"), usc(47, 227), orc("1345.02"), orc("1345.22"), orc("1345.72")]))

    # ================= Voters =================
    vote_fed = rights([
        ("ballot", "You have the right to vote at 18, whatever your race, color or sex.", "No poll tax can be charged in federal elections.", amend(15) + "; " + amend(19) + "; " + amend(24) + "; " + amend(26)),
        ("peer_support", "You have the right to bring someone to help you vote if you need it because of a disability or trouble reading.",
         "Anyone you choose can help, except your employer or union officer.", usc(52, 10508)),
        ("document", "You have the right to a provisional ballot if your name isn't on the list.", "It's counted once your eligibility is confirmed.", usc(52, 21082)),
        ("language", "In some counties, you have the right to voting materials in your language.", "", usc(52, "10503")),
    ])
    vote_oh = rights([
        ("clock", "You have the right to vote if you're in line when polls close.", "Polls are open 6:30 a.m. to 7:30 p.m. Stay in line.", orc("3501.32")),
        ("ballot", "You have the right to time off work to vote.", "Your employer can't fire or threaten you for taking a reasonable amount of time.", orc("3599.06")),
        ("document", "You have the right to vote with any of the accepted photo IDs.", "Without one, you can cast a provisional ballot and show ID within four days.", orc("3505.18")),
        ("ballot", "Your right to vote returns when you leave prison.", "A felony record doesn't stop you from voting in Ohio once you're released. Re-register.", orc("2961.01")),
    ])
    rp("voters", "Your rights as a voter", "Your voting rights: age, race and sex protections, help in the booth, provisional ballots, staying in line, time off work, ID, and voting after a conviction.",
       "Your rights as a voter.", "Your vote is your voice in what the government does next.",
       where(vote_fed, vote_oh) +
       '<p class="note">Turned away or intimidated? Ask for a provisional ballot, then report it to the ' + ext("https://www.ohiosos.gov/", "Ohio Secretary of State") + ' or ' + ext("https://civilrights.justice.gov/", "the Justice Department") + '.</p>' +
       enforce_note + checked([amend(15), amend(19), amend(24), amend(26), usc(52, 10508), usc(52, 21082), orc("3501.32"), orc("3599.06"), orc("3505.18"), orc("2961.01")]))

    # ================= Students =================
    stu_fed = rights([
        ("school", "You have the right to a free public education, whatever your immigration status.", "", case("Plyler v. Doe", 457, 202, 1982)),
        ("megaphone", "You have the right to free speech at school.", "Schools can limit speech that substantially disrupts class, but they can't silence a view just because they dislike it.", case("Tinker v. Des Moines", 393, 503, 1969)),
        ("document", "You, or your parents if you're under 18 and in K-12, have the right to see school records within 45 days and ask for corrections.", "", cfr(34, "99.10") + "; " + usc(20, "1232g")),
        ("cane", "If you have a disability, you have the right to a free appropriate public education, with an IEP or a 504 plan.", "", usc(20, 1412) + "; " + usc(29, 794)),
        ("shield", "You have the right to an education free of sex discrimination and sexual harassment.", "", usc(20, 1681)),
        ("housing", "If you don't have a stable home, you have the right to enroll right away, without the usual papers.", "You can stay at your school of origin when that's in your best interest.", usc(42, 11432)),
    ])
    rp("students", "Your rights as a student", "Your rights in school: free public education, free speech, records, disability services, Title IX and enrolling without a home.",
       "Your rights as a student.", "School is where you learn your rights. These are yours while you're there.",
       f'<section aria-labelledby="us-h"><h2 id="us-h">{ic("globe")} Everywhere in the United States</h2>{stu_fed}</section>'
       '<p class="note">Ohio-specific student rights are on the way. Complaints about discrimination at school go to the ' + ext("https://www.ed.gov/", "US Department of Education") + "'s Office for Civil Rights.</p>" +
       enforce_note + checked([case("Plyler v. Doe", 457, 202, 1982), case("Tinker v. Des Moines", 393, 503, 1969), cfr(34, "99.10"), usc(20, 1412), usc(29, 794), usc(20, 1681), usc(42, 11432)]))

    # ================= Veterans and service members =================
    vet_fed = rights([
        ("veterans", "You have the right to your civilian job back after service.", "With the seniority and pay you'd have earned, if you give notice and return on time.", usc(38, 4312)),
        ("rights_legal", "You have the right to challenge a VA decision.", "Within one year: a Supplemental Claim with new evidence, a Higher-Level Review, or a Board Appeal.", usc(38, "5104C") + "; " + ext("https://www.va.gov/resources/choosing-a-decision-review-option/", "VA: choosing a decision review option")),
        ("peer_support", "You have the right to free help with a VA claim.", "Accredited veterans service officers help at no cost.", ext("https://www.va.gov/ogc/apps/accreditation/index.asp", "VA accreditation search")),
        ("document", "You have the right to a copy of your own VA records.", "", usc(5, "552a", "Privacy Act, 5 U.S. Code § 552a(d)")),
        ("funding", "On active duty, you have the right to cap interest at 6% on debts from before you joined.", "", usc(50, 3937)),
        ("housing", "On active duty, you have the right to end a lease or car lease early for orders.", "", usc(50, 3955)),
        ("work_school", "You have the right to veterans' preference in federal hiring.", "", usc(5, 2108)),
    ])
    vet_oh = rights([
        ("peer_support", "You have the right to free help from your county veterans service office.", "Every Ohio county has one.", ext("https://codes.ohio.gov/ohio-revised-code/chapter-5901", "Ohio Revised Code Chapter 5901")),
        ("shield", "You have the right not to be treated differently at work or in housing because of military status.", "", orc("4112.02")),
    ])
    rp("veterans", "Your rights as a veteran or service member", "Your rights as a veteran or service member: your job back, VA appeals, free claim help, records, interest caps, leases and hiring preference.",
       "Your rights as a veteran or service member.", "You served. These are yours.",
       where(vet_fed, vet_oh) + enforce_note +
       checked([usc(38, 4312), usc(38, "5104C"), ext("https://www.va.gov/resources/choosing-a-decision-review-option/", "VA decision reviews"), usc(50, 3937), usc(50, 3955), usc(5, 2108), orc("4112.02")]))

    # ================= Disability =================
    dis_fed = rights([
        ("ramps_home", "You have the right to equal access to businesses open to the public.", "Stores, restaurants, hotels, doctors' offices and more must make reasonable changes so you can use them.", usc(42, 12182)),
        ("navigation", "You have the right to equal access to government programs and services.", "That includes courts, schools, transit and voting.", usc(42, 12132)),
        ("work_school", "You have the right to reasonable accommodations at work.", "At employers with 15 or more workers, unless it would cause undue hardship.", usc(42, 12112)),
        ("service_dog", "You have the right to bring your service dog almost anywhere the public can go.", "Staff can ask only two questions: is it needed because of a disability, and what task is it trained to do.", cfr(28, "36.302")),
        ("plane", "You have the right to fly without disability discrimination.", "", usc(49, 41705)),
        ("housing", "You have the right to reasonable accommodations and modifications in housing.", "", usc(42, 3604, "42 U.S. Code § 3604(f)")),
    ])
    dis_oh = rights([
        ("peer_support", "You have the right not to be treated differently because of disability at work, in housing and in public places in Ohio.", "", orc("4112.02")),
        ("service_dog", "You have the right to be accompanied by your assistance dog in Ohio public places and transportation.", "", orc("955.43")),
    ])
    rp("disability", "Your rights with a disability", "Your rights with a disability: access to businesses and government, accommodations at work and home, service dogs and air travel, in the US and in Ohio.",
       "Your rights with a disability.", "Access is not a favor. It is a right.",
       where(dis_fed, dis_oh) +
       '<p class="note">Complaints: ' + ext("https://www.ada.gov/", "ADA.gov") + ' for access problems.</p>' +
       enforce_note + checked([usc(42, 12182), usc(42, 12132), usc(42, 12112), cfr(28, "36.302"), usc(49, 41705), orc("4112.02"), orc("955.43")]))

    # ================= Index =================
    situations = [
        ("everyone", "peer_support", "Every person", "Speech, religion, privacy, due process and equal protection."),
        ("police", "rights_legal", "Stopped, arrested or accused", "Silence, a lawyer, searches, trials, and victims' rights."),
        ("patients", "medical", "Patients", "Your records, emergency care, surprise bills and your own decisions."),
        ("tenants", "housing", "Renters", "Fair housing, repairs, notice, deposits and eviction."),
        ("workers", "work_school", "Workers", "Pay, overtime, discrimination, leave, organizing and safety."),
        ("consumers", "funding", "Consumers", "Credit reports, debt collectors, billing errors and canceling sales."),
        ("voters", "ballot", "Voters", "Who can vote, help in the booth, ID and staying in line."),
        ("students", "school", "Students", "Free school, speech, records and disability services."),
        ("veterans", "veterans", "Veterans and service members", "Your job, VA appeals, free help and leases."),
        ("disability", "service_dog", "People with disabilities", "Access, accommodations and service dogs."),
    ]
    sit = '<div class="grid">' + "".join(
        f'<a class="card" href="{s}.html"><div class="iconrow">{ic(i)}<h3>{t}</h3></div><p>{d}</p></a>' for s, i, t, d in situations) + "</div>"
    places = checklist([
        ("globe", "<strong>Everywhere in the US:</strong> the Constitution and federal law. These are the floor; no state can go below them."),
        ("map_pin", "<strong>Your state:</strong> its own constitution and laws can add more. Every situation page lists Ohio's, and more states are coming."),
        ("navigation", "<strong>Your city:</strong> many cities add protections, such as for sexual orientation in housing or for paid sick time. Check your city's code."),
        ("lock", "<strong>At the border and airport security:</strong> agents can search bags and devices with less cause than police need inside the country."),
        ("plane", "<strong>In another country:</strong> its laws apply to you. As a US citizen arrested abroad, you have the right to ask that the US embassy be told. See the " + ext("https://travel.state.gov/en/international-travel/help-abroad.html", "State Department's guide") + "."),
    ])
    idx = f"""
<section aria-labelledby="why-r" class="panel"><h2 id="why-r">Your rights are already yours</h2>
<p>Nobody hands you your rights. The Declaration of Independence calls them "unalienable." The Ninth Amendment says the rights written down are not the only ones you keep. Ohio's Constitution opens with the line that every person has "certain inalienable rights."</p>
<p>Laws don't create these rights. They write them down and set limits on what governments, landlords, employers and businesses can do to you. Each page below says what's yours, in plain words, and links to the law that backs it up.</p></section>
<section aria-labelledby="sit-h"><h2 id="sit-h">By situation</h2>{sit}</section>
<section aria-labelledby="pl-h"><h2 id="pl-h">By place: where you are changes what's covered</h2>{places}</section>
<section aria-labelledby="use-h"><h2 id="use-h">How to use a right</h2>{checklist([
 ("megaphone", "Name it out loud: \"I'm using my right to remain silent.\" Some rights only count once you say them."),
 ("document", "Put it in writing, keep copies, and note dates and names."),
 ("clock", "Watch the deadline. Many complaints must be filed within 30 days to a year."),
 ("rights_legal", "Get help free: " + ext("https://www.ohiolegalhelp.org/", "Ohio Legal Help") + " in Ohio, or dial <a href=\"tel:211\">211</a> and ask for legal aid anywhere."),
])}</section>
<p class="note">This is general information about the law, checked against the sources on each page. It isn't legal advice for your situation. For that, talk with a lawyer or legal aid.</p>
{checked([ext("https://www.archives.gov/founding-docs/declaration-transcript", "Declaration of Independence, National Archives"), amend(9), ohcon("1.1")])}
"""
    URLS.append(page("rights/index.html", "Your rights, in plain words | Earth Rules",
                     "Your rights by situation (police, patients, renters, workers, consumers, voters, students, veterans, disability) and by place, US and Ohio, each linked to the law.",
                     "EARTH RULES · YOUR RIGHTS", "Your rights.", "What's yours, wherever you are, and the law that says so.", idx))

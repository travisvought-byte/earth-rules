"""Practical life pages: money, help groups, coverage, papers, basics, work, rides, business,
"My year" printable checklists, how people work, and places (world, country, state). Imported by build.py."""


def build(page, ic, ext, checklist, checked, tiles, URLS):
    def layers(world, us, oh, world_h="Everywhere", us_h="In the United States", oh_h="In Ohio"):
        """Big picture first, then the country, then the state."""
        out = f'<section aria-labelledby="w-h"><h2 id="w-h">{ic("globe")} {world_h}</h2>{world}</section>'
        if us:
            out += f'<section aria-labelledby="u-h"><h2 id="u-h">{ic("map_pin")} {us_h}</h2>{us}</section>'
        if oh:
            out += f'<section aria-labelledby="o-h"><h2 id="o-h">{ic("map_pin")} {oh_h}</h2>{oh}</section>'
        return out

    def todo(items):
        return '<ul class="todo">' + "".join(f"<li>{t}</li>" for t in items) + "</ul>"

    def printbtn():
        return f'<p><button type="button" class="printbtn">{ic("printer")}<span>Print this page</span></button></p>'

    def tel(num, label=None):
        digits = "".join(c for c in num if c.isdigit())
        return f'<a href="tel:{digits}">{label or num}</a>'

    def call_tiles(items):
        """items: (href, icon, label, hint, css)"""
        return tiles(items)

    # ================= Money =================
    money = f"""
<section aria-labelledby="m0" class="panel"><h2 id="m0">The short version</h2>
<p>Money flows toward people who already have it. If you have money, you earn interest. If you need money, you pay interest. Most of the system is built on that one fact.</p>
<p>You can't change the system alone. You can stop paying it more than you have to.</p></section>
<section aria-labelledby="m1"><h2 id="m1">{ic("dollar")} Interest: the price of money</h2>
<p>Interest is rent on money. When you borrow, you pay rent. When you save, the bank pays you rent, usually far less than it charges.</p>
<p><strong>Compound interest</strong> means interest on top of interest. It works for you when you save and against you when you owe.</p>
<div class="grid">
<div class="stat"><span class="n">15 years</span>to pay off $3,000 on a credit card at 22% if you pay only the minimum. Interest: about $4,400.</div>
<div class="stat"><span class="n">26 months</span>to pay off the same $3,000 at $150 a month. Interest: about $770.</div>
<div class="stat"><span class="n">$69,000</span>is what $100 a month grows to in 30 years at 4% a year. You put in $36,000.</div>
</div>
<p class="note">The average credit card rate for people who carry a balance was about 22% in 2026, from the Federal Reserve. Our math assumes a minimum payment of the interest plus 1% of the balance, at least $25.</p></section>
<section aria-labelledby="m2"><h2 id="m2">{ic("chart")} Credit scores: a grade for how you pay</h2>
<p>Lenders, landlords and some employers look at a score built from your credit report. The FICO score weighs:</p>{checklist([
 ("clock", "<strong>Paying on time: about 35%.</strong> One payment 30 days late can hurt for years."),
 ("dollar", "<strong>How much you owe: about 30%.</strong> Using a small part of your limit helps."),
 ("calendar", "<strong>How long you've had credit: about 15%.</strong> Keep old cards open if they're free."),
 ("document", "<strong>New credit and the mix of credit: about 20%.</strong> Apply only when you need to."),
])}
<p>See your credit reports free every week at {ext("https://www.annualcreditreport.com/", "AnnualCreditReport.com")}, the only official site. Fix mistakes by disputing them with the credit bureau.</p></section>
<section aria-labelledby="m3"><h2 id="m3">{ic("no")} The traps</h2>{checklist([
 ("no", "<strong>Payday and title loans.</strong> A $15 fee for every $100 borrowed for two weeks works out to almost 400% a year, the CFPB says."),
 ("no", "<strong>Minimum payments.</strong> They're set so you stay in debt longer. Pay more than the minimum whenever you can."),
 ("no", "<strong>Overdraft fees.</strong> Turn off overdraft \"coverage\" so a card is declined instead of charged a fee."),
 ("no", "<strong>Rent-to-own and buy now, pay later.</strong> Add up the total before you sign. It's often far more than the price tag."),
 ("no", "<strong>Anything you don't understand.</strong> If someone can't explain where the money comes from in one sentence, keep your money."),
])}</section>
<section aria-labelledby="m4"><h2 id="m4">{ic("globe")} How the big system works</h2>
<p><strong>Banks make money by lending.</strong> When a bank makes a loan, it creates new money in your account. That's how most money comes to exist, the Bank of England explains.</p>
<p><strong>Central banks set the base price of money.</strong> In the US that's the Federal Reserve. When it raises rates, loans cost more for everyone. When prices rise faster than your pay, your money buys less. That's inflation.</p>
<p><strong>Wealth piles up at the top.</strong> In the US, the richest 1% of households held about a third of all wealth in 2026, by the Federal Reserve's own count. That's about as much as the bottom 90% combined.</p>
<p><strong>Every country works this way</strong>, with different rules for banks, debt and help. Your protections depend on where you live.</p></section>
<section aria-labelledby="m5"><h2 id="m5">{ic("yes")} What actually works</h2>{checklist([
 ("yes", "Keep a little cash for emergencies, even $20 a week. It's what keeps a flat tire from becoming a payday loan."),
 ("yes", "Pay the highest-interest debt first, and never miss a minimum."),
 ("yes", "Take free money: an employer's retirement match, tax credits like the Earned Income Tax Credit, and benefits you qualify for."),
 ("yes", "Call your lender before you miss a payment. Many have hardship plans they don't advertise."),
])}</section>
<section aria-labelledby="m6"><h2 id="m6">{ic("phone")} Free money help</h2>{checklist([
 ("phone", "<strong>Nonprofit credit counseling:</strong> " + tel("800-388-2227", "800-388-2227") + ", the " + ext("https://www.nfcc.org/", "National Foundation for Credit Counseling") + ". Free or low cost, and they work out payment plans."),
 ("rights_legal", "<strong>Complaints and debt collectors:</strong> the " + ext("https://www.consumerfinance.gov/complaint/", "Consumer Financial Protection Bureau") + ". See also <a href=\"rights/consumers.html\">your rights as a consumer</a>."),
 ("document", "<strong>Free tax help:</strong> " + ext("https://www.irs.gov/individuals/free-tax-return-preparation-for-qualifying-taxpayers", "IRS VITA") + " for people with low to moderate income, people with disabilities and people who speak limited English."),
 ("phone", "<strong>Anything else:</strong> dial <a href=\"tel:211\">211</a>."),
])}</section>
{checked([ext("https://fred.stlouisfed.org/series/TERMCBCCINTNS", "Federal Reserve G.19: credit card interest rate, accounts assessed interest"),
          ext("https://www.consumerfinance.gov/ask-cfpb/what-are-the-costs-and-fees-for-a-payday-loan-en-1589/", "CFPB: costs of a payday loan"),
          ext("https://www.myfico.com/credit-education/whats-in-your-credit-score", "myFICO: what's in your credit score"),
          ext("https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy", "Bank of England: money creation in the modern economy"),
          ext("https://fred.stlouisfed.org/series/WFRBST01134", "Federal Reserve DFA: share of net worth held by the top 1%"), ext("https://www.cbsnews.com/news/us-wealth-gap-widest-in-three-decades-federal-reserve", "CBS News: top 1% vs bottom 90%"),
          ext("https://www.annualcreditreport.com/", "AnnualCreditReport.com"), ext("https://www.nfcc.org/", "NFCC")])}
"""
    URLS.append(page("money.html", "How money works, and how it works against you | Earth Rules",
                     "Interest, compound interest, credit scores, debt traps and how the banking system works, in plain words, with free places to get help.",
                     "EARTH RULES · MONEY", "How money works.", "Interest, credit, debt and the system, in plain words. And where to get free help.", money))

    # ================= Help groups =================
    hg = f"""
<section aria-labelledby="g0"><h2 id="g0">Call now, free and private</h2>{call_tiles([
 ("tel:18006624357", "phone", "1-800-662-4357", "Drugs or alcohol help, 24/7", "tile-blue"),
 ("tel:988", "crisis", "988", "Crisis or thoughts of suicide", "tile-calm"),
 ("tel:18005899966", "dollar", "1-800-589-9966", "Gambling help in Ohio", ""),
 ("tel:18007848669", "no", "1-800-784-8669", "Quit smoking or vaping", ""),
])}</section>
<section aria-labelledby="g1" class="panel"><h2 id="g1">Addictions you can't afford</h2>
<p>An addiction is anything you keep doing after it starts costing you money, health, work or people. Alcohol, drugs, gambling, spending and nicotine are the common ones. It isn't a moral failing, and you don't have to hit bottom to get help.</p></section>
<section aria-labelledby="g2"><h2 id="g2">{ic("peer_support")} Groups that meet everywhere, free</h2>{checklist([
 ("peer_support", "<strong>Alcohol:</strong> " + ext("https://www.aa.org/", "Alcoholics Anonymous") + " meets in most towns worldwide and online."),
 ("peer_support", "<strong>Drugs:</strong> " + ext("https://na.org/", "Narcotics Anonymous") + ", any drug, including alcohol."),
 ("peer_support", "<strong>A science-based option:</strong> " + ext("https://smartrecovery.org/", "SMART Recovery") + ", for any addiction, with no higher power required."),
 ("dollar", "<strong>Gambling:</strong> " + ext("https://gamblersanonymous.org/", "Gamblers Anonymous") + "."),
 ("funding", "<strong>Spending and debt:</strong> " + ext("https://debtorsanonymous.org/", "Debtors Anonymous") + "."),
 ("heart", "<strong>Family and friends of someone drinking:</strong> " + ext("https://al-anon.org/", "Al-Anon") + " and Alateen."),
])}
<p>Meetings are free. You can sit in the back and just listen. Try a few different groups; each one feels different.</p></section>
{layers(checklist([
 ("search", "Treatment is real medicine. For opioids and alcohol, there are medicines that cut the risk of relapse and death. Ask a doctor."),
 ("clock", "Stopping heavy drinking or some drugs suddenly can be dangerous. Get medical help to stop safely."),
]), checklist([
 ("search", ext("https://findtreatment.gov/", "FindTreatment.gov") + ": every licensed treatment place, searchable by insurance and cost."),
 ("phone", "SAMHSA's helpline: " + tel("1-800-662-4357") + ", free, confidential, 24/7, in English and Spanish."),
 ("no", "Quitline for tobacco and vaping: " + tel("1-800-784-8669", "1-800-QUIT-NOW") + "."),
]), checklist([
 ("dollar", "Ohio's Problem Gambling Helpline: " + tel("1-800-589-9966") + ", 24/7."),
 ("medical", "Ohio Medicaid covers addiction treatment. See <a href=\"coverage.html\">health coverage</a>."),
 ("peer_support", "Dial <a href=\"tel:211\">211</a> for meetings and treatment near you."),
]))}
{checked([ext("https://www.samhsa.gov/find-help/helplines/national-helpline", "SAMHSA National Helpline"), ext("https://findtreatment.gov/", "FindTreatment.gov"),
          ext("https://pausebeforeyouplay.org/get-help/", "Ohio Problem Gambling Helpline"), ext("https://www.aa.org/", "AA"), ext("https://na.org/", "NA"),
          ext("https://smartrecovery.org/", "SMART Recovery"), ext("https://al-anon.org/", "Al-Anon"), ext("https://gamblersanonymous.org/", "GA"), ext("https://debtorsanonymous.org/", "DA")])}
"""
    URLS.append(page("help-groups.html", "Help groups for addiction: alcohol, drugs, gambling, spending | Earth Rules",
                     "Free help for addictions you can't afford: AA, NA, SMART Recovery, Gamblers Anonymous, Al-Anon, the SAMHSA helpline and Ohio's gambling helpline.",
                     "EARTH RULES · HELP GROUPS", "Help groups.", "Free, private help for drinking, drugs, gambling, spending and smoking.", hg))

    # ================= Health coverage =================
    cov = f"""
<section aria-labelledby="c0"><h2 id="c0">Which one is yours?</h2>{call_tiles([
 ("#medicaid", "dollar", "Medicaid", "Low income, any age", ""),
 ("#medicare", "clock", "Medicare", "65 and older, or disabled", ""),
 ("#aca", "shield", "Marketplace", "Buy your own plan", ""),
 ("#va", "veterans", "VA health", "Veterans", ""),
 ("#none", "medical", "No coverage", "Still get care", "tile-help"),
])}</section>
<section aria-labelledby="c1" class="panel"><h2 id="c1">{ic("globe")} Everywhere</h2>
<p>Most rich countries cover everyone through the government. The United States mixes government plans, job plans and plans you buy. If you're in another country, ask what its public health system covers; often it's more than you'd guess.</p></section>
<section aria-labelledby="medicaid-h" id="medicaid"><h2 id="medicaid-h">{ic("dollar")} Medicaid: for low income</h2>
<p>Run by each state with federal money. In Ohio it covers adults with low income, children, pregnant people, and people with disabilities.</p>{checklist([
 ("yes", "<strong>Covers:</strong> doctors, hospitals, prescriptions, mental health and addiction care, eye care, and rides to appointments in many cases."),
 ("yes", "<strong>Dental for adults in Ohio:</strong> checkups and cleanings, fillings and pulling teeth. Dentures need approval first. Your plan's handbook lists the limits."),
 ("search", "<strong>Find a dentist who takes it:</strong> call the member number on your Medicaid card and ask for three dentists taking new patients. Or try a " + ext("https://findahealthcenter.hrsa.gov/", "community health center") + "."),
 ("document", "<strong>Apply or renew:</strong> " + ext("https://benefits.ohio.gov/", "Ohio Benefits") + " or the Ohio Medicaid hotline, " + tel("800-324-8680") + ". Open every letter about renewal and answer by the date on it."),
])}</section>
<section aria-labelledby="medicare-h" id="medicare"><h2 id="medicare-h">{ic("clock")} Medicare: 65 and older</h2>
<p>Federal coverage for people 65 and older and some younger people with disabilities.</p>{checklist([
 ("medical", "<strong>Part A</strong> is hospital care. <strong>Part B</strong> is doctors and outpatient care. <strong>Part D</strong> is prescriptions."),
 ("no", "<strong>Original Medicare doesn't cover</strong> most dental care, eyeglasses or hearing aids. Many Medicare Advantage plans add some of these."),
 ("calendar", "<strong>Change plans</strong> each year from October 15 to December 7."),
 ("phone", "<strong>Free, unbiased help in Ohio:</strong> OSHIIP, " + tel("800-686-1578") + ". Compare doctors and plans at " + ext("https://www.medicare.gov/care-compare/", "Medicare Care Compare") + "."),
])}</section>
<section aria-labelledby="aca-h" id="aca"><h2 id="aca-h">{ic("shield")} The Marketplace: buy your own plan</h2>{checklist([
 ("calendar", "Sign up at " + ext("https://www.healthcare.gov/", "HealthCare.gov") + " from November 1 to January 15. Losing coverage, moving or having a baby lets you sign up within 60 days."),
 ("dollar", "Help paying depends on your income. The site shows your price before you pick."),
 ("yes", "Preventive care like checkups, many screenings and vaccines costs nothing extra on these plans."),
])}</section>
<section aria-labelledby="va-h" id="va"><h2 id="va-h">{ic("veterans")} VA health care</h2>{checklist([
 ("veterans", "Apply at " + ext("https://www.va.gov/health-care/apply-for-health-care-form-10-10ez/", "VA.gov") + " or call " + tel("877-222-8387") + "."),
 ("no", "VA dental is limited to some veterans, such as those rated 100% service-connected or with a service-connected dental problem."),
 ("yes", "If you're enrolled in VA health care, you can buy low-cost " + ext("https://www.va.gov/health-care/about-va-health-benefits/dental-care/dental-insurance/", "VA dental insurance") + "."),
 ("map_pin", "Find a VA clinic: " + ext("https://www.va.gov/find-locations/", "VA locations") + "."),
])}</section>
<section aria-labelledby="none-h" id="none"><h2 id="none-h">{ic("medical")} No coverage? You can still get care</h2>{checklist([
 ("medical", ext("https://findahealthcenter.hrsa.gov/", "Community health centers") + " charge on a sliding scale by income, including dental at many of them."),
 ("siren", "Emergency rooms must check and stabilize you even if you can't pay. See <a href=\"rights/patients.html\">your rights as a patient</a>."),
 ("dollar", "Hospitals run by nonprofits must have a financial assistance policy. Ask for it before you pay a big bill."),
])}</section>
{checked([ext("https://medicaid.ohio.gov/", "Ohio Department of Medicaid"), ext("https://www.medicare.gov/", "Medicare.gov"), ext("https://www.healthcare.gov/", "HealthCare.gov"),
          ext("https://www.va.gov/health-care/about-va-health-benefits/dental-care/", "VA dental care"), ext("https://findahealthcenter.hrsa.gov/", "HRSA Find a Health Center"),
          ext("https://insurance.ohio.gov/", "Ohio Department of Insurance (OSHIIP)")])}
"""
    URLS.append(page("coverage.html", "Health coverage explained: Medicaid, Medicare, Marketplace, VA | Earth Rules",
                     "How Medicaid, Medicare, Marketplace plans and VA health care work, what they cover (including adult dental in Ohio Medicaid), and how to find a provider.",
                     "EARTH RULES · HEALTH COVERAGE", "Health coverage.", "What each kind covers, and how to find a doctor or dentist who takes it.", cov))

    # ================= Papers =================
    pp = f"""
<section aria-labelledby="p0"><h2 id="p0">{ic("idcard")} Replace a lost ID or paper</h2>{layers(
 "<p>Every country has an office for birth records, ID cards and passports. Start with the one where you were born for a birth record, and the one where you live for an ID.</p>",
 checklist([
  ("idcard", "<strong>Social Security card:</strong> free, at " + ext("https://www.ssa.gov/number-card", "SSA.gov") + "."),
  ("globe", "<strong>Passport:</strong> " + ext("https://travel.state.gov/content/travel/en/passports.html", "State Department") + "."),
  ("veterans", "<strong>DD-214 for veterans:</strong> " + ext("https://www.archives.gov/veterans/military-service-records", "National Archives") + ", free."),
 ]),
 checklist([
  ("idcard", "<strong>State ID card:</strong> free for Ohioans 17 and older, at any " + ext("https://bmv.ohio.gov/", "Ohio BMV") + " office."),
  ("document", "<strong>Birth certificate:</strong> local health departments in Ohio can print one for anyone born in Ohio since 1908, usually for about $25. Call yours first."),
 ]), world_h="Everywhere", us_h="In the United States", oh_h="In Ohio")}</section>
<section aria-labelledby="p1"><h2 id="p1">{ic("document")} Keep your papers in one folder</h2>
<p>Print this list. Put each paper in one folder or envelope, and check it off. Keep it somewhere dry that you can grab fast.</p>{printbtn()}
<div class="printable">{todo([
 "Photo ID (driver's license or state ID)", "Birth certificate", "Social Security card", "Passport, if you have one",
 "Health insurance cards (Medicaid, Medicare, VA, job plan)", "List of your medicines and doctors", "Lease or deed",
 "Car title and registration", "Last 3 years of tax returns", "Recent pay stubs or benefit letters", "Bank account info (not passwords)",
 "DD-214 (veterans)", "Will, power of attorney, health care wishes", "Copies of all of the above, kept somewhere else",
])}
<h3>Important numbers</h3>
<table class="fill"><caption class="sr">Fill in your important numbers</caption><tr><th scope="col">Who</th><th scope="col">Name</th><th scope="col">Phone</th></tr>
{"".join(f'<tr><td>{w}</td><td></td><td></td></tr>' for w in ["Emergency contact", "Doctor", "Pharmacy", "Dentist", "Caseworker", "Landlord", "Work"])}</table></div></section>
{checked([ext("https://www.ssa.gov/number-card", "SSA: Social Security card"), ext("https://bmv.ohio.gov/", "Ohio BMV"),
          ext("https://odh.ohio.gov/know-our-programs/vital-statistics/", "Ohio Department of Health: vital statistics"), ext("https://www.columbus.gov/Services/Public-Health/Get-a-Birth-or-Death-Certificate", "Columbus Public Health: birth certificates"), ext("https://www.archives.gov/veterans/military-service-records", "National Archives: military records")])}
"""
    URLS.append(page("papers.html", "Replace your ID and keep your papers organized | Earth Rules",
                     "How to replace an ID, birth certificate or Social Security card, plus a printable checklist of papers to keep in one folder.",
                     "EARTH RULES · PAPERS", "Your papers.", "Replace what's lost, and keep the rest in one place.", pp))

    # ================= Basics =================
    bs = f"""
<section aria-labelledby="b0"><h2 id="b0">Tap what you need</h2>{tiles([
 ("#food", "food", "Food", "SNAP, WIC, food banks", ""),
 ("#heat", "housing", "Heat and lights", "Help with bills", ""),
 ("#phone", "phone", "Phone and internet", "Discounts", ""),
 ("#kids", "children", "Child care", "Help paying", ""),
 ("rides.html", "transportation", "Rides", "To work or the doctor", ""),
 ("papers.html", "idcard", "ID and papers", "Replace and keep", ""),
])}</section>
<section aria-labelledby="food-h" id="food"><h2 id="food-h">{ic("food")} Food</h2>{checklist([
 ("food", "<strong>SNAP</strong> puts money for groceries on a card each month. Apply in Ohio at " + ext("https://benefits.ohio.gov/", "Ohio Benefits") + "."),
 ("children", "<strong>WIC</strong> gives food, formula and support to pregnant people and children under 5. " + ext("https://www.fna.usda.gov/wic", "About WIC") + "."),
 ("map_pin", "<strong>Food banks and pantries</strong> give food free, no long forms. Dial <a href=\"tel:211\">211</a> or search " + ext("https://www.feedingamerica.org/find-your-local-foodbank", "Feeding America") + "."),
])}</section>
<section aria-labelledby="heat-h" id="heat"><h2 id="heat-h">{ic("housing")} Heat and lights</h2>{checklist([
 ("housing", "Every state runs a home energy program with federal money (LIHEAP)."),
 ("map_pin", "<strong>Ohio:</strong> HEAP gives a credit on your heating bill. Apply at " + ext("https://energyhelp.ohio.gov/", "energyhelp.ohio.gov") + " or call " + tel("800-282-0880") + "."),
 ("phone", "Before a shutoff, call your utility and ask for a payment plan. Most have one."),
])}</section>
<section aria-labelledby="phone-h" id="phone"><h2 id="phone-h">{ic("phone")} Phone and internet</h2>{checklist([
 ("phone", "<strong>Lifeline</strong> takes up to $9.25 a month off one phone or internet bill if you get SNAP, Medicaid, SSI, housing help or have low income. Apply at " + ext("https://www.lifelinesupport.org/", "LifelineSupport.org") + "."),
 ("search", "Many internet companies sell low-cost plans for families on benefits. Ask for their \"low-income plan\" by name."),
])}</section>
<section aria-labelledby="kids-h" id="kids"><h2 id="kids-h">{ic("children")} Child care</h2>{checklist([
 ("search", "Find licensed child care and help paying at " + ext("https://childcare.gov/", "ChildCare.gov") + "."),
 ("map_pin", "<strong>Ohio:</strong> your county Job and Family Services office handles publicly funded child care."),
])}</section>
{checked([ext("https://www.fna.usda.gov/snap", "USDA SNAP"), ext("https://www.fna.usda.gov/wic", "USDA WIC"), ext("https://www.occ.ohio.gov/factsheet/home-energy-assistance-program-heap", "Ohio Consumers' Counsel: HEAP"),
          ext("https://www.fcc.gov/lifeline-consumers", "FCC Lifeline"), ext("https://childcare.gov/", "ChildCare.gov")])}
"""
    URLS.append(page("basics.html", "Food, heat, phone and child care help | Earth Rules",
                     "Where to get help with food (SNAP, WIC, food banks), heating bills (HEAP), phone and internet (Lifeline) and child care.",
                     "EARTH RULES · BASICS", "Food, heat, phone, child care.", "The everyday help most people don't know they can get.", bs))

    # ================= Work =================
    wk = f"""
<section aria-labelledby="k0" class="panel"><h2 id="k0">Programs that are real</h2>
<p>These are run or funded by the government, cost you nothing, and lead to actual jobs. If a \"job\" asks you to pay first, cash a check for them or buy gift cards, it's a scam.</p></section>
{layers(checklist([
 ("wrench", "Skilled trades, health care and driving jobs are in demand almost everywhere. Training is often short and sometimes paid."),
 ("search", "Every country has a public job service. Search for its name plus \"employment service.\""),
]), checklist([
 ("map_pin", "<strong>American Job Centers:</strong> free career help, and training paid for by the WIOA program if you qualify. Find one at " + ext("https://www.careeronestop.org/LocalHelp/AmericanJobCenters/find-american-job-centers.aspx", "CareerOneStop") + "."),
 ("wrench", "<strong>Apprenticeships:</strong> get paid while you learn a trade. " + ext("https://www.apprenticeship.gov/", "Apprenticeship.gov") + "."),
 ("school", "<strong>Job Corps:</strong> free training, and often housing, for ages 16 to 24. " + ext("https://www.jobcorps.gov/", "JobCorps.gov") + "."),
 ("veterans", "<strong>Veterans:</strong> " + ext("https://www.va.gov/careers-employment/vocational-rehabilitation/", "VA Veteran Readiness and Employment") + " for service-connected disabilities, and priority service at every job center."),
]), checklist([
 ("search", "<strong>OhioMeansJobs:</strong> job listings, resume help and training money at " + ext("https://ohiomeansjobs.ohio.gov/", "OhioMeansJobs.com") + " and centers in every county."),
 ("service_dog", "<strong>Disability:</strong> " + ext("https://ood.ohio.gov/", "Opportunities for Ohioans with Disabilities") + " pays for training and job help. Apply online or call " + tel("800-282-4536") + "."),
]))}
{checked([ext("https://www.careeronestop.org/", "CareerOneStop (U.S. Department of Labor)"), ext("https://www.apprenticeship.gov/", "Apprenticeship.gov"),
          ext("https://www.jobcorps.gov/", "Job Corps"), ext("https://www.va.gov/careers-employment/vocational-rehabilitation/", "VA VR&amp;E"),
          ext("https://ohiomeansjobs.ohio.gov/", "OhioMeansJobs"), ext("https://ood.ohio.gov/", "OOD")])}
"""
    URLS.append(page("work.html", "Job programs that actually work | Earth Rules",
                     "Free, real job programs: American Job Centers, WIOA training, apprenticeships, Job Corps, VA Veteran Readiness and Employment, OhioMeansJobs and Ohio's disability job program.",
                     "EARTH RULES · WORK", "Find work.", "Free programs that lead to real jobs, and how to spot fake ones.", wk))

    # ================= Rides =================
    rd = f"""
{layers(checklist([
 ("transportation", "Buses and trains are the cheapest way to get around in most places. Ask about reduced fares for older people, people with disabilities and students."),
 ("peer_support", "Carpools and vanpools split the cost of a commute. Many cities and employers will match you with riders."),
]), checklist([
 ("transportation", "<strong>Reduced fares:</strong> bus and train systems that take federal money can charge older adults, people with disabilities and anyone with a Medicare card no more than half fare at off-peak times."),
 ("service_dog", "<strong>Paratransit:</strong> if a disability keeps you from using the bus, your transit system must offer door-to-door rides in the same area. Ask your transit agency to apply."),
 ("clock", "<strong>Older adults:</strong> the " + ext("https://eldercare.acl.gov/", "Eldercare Locator") + ", " + tel("800-677-1116") + ", finds senior ride programs near you."),
 ("veterans", "<strong>Veterans:</strong> many VA medical centers run free shuttles and van programs to appointments. Call your VA clinic."),
]), checklist([
 ("medical", "<strong>Medicaid rides:</strong> call the member number on your card at least two days ahead. Your county Job and Family Services office can also help."),
 ("phone", "Dial <a href=\"tel:211\">211</a> for local ride programs."),
]))}
{checked([ext("https://www.transit.dot.gov/are-transit-providers-required-offer-reduced-transit-fares-seniors-people-disabilities-or-medicare", "FTA: reduced fares for seniors, people with disabilities and Medicare cardholders"),
          ext("https://www.ecfr.gov/current/title-49/subtitle-A/part-37/subpart-F", "49 CFR Part 37, Subpart F: ADA paratransit"),
          ext("https://eldercare.acl.gov/", "Eldercare Locator"),
          ext("https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Managed_Care_Transportation_Resource_Guide_for_Practices_042024_Final.pdf", "Ohio Medicaid transportation guide")])}
"""
    URLS.append(page("rides.html", "Rides to work and appointments | Earth Rules",
                     "How to get a ride: reduced transit fares, ADA paratransit, Medicaid rides, senior and veteran ride programs, carpools and vanpools.",
                     "EARTH RULES · RIDES", "Getting around.", "Cheap and free rides to work, the doctor and the store.", rd))

    # ================= Business =================
    bz = f"""
<section aria-labelledby="z0" class="panel"><h2 id="z0">Step one: say what you sell, in one sentence</h2>
<p>A business is simple: someone pays you more for something than it costs you to make it. Everything else is detail.</p>
<p>Your <strong>value proposition</strong> is why a customer would pay you instead of doing nothing or going somewhere else. If you can't say it in one or two sentences, nobody will fund you. Not a bank, not an investor, not a grant. That's the first wall, and most people never get past it.</p></section>
<section aria-labelledby="z1"><h2 id="z1">{ic("bigarrow")} The path, in order</h2>
<ol class="steps">
<li><strong>Value proposition.</strong> For [who], who [have this problem], I [do this], unlike [what they do now].</li>
<li><strong>Customer.</strong> Name a real person who would buy it. Then ask them.</li>
<li><strong>How you make money.</strong> What do you charge, and how often?</li>
<li><strong>Costs.</strong> What does it cost to make, deliver and sell one? What does it cost each month to stay open?</li>
<li><strong>Plan.</strong> Only now write the business plan. Each part above becomes a page of it.</li>
</ol></section>
<section aria-labelledby="z2"><h2 id="z2">{ic("document")} Worksheet</h2>{printbtn()}
<div class="printable worksheet">
<p><strong>My value proposition</strong><br>For <span class="blank"></span> who <span class="blank"></span>,<br>I <span class="blank"></span>, unlike <span class="blank"></span>.</p>
<p><strong>One real customer I could call:</strong> <span class="blank wide"></span></p>
<p><strong>What I charge:</strong> <span class="blank"></span> &nbsp; <strong>How often:</strong> <span class="blank"></span></p>
<p><strong>Cost to make and deliver one:</strong> <span class="blank"></span></p>
<p><strong>Cost each month to stay open:</strong> <span class="blank"></span></p>
<p><strong>Sales I need each month to break even:</strong> (monthly cost) ÷ (price minus cost of one) = <span class="blank"></span></p>
</div></section>
<section aria-labelledby="z3"><h2 id="z3">{ic("phone")} Free help to get there</h2>{checklist([
 ("peer_support", ext("https://www.score.org/", "SCORE") + ": free mentors, many of them retired business owners."),
 ("map_pin", "Small Business Development Centers: free advisers who help with plans, numbers and loans. Ohio has them in every region. Find yours with the " + ext("https://www.sba.gov/local-assistance", "SBA's local help finder") + "."),
 ("veterans", "Veterans and military spouses: " + ext("https://www.sba.gov/tools/local-assistance/vboc", "Veterans Business Outreach Centers") + "."),
 ("book", "The " + ext("https://www.sba.gov/business-guide", "SBA business guide") + " walks through registering, licenses and taxes."),
])}</section>
{checked([ext("https://www.sba.gov/business-guide", "SBA business guide"), ext("https://www.sba.gov/local-assistance", "SBA local assistance"),
          ext("https://www.sba.gov/tools/local-assistance/vboc", "SBA: Veterans Business Outreach Centers"), ext("https://www.score.org/", "SCORE")])}
"""
    URLS.append(page("business.html", "Starting a business: value proposition first | Earth Rules",
                     "How a business works, what a value proposition is, a printable worksheet, and free help from SCORE, Small Business Development Centers and the SBA.",
                     "EARTH RULES · BUSINESS", "Start a business.", "Say what you sell in one sentence. Then everything else.", bz))

    # ================= My year =================
    common_money = ["File taxes by April 15 (free help: VITA)", "Check your 3 credit reports, free", "Review insurance at open enrollment",
                    "Put something in emergency savings"]
    common_home = ["Test smoke and carbon monoxide alarms", "Change the furnace filter", "Renew car registration and check tires",
                   "Update your address everywhere if you moved"]
    bands = [
        ("18-29", "Ages 18 to 29", ["Dentist checkup and cleaning", "Checkup with a doctor or clinic", "Ask which vaccines you're due for",
                                     "Eye exam if you have trouble seeing"],
         ["Register to vote", "Men 18 to 25: register with Selective Service", "Start retirement savings at your first job",
          "Get your own health insurance by 26"]),
        ("30-39", "Ages 30 to 39", ["Dentist checkup and cleaning", "Checkup with blood pressure check", "Ask which vaccines you're due for",
                                     "Cervical cancer screening if due"],
         ["Life insurance if anyone depends on you", "Write a simple will", "Raise retirement savings when pay goes up"]),
        ("40-49", "Ages 40 to 49", ["Dentist checkup and cleaning", "Yearly checkup and blood pressure", "Eye exam (baseline at 40)",
                                     "Mammogram every 2 years for women from 40", "Colorectal screening from 45"],
         ["Check retirement savings are on track", "Update will and beneficiaries"]),
        ("50-64", "Ages 50 to 64", ["Dentist checkup and cleaning", "Yearly checkup", "Colorectal screening", "Eye exam",
                                     "Ask about shingles and other vaccines"],
         ["Plan for Medicare at 65", "Check your Social Security statement at ssa.gov", "Power of attorney and health care wishes"]),
        ("65", "Age 65 and older", ["Medicare yearly wellness visit (free)", "Dentist checkup and cleaning", "Eye and hearing check",
                                     "Ask about fall prevention", "Review all medicines with a pharmacist"],
         ["Compare Medicare plans October 15 to December 7", "Keep will and health care wishes current"]),
    ]
    restart = checklist([
        ("medical", "<strong>No dentist in 5 years?</strong> Book one cleaning. Ohio Medicaid covers adults. Community health centers charge by income."),
        ("medical", "<strong>No checkup in 5 years?</strong> Book one visit. Most plans cover a yearly checkup at no extra cost."),
        ("document", "<strong>Haven't filed taxes in years?</strong> You can still file. Refunds from the last 3 years can still be claimed."),
        ("chart", "<strong>Never looked at your credit?</strong> Pull your reports today. It doesn't hurt your score."),
    ])
    yr_tiles = []
    for slug, label, health, life in bands:
        body = f"""
{printbtn()}
<div class="printable">
<h2>{ic("medical")} Health</h2>{todo(health)}
<h2>{ic("dollar")} Money</h2>{todo(common_money)}
<h2>{ic("housing")} Home and car</h2>{todo(common_home)}
<h2>{ic("calendar")} This stage of life</h2>{todo(life)}
</div>
<section aria-labelledby="r-h"><h2 id="r-h">{ic("reuse")} Behind? Start here</h2>{restart}</section>
<p class="note">General guidance. Your doctor or dentist may tell you to come more or less often. Screenings by age are on <a href="../checkups.html">Checkups</a>.</p>
{checked([ext("https://www.uspreventiveservicestaskforce.org/uspstf/recommendation-topics/uspstf-a-and-b-recommendations", "USPSTF A and B recommendations"),
          ext("https://www.cdc.gov/vaccines/", "CDC vaccines"), ext("https://www.irs.gov/", "IRS"), ext("https://www.annualcreditreport.com/", "AnnualCreditReport.com")])}
"""
        URLS.append(page(f"my-year/{slug}.html", f"My year checklist: {label.lower()} | Earth Rules",
                         f"A printable one-page checklist of what to check and keep up this year at {label.lower()}: health, money, home and car.",
                         "EARTH RULES · MY YEAR", f"My year: {label.lower()}.", "Print it. Check things off. Do it again next year.", body))
        yr_tiles.append((f"{slug}.html", "calendar", label.replace("Ages ", "").replace("Age ", ""), "Print my list", ""))
    URLS.append(page("my-year/index.html", "My year: printable checklists by age | Earth Rules",
                     "Printable one-page checklists by age: the checkups, money tasks and upkeep to do each year, and where to start if you're years behind.",
                     "EARTH RULES · MY YEAR", "My year.", "Pick your age. Print one page. Check it off.",
                     f'<section aria-labelledby="y0"><h2 id="y0">Pick your age</h2>{tiles(yr_tiles)}</section>'
                     f'<section aria-labelledby="y1"><h2 id="y1">{ic("reuse")} Behind? Start here</h2>{restart}</section>'))

    # ================= How people work =================
    hw = f"""
<section aria-labelledby="h0" class="panel"><h2 id="h0">People are built for groups</h2>
<p>For most of history, being part of a group meant staying alive. That wiring is still in us. It makes us loyal, generous and brave. It also makes us easy to fool.</p></section>
<section aria-labelledby="h1"><h2 id="h1">{ic("peer_support")} Teams and tribes</h2>
<p>Sports fans, neighborhoods, churches, political parties and fan clubs all give people a team. Studies going back to the 1970s found people favor their own group even when the groups are made up on the spot by a coin toss.</p>
<p>That's normal. It turns into a problem when your team decides what's true, or who counts as a person.</p></section>
<section aria-labelledby="h2"><h2 id="h2">{ic("megaphone")} Us versus them, and who profits</h2>{checklist([
 ("megaphone", "Anger and fear keep people watching and clicking, so news, ads and social media feeds lean into them."),
 ("megaphone", "Politicians, sellers and scammers all use the same move: name an enemy, then ask you to trust them."),
 ("yes", "Ask: who gains if I believe this? Who's left out of the story? Would I believe it if the other side said it?"),
])}</section>
<section aria-labelledby="h3"><h2 id="h3">{ic("dollar")} Gambling</h2>
<p>Every casino game, lottery and sports bet is priced so the house wins over time. Betting apps make it fast, private and always on, and ads link it to being a real fan. A win now and then is part of the design; it keeps you playing.</p>
<p>If you bet more than you planned, chase losses, or hide it, that's the sign. <a href="help-groups.html">Help groups</a> are free.</p></section>
<section aria-labelledby="h4"><h2 id="h4">{ic("no")} Alcohol</h2>
<p>Many places treat drinking as normal or even expected. It's also one of the leading causes of preventable death in the US, and the US Surgeon General says it raises the risk of several cancers. Less is safer, and not drinking is a normal choice. If it's costing you, <a href="help-groups.html">help groups</a> are free.</p></section>
<section aria-labelledby="h6"><h2 id="h6">{ic("megaphone")} Go deeper</h2>{tiles([
 ("manipulation.html", "megaphone", "Spot the trick", "Tricks, propaganda, biases", ""),
 ("scams.html", "siren", "Scams", "Spot and report", ""),
 ("attention.html", "device", "Phone traps", "Why you can't stop", ""),
 ("disagree.html", "chat_q", "Disagree well", "Without a fight", ""),
])}</section>
<section aria-labelledby="h5"><h2 id="h5">{ic("globe")} Culture: the unwritten rules</h2>
<p>Every place has rules nobody writes down: how close to stand, whether to look people in the eye, how much to tip, what time \"on time\" means, how direct to be, what you can joke about. None of them is the right way. They're just the local way.</p>{checklist([
 ("search", "When you're new somewhere, watch first. Do what people around you do."),
 ("chat_q", "Ask. \"How do people usually do this here?\" is a respectful question almost everywhere."),
 ("heart", "Assume good intent. Most clashes are two sets of rules, not two bad people."),
])}
<p>The <a href="places/index.html">places</a> pages note what changes where you are.</p></section>
{checked([ext("https://www.cdc.gov/alcohol/facts-stats/", "CDC: alcohol facts and stats"),
          ext("https://www.hhs.gov/surgeongeneral/reports-and-publications/alcohol-cancer/index.html", "US Surgeon General: alcohol and cancer risk advisory"),
          ext("https://www.simplypsychology.org/social-identity-theory.html", "Social identity theory (Tajfel and Turner)")])}
"""
    URLS.append(page("how-people-work.html", "How people work: tribes, us vs them, gambling, alcohol, culture | Earth Rules",
                     "Why people form teams and tribes, how us-versus-them gets used on you, how gambling and alcohol culture work, and the unwritten rules that change from place to place.",
                     "EARTH RULES · HOW PEOPLE WORK", "How people work.", "Teams, tribes, betting, drinking and the unwritten rules, without the preaching.", hw))

    # ================= Places: world -> country -> state =================
    pl = f"""
<section aria-labelledby="pl0"><h2 id="pl0">Where are you?</h2>{tiles([
 ("world.html", "globe", "Anywhere", "What's true everywhere", ""),
 ("us.html", "map_pin", "United States", "Federal rules", ""),
 ("../states/ohio.html", "map_pin", "Ohio", "State rules", ""),
])}</section>
<section aria-labelledby="pl1"><h2 id="pl1">How this guide is built</h2>
<p>Every section starts with what's true everywhere. Then it narrows to your country, then your state or province. The United States and Ohio come first. More countries and states are added one at a time, each checked against that place's own official pages.</p></section>
"""
    URLS.append(page("places/index.html", "Where you are: world, country, state | Earth Rules",
                     "Pick your place. Earth Rules starts with what's true everywhere, then your country, then your state. US and Ohio first.",
                     "EARTH RULES · PLACES", "Where you are.", "Start with the whole world. Then your country. Then your state.", pl))

    wd = f"""
<section aria-labelledby="wd0"><h2 id="wd0">{ic("siren")} Emergency numbers</h2>
<table><caption>The number to call for police, fire or ambulance</caption><tr><th scope="col">Where</th><th scope="col">Number</th></tr>
<tr><td>United States, Canada and most of the Americas</td><td><a href="tel:911">911</a></td></tr>
<tr><td>European Union (works in every member country)</td><td><a href="tel:112">112</a></td></tr>
<tr><td>United Kingdom</td><td><a href="tel:999">999</a> or <a href="tel:112">112</a></td></tr>
<tr><td>Australia</td><td><a href="tel:000">000</a></td></tr>
<tr><td>India</td><td><a href="tel:112">112</a></td></tr></table>
<p>Most mobile phones will connect 112 or 911 to local emergency services in many countries, but don't count on it. Look up the number when you arrive.</p></section>
<section aria-labelledby="wd1"><h2 id="wd1">{ic("globe")} What changes from country to country</h2>{checklist([
 ("medical", "<strong>Health care:</strong> most rich countries cover everyone through a public system. Find out how to see a doctor before you need one."),
 ("rights_legal", "<strong>Your rights:</strong> the local law applies to you, even as a visitor. If you're arrested abroad, you can ask that your country's embassy be told."),
 ("transportation", "<strong>Driving:</strong> which side of the road, whether your license works, and the drinking limit."),
 ("dollar", "<strong>Money:</strong> tipping, taxes in the price or added at the register, and how people pay."),
 ("peer_support", "<strong>Manners:</strong> greetings, personal space, time and how direct people are. See " + "<a href=\"../how-people-work.html\">how people work</a>."),
])}</section>
<section aria-labelledby="wd2"><h2 id="wd2">{ic("idcard")} Countries in this guide</h2><p><a href="us.html">United States</a>. More are on the way.</p></section>
{checked([ext("https://digital-strategy.ec.europa.eu/en/policies/112", "European Union: 112"),
          ext("https://www.gov.uk/guidance/999-and-112-the-uks-national-emergency-numbers", "GOV.UK: 999 and 112"),
          ext("https://www.triplezero.gov.au/", "Triple Zero (Australia)"), ext("https://112.gov.in/", "India: 112"),
          ext("https://travel.state.gov/helpabroad", "U.S. State Department: help abroad")])}
"""
    URLS.append(page("places/world.html", "What's true everywhere | Earth Rules",
                     "The big picture that holds in every country: emergency numbers around the world, and what changes from place to place.",
                     "EARTH RULES · THE WORLD", "Everywhere.", "What holds anywhere on Earth, and what changes when you cross a border.", wd))

    us = f"""
<section aria-labelledby="us0"><h2 id="us0">{ic("map_pin")} The federal layer</h2>
<p>Federal law covers everyone in all 50 states. States can add more protection but can't take away what federal law gives you.</p>{tiles([
 ("../rights/index.html", "rights_legal", "Rights", "Federal and state", ""),
 ("../coverage.html", "medical", "Health coverage", "Medicaid, Medicare, VA", ""),
 ("../taxes.html", "document", "Taxes", "Federal return", ""),
 ("../work.html", "wrench", "Work", "Job programs", ""),
 ("../calendar.html", "calendar", "What's due", "Year round", ""),
])}</section>
<section aria-labelledby="us1"><h2 id="us1">{ic("map_pin")} States</h2>{tiles([
 ("../states/ohio.html", "map_pin", "Ohio", "Ready", ""),
])}<p>More states are being added one at a time.</p></section>
<section aria-labelledby="us2"><h2 id="us2">{ic("phone")} Numbers that work anywhere in the US</h2>{checklist([
 ("siren", "<a href=\"tel:911\">911</a>: police, fire, ambulance."),
 ("crisis", "<a href=\"tel:988\">988</a>: Suicide and Crisis Lifeline, call or text. Veterans press 1."),
 ("phone", "<a href=\"tel:211\">211</a>: food, rent, bills, rides and local programs."),
 ("phone", tel("1-800-662-4357") + ": drug and alcohol treatment referrals."),
])}</section>
"""
    URLS.append(page("places/us.html", "United States: the federal rules | Earth Rules",
                     "The federal layer of Earth Rules: rights, health coverage, taxes, work and the national help numbers, then each state.",
                     "EARTH RULES · UNITED STATES", "United States.", "What's the same in every state, and links to each state.", us))

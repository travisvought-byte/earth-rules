"""Know-how pages: manipulation, scams, attention traps, disagreeing well, fine print,
when someone dies, and the body basics (sleep, food, boredom). Imported by build.py."""


def build(page, ic, ext, checklist, checked, tiles, URLS):
    def tel(num, label=None):
        digits = "".join(c for c in num if c.isdigit())
        return f'<a href="tel:{digits}">{label or num}</a>'

    def tricks(items):
        """items: (icon, name, what it looks like, defense). One card per trick, so each can be spotted and named."""
        return '<ul class="tricks">' + "".join(
            f'<li>{ic(i)}<div><h3>{n}</h3><p>{w}</p><p class="def"><strong>Your move:</strong> {d}</p></div></li>'
            for i, n, w, d in items) + "</ul>"

    # ================= Manipulation =================
    mp = f"""
<section aria-labelledby="mm0" class="panel"><h2 id="mm0">Name it and it loses power</h2>
<p>Everyone uses these tricks: sellers, scammers, politicians, preachers, bosses, friends and you. Most of the time nobody plans it. Once you can name a trick, it's much harder to fall for it.</p></section>
<section aria-labelledby="mm1"><h2 id="mm1">{ic("store")} Persuasion tricks</h2>{tricks([
 ("clock", "Fake urgency", "\"Today only.\" \"Only 2 left.\" A countdown clock. Rushing you stops you from thinking or asking anyone.", "Anything real will still be there tomorrow. Sleep on it."),
 ("dollar", "Scarcity", "Things seem worth more when there's less of them, even when the shortage is made up.", "Ask what it's worth to you if there were a thousand of them."),
 ("heart", "Reciprocity", "A free gift, sample or favor makes you feel you owe something back.", "You can say thank you and still say no."),
 ("idcard", "Authority", "Uniforms, titles, logos and \"experts say\" make people obey without checking.", "Ask what the person actually knows, and who pays them."),
 ("peer_support", "Social proof", "\"Everyone's buying it.\" Fake reviews, paid crowds and follower counts.", "Ask how many people, and who counted."),
 ("yes", "Foot in the door", "A small yes first, then a bigger ask. People want to stay consistent with what they already agreed to.", "Each new ask is a new decision."),
])}</section>
<section aria-labelledby="mm2"><h2 id="mm2">{ic("megaphone")} Propaganda moves</h2>{tricks([
 ("no", "Us versus them", "Name an enemy group and blame them for your problems. The fastest way to win loyalty.", "Ask whether the group is really one thing, and who gains if you hate it."),
 ("megaphone", "Repetition", "Say it again and again. Things we hear often start to feel true, even when they aren't.", "Ask where you first heard it, and whether anyone showed proof."),
 ("siren", "Fear", "Make people scared enough to stop asking questions.", "Scared is when to slow down, not speed up."),
 ("chat_q", "Name-calling and labels", "A nickname or label replaces an argument.", "Ask what the person actually said or did."),
 ("sliders", "False choice", "\"You're either with us or against us.\" Only two options, when there are many.", "Ask what the third and fourth options are."),
 ("search", "Cherry-picking", "Only the facts that help, none that hurt.", "Ask what's been left out."),
 ("reuse", "Whataboutism", "Answering a question by pointing at someone else's bad act.", "Both can be wrong. Bring it back to the question."),
])}</section>
<section aria-labelledby="mm3"><h2 id="mm3">{ic("chart")} Shortcuts our brains take</h2>
<p>These are called cognitive biases. Everyone has them. They save time and they cost money.</p>{tricks([
 ("search", "Confirmation bias", "We notice what fits what we already believe and skip what doesn't.", "Look for the best case against your view."),
 ("dollar", "Sunk cost", "\"I've already put so much into it.\" Staying in a bad job, deal or relationship because of what's already spent.", "What's spent is gone either way. Decide from today forward."),
 ("no", "Loss aversion", "Losing $100 feels about twice as bad as winning $100 feels good, so we take bad bets to avoid a loss.", "Ask what you'd choose if you were starting fresh."),
 ("idcard", "Anchoring", "The first number you hear sets the range. That's why sticker prices are high.", "Find out the real price before you hear theirs."),
 ("siren", "Availability", "Whatever's on the news feels more common than it is.", "Look up the actual numbers."),
 ("heart", "Halo effect", "Good-looking, confident or famous people seem right about everything.", "Judge the claim, not the person."),
])}</section>
<section aria-labelledby="mm4"><h2 id="mm4">{ic("peer_support")} Groups, faith and why minds don't change</h2>
<p>People hold beliefs that tie them to their family, faith, team or party. Changing one of those beliefs can feel like leaving the group, so the mind protects it. Facts rarely change someone's mind in one conversation; studies find people do shift a little when the facts don't threaten who they are.</p>{checklist([
 ("peer_support", "Every group, religious or not, has insiders and outsiders. Notice when a rule applies only to them."),
 ("chat_q", "If you want to change a mind, start with what you share, ask questions, and give the person a way to save face."),
 ("heart", "If you want to keep your own mind open, say out loud: \"I might be wrong about this.\" See <a href=\"disagree.html\">how to disagree well</a>."),
])}</section>
<section aria-labelledby="mm5"><h2 id="mm5">{ic("globe")} Strange things people do</h2>{checklist([
 ("peer_support", "<strong>Going along with the room.</strong> In the 1950s Asch experiments, many people gave an answer they could see was wrong because everyone else did."),
 ("idcard", "<strong>Obeying orders.</strong> In Milgram's experiments, most people kept giving what they believed were painful shocks because a man in a lab coat told them to."),
 ("siren", "<strong>The bystander effect.</strong> The more people who see an emergency, the less likely any one of them is to help. If you need help, point at one person and tell them what to do."),
 ("reuse", "<strong>Liking what's familiar.</strong> We tend to like things more just because we've seen them before. That's why ads repeat."),
 ("wrench", "<strong>Valuing what we built.</strong> People value things more when they put work into them, even flat-pack furniture."),
])}</section>
{checked([ext("https://www.simplypsychology.org/asch-conformity.html", "Asch conformity experiments"), ext("https://www.simplypsychology.org/milgram.html", "Milgram obedience experiments"),
          ext("https://www.simplypsychology.org/bystander-effect.html", "The bystander effect"), ext("https://www.simplypsychology.org/confirmation-bias.html", "Confirmation bias"),
          ext("https://www.influenceatwork.com/7-principles-of-persuasion/", "Cialdini: principles of persuasion"),
          ext("https://www.britannica.com/topic/propaganda", "Britannica: propaganda"),
          ext("https://link.springer.com/article/10.1007/s11109-018-9443-y", "Wood and Porter (2019): factual corrections rarely backfire")])}
"""
    URLS.append(page("manipulation.html", "Spot the trick: manipulation, propaganda and biases | Earth Rules",
                     "Persuasion tricks, propaganda moves, cognitive biases like sunk cost and loss aversion, why beliefs resist change, and the strange things people do in groups.",
                     "EARTH RULES · SPOT THE TRICK", "Spot the trick.", "The tricks people use on you, and on themselves. Name it and it stops working.", mp))

    # ================= Scams =================
    sc = f"""
<section aria-labelledby="s0"><h2 id="s0">The 4 signs of almost every scam</h2>{tiles([
 ("#signs", "siren", "Rush", "Act now or else", "tile-help"),
 ("#signs", "lock", "Secret", "Don't tell anyone", "tile-help"),
 ("#signs", "dollar", "Odd payment", "Gift cards, wire, crypto, cash", "tile-help"),
 ("#signs", "idcard", "Fake official", "Government, bank, family", "tile-help"),
])}</section>
<section aria-labelledby="signs-h" id="signs"><h2 id="signs-h">{ic("no")} Common scams</h2>{tricks([
 ("idcard", "Government impostor", "A call or text from the \"IRS,\" Social Security or police says you owe money or will be arrested.", "Hang up. Agencies send letters first and never demand gift cards. Call the agency's number yourself."),
 ("peer_support", "Grandkid or family emergency", "\"Grandma, I'm in jail, please don't tell Mom.\" Sometimes the voice is faked with AI.", "Hang up and call your grandkid or their parent at a number you know. Agree on a family code word."),
 ("heart", "Romance", "Someone you met online is lovely, can never video chat, and soon needs money for a ticket, a bill or an \"investment.\"", "Never send money to someone you haven't met in person."),
 ("wrench", "Fake job", "A job that pays well for little work, hires you without an interview, then sends a check and asks you to send some back.", "A real employer never asks you to pay or forward money."),
 ("link", "Phishing", "A text or email with a link: a package problem, a locked account, a refund.", "Don't tap the link. Open the app or type the website yourself."),
 ("device", "Tech support", "A pop-up or call says your computer has a virus and asks for remote access.", "Close it. Real companies don't call you about viruses."),
])}</section>
<section aria-labelledby="s2"><h2 id="s2">{ic("phone")} If it happened, report it</h2>{checklist([
 ("siren", "<strong>Call your bank first</strong> if money left your account. The faster, the better the chance of stopping it."),
 ("document", "<strong>Everyone:</strong> " + ext("https://reportfraud.ftc.gov/", "ReportFraud.ftc.gov") + "."),
 ("device", "<strong>Online scams:</strong> the FBI's " + ext("https://www.ic3.gov/", "IC3") + "."),
 ("clock", "<strong>Age 60 and older:</strong> National Elder Fraud Hotline, " + tel("833-372-8311") + "."),
 ("text_msg", "<strong>Scam texts:</strong> forward them to 7726 (SPAM), then delete."),
 ("map_pin", "<strong>Ohio:</strong> the Ohio Attorney General, " + tel("800-282-0515") + "."),
])}
<p>Being scammed isn't stupid. These are run by professionals who do it all day. Telling someone is how the next person is saved.</p></section>
{checked([ext("https://www.ftc.gov/news-events/news/press-releases/2025/03/new-ftc-data-show-big-jump-reported-losses-fraud-125-billion-2024", "FTC: $12.5 billion lost to fraud in 2024"),
          ext("https://reportfraud.ftc.gov/", "ReportFraud.ftc.gov"), ext("https://www.ic3.gov/", "FBI IC3"),
          ext("https://ovc.ojp.gov/program/stop-elder-fraud/providing-help-restoring-hope", "National Elder Fraud Hotline"),
          ext("https://www.ohioattorneygeneral.gov/", "Ohio Attorney General")])}
"""
    URLS.append(page("scams.html", "Scams: how to spot them and where to report | Earth Rules",
                     "The four signs of a scam, the most common ones (government impostor, grandkid, romance, fake job, phishing, tech support), and where to report each.",
                     "EARTH RULES · SCAMS", "Scams.", "Rush, secret, odd payment, fake official. Spot one and you've spotted them all.", sc))

    # ================= Attention traps =================
    at = f"""
<section aria-labelledby="a0" class="panel"><h2 id="a0">You're not the customer</h2>
<p>Free apps make money from ads, and ads pay for time. So the apps are built to keep you looking as long as possible. That's not a flaw. It's the business.</p></section>
<section aria-labelledby="a1"><h2 id="a1">{ic("device")} The traps</h2>{tricks([
 ("reuse", "Endless scroll and autoplay", "No bottom to the page and the next video starts on its own, so there's never a natural place to stop.", "Decide when you'll stop before you start. Set a timer."),
 ("dollar", "Slot-machine rewards", "Pull to refresh, and sometimes there's something good. Rewards that come at random keep people pulling, like a slot machine.", "Turn off pull-to-refresh habits: check at set times."),
 ("siren", "Outrage", "Posts with angry, moral words spread further. One study found each added moral-emotional word raised sharing by about 20%.", "If a post makes you furious, wait before you share it."),
 ("phone", "Notifications", "Red dots and buzzes are built to pull you back in.", "Turn off every notification that isn't from a real person."),
 ("search", "The algorithm", "The feed shows what kept you watching last time, not what's true or good for you. Over time it can narrow what you see.", "Follow people on purpose, and use a chronological feed where you can."),
])}</section>
<section aria-labelledby="a2"><h2 id="a2">{ic("yes")} Small fixes that work</h2>{checklist([
 ("clock", "Use the screen time limits built into your phone."),
 ("device", "Keep the phone out of the bedroom at night. Use a cheap alarm clock."),
 ("sliders", "Move the apps that eat your time off the home screen."),
])}</section>
{checked([ext("https://www.pnas.org/doi/10.1073/pnas.1618923114", "Brady and others (2017): emotion shapes the spread of moralized content"),
          ext("https://www.hhs.gov/surgeongeneral/reports-and-publications/youth-mental-health/social-media/index.html", "US Surgeon General: social media and youth mental health")])}
"""
    URLS.append(page("attention.html", "Attention traps: why your phone is hard to put down | Earth Rules",
                     "How apps keep you scrolling: endless feeds, random rewards, outrage, notifications and algorithms, and the small fixes that work.",
                     "EARTH RULES · ATTENTION", "Attention traps.", "Why it's hard to put the phone down, and how to win some time back.", at))

    # ================= Disagree well =================
    dg = f"""
<section aria-labelledby="d0" class="panel"><h2 id="d0">The goal is to understand, not to win</h2>
<p>You'll rarely change a mind by beating it. You can understand someone, and be understood, which is what makes change possible later.</p></section>
<section aria-labelledby="d1"><h2 id="d1">{ic("chat_q")} How to do it</h2><ol class="steps">
<li><strong>Steelman first.</strong> Say their view back in its strongest form, until they say \"yes, that's it.\" The opposite of a straw man.</li>
<li><strong>Ask, don't tell.</strong> \"What makes you sure?\" \"What would change your mind?\" Questions open people up; statements shut them.</li>
<li><strong>Find the shared goal.</strong> Most fights are about how, not what. Safe kids, fair pay, a working town.</li>
<li><strong>Separate facts from values.</strong> Facts can be looked up. Values are choices. Know which one you're arguing about.</li>
<li><strong>Pick the moment.</strong> Not in front of a crowd, not online, not when anyone's hungry, drunk or angry.</li>
</ol></section>
<section aria-labelledby="d2"><h2 id="d2">{ic("reuse")} Changing your mind without losing face</h2>{checklist([
 ("yes", "\"I hadn't thought of that.\""),
 ("yes", "\"You've changed my mind on part of this.\""),
 ("yes", "\"I learned something new, so I see it differently now.\""),
 ("heart", "When someone else changes their mind, thank them. Don't say \"I told you so.\" Make it easy, and they'll do it again."),
])}</section>
<section aria-labelledby="d3"><h2 id="d3">{ic("no")} Signs it's not a real argument</h2>{checklist([
 ("no", "Name-calling, or arguing about the person instead of the point."),
 ("no", "The goalposts keep moving no matter what you show."),
 ("no", "Threats or yelling. You can leave. \"Let's pick this up another time\" is a full sentence."),
])}
<p>More on why people dig in: <a href="manipulation.html">spot the trick</a> and <a href="how-people-work.html">how people work</a>.</p></section>
"""
    URLS.append(page("disagree.html", "How to disagree well | Earth Rules",
                     "How to argue without a fight: steelmanning, asking questions, finding shared goals, and changing your mind without losing face.",
                     "EARTH RULES · DISAGREE WELL", "Disagree well.", "Understand first. Then be understood. Winning is optional.", dg))

    # ================= Fine print =================
    fp = f"""
<section aria-labelledby="fp0" class="panel"><h2 id="fp0">You can always ask for time</h2>
<p>You have the right to read anything before you sign it, take it home, and ask someone else to read it. If they won't let you, that tells you something.</p></section>
<section aria-labelledby="fp1"><h2 id="fp1">{ic("search")} What to look for</h2>{tricks([
 ("reuse", "Auto-renewal", "Free trials that turn into monthly charges, and subscriptions that renew every year.", "Put the cancel date in your calendar the day you sign up."),
 ("rights_legal", "Arbitration clauses", "You agree not to sue in court or join a class action. Disputes go to a private arbitrator instead, often chosen by the company.", "Look for an opt-out window, often 30 days, and use it."),
 ("dollar", "Fees and penalties", "Late fees, early-cancel fees, \"processing\" fees and fees for paying by phone.", "Add up the total cost, not the monthly price."),
 ("housing", "Leases", "Who fixes what, when rent can go up, notice to move out, and what comes out of the deposit.", "Take dated photos when you move in. See <a href=\"rights/tenants.html\">your rights as a renter</a>."),
 ("idcard", "Co-signing", "If you co-sign, you owe the whole debt if they don't pay.", "Only co-sign what you could afford to pay yourself."),
 ("lock", "Privacy", "What they collect about you and who they sell it to.", "Pick the most private settings."),
])}</section>
<section aria-labelledby="fp2"><h2 id="fp2">{ic("clock")} Changed your mind?</h2>{checklist([
 ("map_pin", "<strong>US:</strong> the FTC's Cooling-Off Rule gives you 3 days to cancel many sales made at your home, or at a temporary location like a hotel or fair."),
 ("map_pin", "<strong>Ohio:</strong> Ohio law also gives you until midnight of the third business day to cancel a sale made at your home."),
 ("document", "Cancel in writing, keep a copy, and note the date."),
])}</section>
{checked([ext("https://consumer.ftc.gov/articles/buyers-remorse-ftcs-cooling-rule-may-help", "FTC: the Cooling-Off Rule"),
          ext("https://codes.ohio.gov/ohio-revised-code/section-1345.22", "Ohio Revised Code 1345.22"),
          ext("https://www.consumerfinance.gov/", "Consumer Financial Protection Bureau")])}
"""
    URLS.append(page("fine-print.html", "Reading the fine print: contracts, leases, subscriptions | Earth Rules",
                     "What to look for before you sign: auto-renewal, arbitration clauses, fees, leases, co-signing and privacy, plus your right to cancel.",
                     "EARTH RULES · FINE PRINT", "The fine print.", "What to look for before you sign, and how to back out.", fp))

    # ================= When someone dies =================
    wd = f"""
<section aria-labelledby="wd0"><h2 id="wd0">{ic("clock")} The first days</h2><ol class="steps">
<li><strong>If the death was unexpected at home,</strong> call 911. If the person was in hospice, call the hospice nurse.</li>
<li><strong>Call a funeral home.</strong> They move the body and usually report the death to Social Security. Under US law they must give you an itemized price list; you only pay for what you choose.</li>
<li><strong>Order death certificates.</strong> Get several certified copies. Banks, insurers and agencies each want one.</li>
<li><strong>Look for a will</strong> and any written funeral wishes.</li>
</ol></section>
<section aria-labelledby="wd1"><h2 id="wd1">{ic("document")} The weeks after</h2>{checklist([
 ("phone", "<strong>Social Security:</strong> call " + tel("800-772-1213") + ". Family members may be owed survivor benefits."),
 ("veterans", "<strong>Veterans:</strong> " + ext("https://www.va.gov/burials-memorials/", "VA burial benefits") + ", including a free burial in a national cemetery and a headstone."),
 ("dollar", "<strong>Banks, insurers, employer, pension:</strong> call each one. Ask about life insurance and final paychecks."),
 ("lock", "<strong>Credit bureaus:</strong> ask them to flag the credit file as deceased to stop identity theft."),
 ("rights_legal", "<strong>Probate:</strong> the court process that settles what they owned and owed. In Ohio it's the county probate court, and small estates can use a shorter process."),
 ("no", "<strong>Debts:</strong> you usually don't owe a family member's debts unless you co-signed. Debt collectors may not say you do."),
])}</section>
<section aria-labelledby="wd2"><h2 id="wd2">{ic("heart")} Do this now, for the people you love</h2>{checklist([
 ("document", "<strong>A will:</strong> who gets what, and who cares for your children."),
 ("idcard", "<strong>Power of attorney:</strong> who handles your money if you can't."),
 ("medical", "<strong>Health care wishes:</strong> a living will and a health care power of attorney. Ohio has standard free forms; " + ext("https://www.ohiolegalhelp.org/", "Ohio Legal Help") + " explains them."),
 ("yes", "<strong>Beneficiaries:</strong> name them on bank accounts, retirement accounts and life insurance. These pass outside the will."),
 ("book", "Put it all in <a href=\"papers.html\">your papers folder</a> and tell someone where it is."),
])}
<p>Grief has no schedule. If it's become too heavy, call or text <a href="tel:988">988</a>.</p></section>
{checked([ext("https://www.usa.gov/when-someone-dies", "USA.gov: what to do when someone dies"), ext("https://consumer.ftc.gov/articles/ftc-funeral-rule", "FTC: the Funeral Rule"),
          ext("https://www.va.gov/burials-memorials/", "VA burials and memorials"), ext("https://codes.ohio.gov/ohio-revised-code/section-2113.03", "Ohio Revised Code 2113.03: small estates"),
          ext("https://www.consumerfinance.gov/ask-cfpb/am-i-responsible-for-my-spouses-debts-after-they-die-en-1463/", "CFPB: debts after a death")])}
"""
    URLS.append(page("when-someone-dies.html", "When someone dies: what to do, and the paperwork | Earth Rules",
                     "What to do in the first days and weeks after a death, and the will, power of attorney and health care papers to put in place now.",
                     "EARTH RULES · WHEN SOMEONE DIES", "When someone dies.", "What to do first, what comes after, and what to set up now.", wd))

    # ================= Body basics =================
    bb = f"""
<section aria-labelledby="bb0" class="panel"><h2 id="bb0">Most bad decisions start here</h2>
<p>Tired, hungry, lonely or bored people make worse choices about money, food, drinking, fights and phones. Recovery groups use a word for it: HALT. Hungry, angry, lonely, tired. Check those four before a big decision.</p></section>
<section aria-labelledby="bb1"><h2 id="bb1">{ic("clock")} Sleep</h2>{checklist([
 ("clock", "Adults need 7 or more hours a night. Teens need more."),
 ("calendar", "Same bedtime and wake time every day, weekends too."),
 ("device", "Screens off and the room dark, cool and quiet."),
 ("medical", "Loud snoring, gasping or always tired? Ask a doctor; sleep apnea is common and treatable."),
])}</section>
<section aria-labelledby="bb2"><h2 id="bb2">{ic("food")} Food and moving</h2>{checklist([
 ("food", "Half your plate fruits and vegetables. Drink water. That's most of it."),
 ("dollar", "Cheap and healthy: dry beans, rice, oats, eggs, frozen vegetables, bananas."),
 ("transportation", "Move about 150 minutes a week, like a 30-minute walk five days a week. Any movement beats none."),
])}</section>
<section aria-labelledby="bb3"><h2 id="bb3">{ic("reuse")} Boredom</h2>
<p>Boredom isn't a problem to fix with a phone. It's often the feeling right before an idea. But long stretches of nothing to do can push people toward drinking, betting and scrolling.</p>{checklist([
 ("peer_support", "Have one thing you do with other people every week."),
 ("wrench", "Have one thing you do with your hands: cooking, fixing, drawing, gardening."),
 ("transportation", "When you're stuck, go outside and walk for ten minutes."),
])}</section>
{checked([ext("https://www.cdc.gov/sleep/about/index.html", "CDC: sleep"), ext("https://www.myplate.gov/", "USDA MyPlate"),
          ext("https://odphp.health.gov/our-work/nutrition-physical-activity/physical-activity-guidelines", "Physical Activity Guidelines for Americans")])}
"""
    URLS.append(page("body-basics.html", "Sleep, food and boredom: the basics | Earth Rules",
                     "The dull basics behind most bad decisions: sleep, food, moving and boredom, with the simple habits that help.",
                     "EARTH RULES · BODY BASICS", "Sleep, food, boredom.", "The dull basics that drive most of the big stuff.", bb))


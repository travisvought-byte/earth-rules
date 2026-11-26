(function () {
  var form = document.getElementById("bq-form");
  var dataEl = document.getElementById("bq-data");
  if (!form || !dataEl) return;
  var data = JSON.parse(dataEl.textContent);
  var out = document.getElementById("bq-results");
  var prefix = (document.querySelector('link[rel="stylesheet"]') || {}).getAttribute
    ? document.querySelector('link[rel="stylesheet"]').getAttribute("href").replace(/assets\/site\.css.*$/, "") : "";
  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var answers = {}, n = 0;
    new FormData(form).forEach(function (v, k) { if (v) { answers[k] = v; n++; } });
    var list = out.querySelector(".bq-list");
    var sum = out.querySelector(".bq-sum");
    list.innerHTML = "";
    out.hidden = false;
    if (!n) {
      sum.textContent = "You skipped every question, so there's nothing to match yet. Pick an answer for any question you have a feeling about.";
      out.focus();
      return;
    }
    var scored = Object.keys(data).map(function (slug) {
      var d = data[slug].d, s = 0;
      Object.keys(answers).forEach(function (k) { s += (d[k] && d[k][answers[k]]) || 0; });
      return { slug: slug, pct: Math.round((s / n) * 100) };
    }).sort(function (a, b) { return b.pct - a.pct || data[a.slug].n.localeCompare(data[b.slug].n); });
    sum.textContent = "Based on " + n + " answer" + (n === 1 ? "" : "s") + ". The closest are at the top. Tap one to read about it and find it near you.";
    scored.forEach(function (r, i) {
      var li = document.createElement("li");
      if (i >= 6) li.className = "bq-more";
      if (i >= 6) li.hidden = true;
      var a = document.createElement("a");
      a.href = prefix + "beliefs/" + r.slug + ".html";
      a.className = "bq-res";
      var name = document.createElement("b"); name.textContent = data[r.slug].n;
      var line = document.createElement("span"); line.className = "bq-line"; line.textContent = data[r.slug].l;
      var bar = document.createElement("span"); bar.className = "bq-bar";
      var fill = document.createElement("span"); fill.style.width = Math.max(r.pct, 2) + "%"; bar.appendChild(fill);
      var pct = document.createElement("span"); pct.className = "bq-pct"; pct.textContent = r.pct + "% match";
      a.appendChild(name); a.appendChild(pct); a.appendChild(bar); a.appendChild(line);
      li.appendChild(a);
      list.appendChild(li);
    });
    var more = out.querySelector(".bq-showall");
    if (!more) {
      more = document.createElement("button");
      more.type = "button"; more.className = "bq-showall";
      more.addEventListener("click", function () {
        out.querySelectorAll(".bq-more").forEach(function (x) { x.hidden = false; });
        more.hidden = true;
      });
      list.after(more);
    }
    more.textContent = "Show all " + scored.length;
    more.hidden = false;
    out.focus();
  });
})();

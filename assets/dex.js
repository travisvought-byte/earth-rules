/* Earth Rules progress: which topics you've marked as learned, saved on this device only. */
(function () {
  var KEY = "earthrules-learned";
  function load() { try { return JSON.parse(localStorage.getItem(KEY)) || []; } catch (e) { return []; } }
  function save(a) { try { localStorage.setItem(KEY, JSON.stringify(a)); } catch (e) {} }
  var RANKS = [[0, "Just starting"], [1, "Explorer"], [10, "Getting the hang of it"], [25, "Knows the ropes"], [45, "Handles anything"]];
  function paint() {
    var got = load();
    document.querySelectorAll("button.learn").forEach(function (b) {
      var on = got.indexOf(b.dataset.slug) >= 0;
      b.hidden = false;
      b.setAttribute("aria-pressed", on ? "true" : "false");
      b.querySelector("span").textContent = on ? "Learned" : "Mark as learned";
    });
    document.querySelectorAll("[data-slug]").forEach(function (a) {
      if (a.tagName !== "A") return;
      var on = got.indexOf(a.dataset.slug) >= 0, d = a.querySelector(".dx-done");
      a.classList.toggle("done", on);
      if (d) d.hidden = !on;
    });
    document.querySelectorAll("[data-slugs]").forEach(function (el) {
      var list = el.dataset.slugs.split(" "), n = list.filter(function (s) { return got.indexOf(s) >= 0; }).length;
      var c = el.querySelector(".dx-n"); if (c) c.textContent = n;
      var p = el.querySelector("progress"); if (p) p.value = n;
    });
    var r = document.querySelector(".dx-rank-name");
    if (r) { var name = RANKS[0][1]; RANKS.forEach(function (x) { if (got.length >= x[0]) name = x[1]; }); r.textContent = name; }
  }
  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest("button.learn");
    if (!b) return;
    var got = load(), i = got.indexOf(b.dataset.slug);
    if (i >= 0) got.splice(i, 1); else got.push(b.dataset.slug);
    save(got); paint();
  });
  paint();
})();
document.addEventListener("click", function (e) {
  var q = e.target.closest && e.target.closest("a.quickexit");
  if (q) { e.preventDefault(); window.location.replace(q.href); }
});

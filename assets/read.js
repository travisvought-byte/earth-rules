// "Read aloud": reads the page out loud with the browser's own voice (speechSynthesis).
// The button stays hidden in browsers that can't speak. Sources and the footer are skipped.
(function () {
  var btn = document.querySelector('.readaloud');
  if (!btn || !('speechSynthesis' in window) || typeof SpeechSynthesisUtterance === 'undefined') return;
  var synth = window.speechSynthesis, label = btn.querySelector('span');
  btn.hidden = false;
  btn.setAttribute('aria-pressed', 'false');

  function clean(el) {
    var c = el.cloneNode(true);
    c.querySelectorAll('.sr, .cite, svg').forEach(function (n) { n.remove(); });
    return c.textContent.replace(/\s+/g, ' ').trim();
  }
  function collect() {
    var out = [], h1 = document.querySelector('h1'), lead = document.querySelector('header p');
    if (h1) out.push(clean(h1));
    if (lead) out.push(clean(lead));
    var main = document.getElementById('main');
    var els = main.querySelectorAll('h2, h3, p, li, caption, th, td');
    els.forEach(function (el) {
      if (el.closest('footer')) return;
      var sec = el.closest('section');
      if (sec && sec.querySelector('#src-h')) return;
      if (el.parentElement.closest('li, p, td, th')) return; // avoid reading nested text twice
      var t = clean(el);
      if (t) out.push(t);
    });
    return out;
  }
  function chunks(texts) {
    var parts = [];
    texts.forEach(function (t) {
      (t.match(/[^.!?]+[.!?]*/g) || [t]).forEach(function (s) { s = s.trim(); if (s) parts.push(s); });
    });
    return parts;
  }
  function set(on) {
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    label.textContent = on ? 'Stop reading' : 'Read aloud';
  }
  function stop() { synth.cancel(); set(false); }
  btn.addEventListener('click', function () {
    if (btn.getAttribute('aria-pressed') === 'true') { stop(); return; }
    synth.cancel();
    var parts = chunks(collect());
    if (!parts.length) return;
    set(true);
    parts.forEach(function (p, i) {
      var u = new SpeechSynthesisUtterance(p);
      u.lang = document.documentElement.lang || 'en';
      u.rate = 0.95;
      if (i === parts.length - 1) { u.onend = function () { set(false); }; }
      u.onerror = function () { set(false); };
      synth.speak(u);
    });
  });
  window.addEventListener('pagehide', stop);
})();

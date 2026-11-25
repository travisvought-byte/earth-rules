// Phones: the main menu folds behind a Menu button (styles in site.css, only below 600px wide).
// The page head sets the "navjs" class, so without JavaScript the full menu shows as it always has.
(function () {
  var nav = document.getElementById('site-nav');
  var btn = nav && nav.querySelector('.navtoggle');
  if (!btn) return;
  function set(open) {
    nav.classList.toggle('open', open);
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    btn.textContent = open ? 'Close menu' : 'Menu';
  }
  btn.addEventListener('click', function () { set(!nav.classList.contains('open')); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && nav.classList.contains('open')) { set(false); btn.focus(); }
  });
})();

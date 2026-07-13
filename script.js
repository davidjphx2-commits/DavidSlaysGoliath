(function () {
  // centered top medallion — above the hero on home, above the title on interior
  if (!document.querySelector('.top-medallion')) {
    var med = document.createElement('a');
    med.className = 'top-medallion';
    med.href = 'index.html';
    med.setAttribute('aria-label', 'David Slays Goliath — home');
    med.innerHTML = '<img src="assets/logo-medallion.png" alt="David Slays Goliath">';
    var hero = document.querySelector('.hero');
    var main = document.querySelector('main');
    if (hero) hero.insertBefore(med, hero.firstChild);
    else if (main) main.insertBefore(med, main.firstChild);
  }

  // mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        nav.classList.remove('open');
        toggle.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // header shrink + scroll progress line (inject the bar if a page lacks it)
  var header = document.querySelector('.site-header');
  var prog = document.getElementById('scrollProgress');
  if (!prog) {
    prog = document.createElement('div');
    prog.id = 'scrollProgress';
    prog.className = 'scroll-progress';
    document.body.appendChild(prog);
  }
  var onScroll = function () {
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 8);
    if (prog) {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      prog.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // reveal on scroll — paragraphs, cards, diagrams, sections
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var targets = document.querySelectorAll('.reveal, main > p, main > h2, main > h3, .diagram-card, .verse-band');
  if (reduce || !('IntersectionObserver' in window)) {
    targets.forEach(function (el) { el.classList.add('reveal', 'in'); });
    return;
  }
  targets.forEach(function (el) { el.classList.add('reveal'); });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  targets.forEach(function (el, i) {
    // gentle stagger for cards in the same grid
    if (el.classList.contains('topic-card')) el.style.transitionDelay = ((i % 5) * 80) + 'ms';
    io.observe(el);
  });
})();

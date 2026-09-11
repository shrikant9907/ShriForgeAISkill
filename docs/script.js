(() => {
  const header = document.querySelector('[data-header]');
  const year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();

  const onScroll = () => header?.classList.toggle('is-scrolled', window.scrollY > 16);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const reveals = document.querySelectorAll('.reveal');
  if (reducedMotion || !('IntersectionObserver' in window)) {
    reveals.forEach((el) => el.classList.add('is-visible'));
  } else {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    reveals.forEach((el) => observer.observe(el));
  }

  const tabs = document.querySelectorAll('[data-code-tab]');
  const panels = document.querySelectorAll('[data-code-panel]');
  tabs.forEach((tab) => {
    tab.addEventListener('click', () => {
      const target = tab.dataset.codeTab;
      tabs.forEach((item) => {
        const selected = item === tab;
        item.classList.toggle('is-active', selected);
        item.setAttribute('aria-selected', selected ? 'true' : 'false');
      });
      panels.forEach((panel) => panel.classList.toggle('is-active', panel.dataset.codePanel === target));
    });
  });
})();

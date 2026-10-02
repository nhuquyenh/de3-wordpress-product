(function () {
    const header = document.querySelector('[data-de3-header]');
    const toggle = document.querySelector('.de3-menu-toggle');
    const nav = document.querySelector('.de3-nav');

    if (header) {
        const updateHeader = function () {
            header.classList.toggle('is-scrolled', window.scrollY > 12);
        };
        updateHeader();
        window.addEventListener('scroll', updateHeader, { passive: true });
    }

    if (!toggle || !nav) {
        return;
    }

    toggle.addEventListener('click', function () {
        const isOpen = toggle.getAttribute('aria-expanded') === 'true';
        toggle.setAttribute('aria-expanded', String(!isOpen));
        nav.classList.toggle('is-open', !isOpen);
    });

    nav.querySelectorAll('a').forEach(function (link) {
        link.addEventListener('click', function () {
            toggle.setAttribute('aria-expanded', 'false');
            nav.classList.remove('is-open');
        });
    });
})();

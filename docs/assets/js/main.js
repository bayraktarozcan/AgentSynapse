document.addEventListener('DOMContentLoaded', () => {
    // Animated counters
    const counters = document.querySelectorAll('.stat-value');
    counters.forEach(el => {
        const target = parseInt(el.textContent.replace(/[,+]/g, ''), 10);
        if (isNaN(target)) return;
        const duration = 1200;
        const start = performance.now();
        function update(now) {
            const elapsed = now - start;
            const progress = Math.min(elapsed / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            el.textContent = Math.floor(eased * target).toLocaleString() + '+';
            if (progress < 1) requestAnimationFrame(update);
        }
        requestAnimationFrame(update);
    });

    // Language toggle
    const langLinks = document.querySelectorAll('.lang-toggle a');
    langLinks.forEach(link => {
        link.addEventListener('click', e => {
            e.preventDefault();
            const lang = link.getAttribute('data-lang');
            langLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
            if (lang === 'tr') {
                document.body.classList.add('lang-tr');
            } else {
                document.body.classList.remove('lang-tr');
            }
        });
    });
});

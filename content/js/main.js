document.addEventListener('DOMContentLoaded', function () {
    // Footer year
    const yearEl = document.getElementById('footerYear');
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    // Active nav link
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(function (link) {
        var href = link.getAttribute('href');
        if (currentPath === href || (href !== '/index.html' && currentPath.startsWith(href.replace('.html', '')))) {
            link.classList.add('active');
        } else if (currentPath === '/' || currentPath === '/index.html') {
            if (href === '/index.html') link.classList.add('active');
            else link.classList.remove('active');
        } else {
            link.classList.remove('active');
        }
    });

    // Hamburger toggle
    var hamburger = document.getElementById('hamburgerBtn');
    var navLinks = document.getElementById('navLinks');
    var overlay = document.getElementById('overlay');

    function toggleMenu() {
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('open');
        overlay.classList.toggle('show');
        document.body.style.overflow = navLinks.classList.contains('open') ? 'hidden' : '';
    }

    function closeMenu() {
        hamburger.classList.remove('active');
        navLinks.classList.remove('open');
        overlay.classList.remove('show');
        document.body.style.overflow = '';
    }

    if (hamburger) {
        hamburger.addEventListener('click', toggleMenu);
    }

    if (overlay) {
        overlay.addEventListener('click', closeMenu);
    }

    document.querySelectorAll('.nav-link').forEach(function (link) {
        link.addEventListener('click', closeMenu);
    });

    // Search functionality
    var searchInput = document.getElementById('heroSearchInput');
    if (searchInput) {
        searchInput.addEventListener('input', function () {
            var query = this.value.trim().toLowerCase();
            var sections = document.querySelectorAll('.section');
            var hasVisible = false;

            sections.forEach(function (section) {
                var items = section.querySelectorAll('.rank-item');
                var found = false;

                if (!query) {
                    section.style.display = '';
                    items.forEach(function (item) { item.style.display = ''; });
                    found = true;
                } else {
                    items.forEach(function (item) {
                        var title = (item.querySelector('.rank-title') || {}).textContent || '';
                        var meta = (item.querySelector('.rank-meta') || {}).textContent || '';
                        var match = title.toLowerCase().includes(query) || meta.toLowerCase().includes(query);
                        item.style.display = match ? '' : 'none';
                        if (match) found = true;
                    });
                    section.style.display = found ? '' : 'none';
                }

                if (found) hasVisible = true;
            });

            // Show/hide empty state
            var emptyState = document.querySelector('.search-empty');
            if (!query) {
                if (emptyState) emptyState.remove();
                return;
            }

            if (!hasVisible) {
                if (!emptyState) {
                    emptyState = document.createElement('div');
                    emptyState.className = 'search-empty';
                    emptyState.innerHTML = '<div class="empty-icon">🔍</div><p>没有找到匹配 "{query}" 的结果</p>'.replace('{query}', query);
                    document.querySelector('.section-grid').appendChild(emptyState);
                }
            } else {
                if (emptyState) emptyState.remove();
            }
        });
    }

    // WeChat modal
    var wechatModal = document.getElementById('wechatModal');
    var wechatBtns = document.querySelectorAll('#wechatBtn, #wechatBtnMobile');

    function openWechatModal() {
        wechatModal.classList.add('show');
        document.body.style.overflow = 'hidden';
    }

    function closeWechatModal() {
        wechatModal.classList.remove('show');
        document.body.style.overflow = '';
    }

    wechatBtns.forEach(function (btn) {
        btn.addEventListener('click', openWechatModal);
    });

    wechatModal.addEventListener('click', function (e) {
        if (e.target === wechatModal) {
            closeWechatModal();
        }
    });

    var closeBtn = document.getElementById('wechatModalClose');
    if (closeBtn) {
        closeBtn.addEventListener('click', closeWechatModal);
    }

    // Scroll effect for navbar
    var lastScroll = 0;
    var navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', function () {
        var currentScroll = window.pageYOffset;
        if (currentScroll > 80) {
            navbar.style.boxShadow = '0 1px 4px rgba(0,0,0,0.08)';
        } else {
            navbar.style.boxShadow = 'none';
        }
        lastScroll = currentScroll;
    }, { passive: true });
});

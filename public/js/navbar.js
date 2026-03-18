/**
 * Navbar Component for BenefitAI
 * Centralizes navigation structure and authentication logic.
 */

async function initNavbar(activePage) {
    const container = document.getElementById('navbar-container');
    if (!container) return;

    // Standard Navbar HTML
    const navbarHtml = `
    <nav class="navbar">
        <div class="logo-link" style="display:none;">BenefitAI</div>
        <div class="nav-links">
            <a href="index.html" class="${activePage === 'home' ? 'active' : ''}">Home</a>
            <a href="analyze.html" class="${activePage === 'analyze' ? 'active' : ''}">Analyze Profile</a>
            <a href="students.html" class="${activePage === 'students' ? 'active' : ''}">Explore Schemes</a>
            <a href="institutes.html" class="${activePage === 'institutes' ? 'active' : ''}">Institutes</a>
            <a href="#">News</a>
        </div>
        <div id="navAuth" class="nav-auth">
            <!-- Loading state or fallback -->
        </div>
        <div class="navbar-mobile-toggle">☰</div>
    </nav>

    <div class="sidebar-overlay" id="sidebarOverlay"></div>
    <div class="mobile-sidebar" id="mobileSidebar">
        <div class="sidebar-header">
            <div class="sidebar-logo">BenefitAI</div>
            <div class="sidebar-close" id="sidebarClose">&times;</div>
        </div>
        <div class="sidebar-links">
            <a href="index.html" class="${activePage === 'home' ? 'active' : ''}">Home</a>
            <a href="analyze.html" class="${activePage === 'analyze' ? 'active' : ''}">Analyze Profile</a>
            <a href="students.html" class="${activePage === 'students' ? 'active' : ''}">Explore Schemes</a>
            <a href="institutes.html" class="${activePage === 'institutes' ? 'active' : ''}">Institutes</a>
            <a href="#">News</a>
            <div id="sidebarAuth" class="sidebar-auth-group"></div>
        </div>
    </div>
    `;

    container.innerHTML = navbarHtml;

    const nav = container.querySelector('.navbar');
    const toggle = container.querySelector('.navbar-mobile-toggle');
    const sidebar = document.getElementById('mobileSidebar');
    const overlay = document.getElementById('sidebarOverlay');
    const closeBtn = document.getElementById('sidebarClose');

    const toggleSidebar = (show) => {
        if (show) {
            sidebar.classList.add('open');
            overlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        } else {
            sidebar.classList.remove('open');
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        }
    };

    if (toggle) toggle.addEventListener('click', () => toggleSidebar(true));
    if (overlay) overlay.addEventListener('click', () => toggleSidebar(false));
    if (closeBtn) closeBtn.addEventListener('click', () => toggleSidebar(false));

    // Authentication Logic
    const navAuth = document.getElementById('navAuth');
    try {
        const me = await apiFetch('/me');
        let authLinks = `
            <a href="dashboard.html" class="${activePage === 'dashboard' ? 'active' : ''}">Dashboard</a>
            <a href="profile.html" class="${activePage === 'profile' ? 'active' : ''} nav-profile-link">
                ${me.profile_pic ? `<img src="${me.profile_pic}" class="nav-avatar">` : `<span class="nav-avatar-fallback">👤</span>`}
                <span>Profile</span>
            </a>
        `;

        // Only show Status link for users with profile complete
        if (me.profile_complete) {
             authLinks = `
                <a href="dashboard.html" class="${activePage === 'dashboard' ? 'active' : ''}">Dashboard</a>
                <a href="dashboard.html#applications" class="${activePage === 'status' ? 'active' : ''}">Status</a>
                <a href="profile.html" class="${activePage === 'profile' ? 'active' : ''} nav-profile-link">
                    ${me.profile_pic ? `<img src="${me.profile_pic}" class="nav-avatar">` : `<span class="nav-avatar-fallback">👤</span>`}
                    <span>Profile</span>
                </a>
            `;
        }

        // Admin check
        if (me.email === 'aryan13705@gmail.com') {
            authLinks += `<a href="admin.html" class="${activePage === 'admin' ? 'active' : ''}">Admin</a>`;
        }

        authLinks += `<a href="#" id="logoutBtn" class="logout-link">Logout</a>`;
        navAuth.innerHTML = authLinks;
        
        const sidebarAuth = document.getElementById('sidebarAuth');
        if (sidebarAuth) sidebarAuth.innerHTML = authLinks;

        // Logout listeners
        document.querySelectorAll('#logoutBtn').forEach(btn => {
            btn.addEventListener('click', async (e) => {
                e.preventDefault();
                try {
                    await apiFetch('/logout', { method: 'POST' });
                    window.location.href = 'index.html';
                } catch (err) {
                    console.error('Logout failed:', err);
                    window.location.href = 'index.html';
                }
            });
        });
    } catch (err) {
        // Not logged in
        const guestLinks = `
            <a href="login.html" class="${activePage === 'login' ? 'active' : ''}">Login</a>
            <a href="register.html" class="${activePage === 'register' ? 'active' : ''}">Register</a>
        `;
        navAuth.innerHTML = guestLinks;
        const sidebarAuth = document.getElementById('sidebarAuth');
        if (sidebarAuth) sidebarAuth.innerHTML = guestLinks;
    }

    // Initialize News for the page (if ticker exists)
    loadGlobalNews();
}

/**
 * Globally updates news tickers and news boxes if they exist on the page.
 */
async function loadGlobalNews() {
    const tickerContent = document.querySelector('.ticker-content');
    const newsBody = document.querySelector('.news-body');
    
    if (!tickerContent && !newsBody) return;

    try {
        const news = await apiFetch('/news');
        if (!news || news.length === 0) return;

        if (tickerContent) {
            tickerContent.innerHTML = news.map(item => `<span>🔥 [${item.date}] ${item.title}</span>`).join('');
        }

        if (newsBody) {
            newsBody.innerHTML = news.map(item => `
                <div class="news-item">
                    <span class="news-date">${item.date}</span>
                    <p class="news-text"><a href="${item.link}" target="_blank" style="color: inherit; text-decoration: none;">${item.title}</a></p>
                </div>
            `).join('');
        }
    } catch (err) {
        console.error('Failed to load global news:', err);
    }
}

GLOBAL_CSS = """
body {
    background:
        radial-gradient(circle at top left, rgba(205, 225, 214, 0.35), transparent 28%),
        linear-gradient(180deg, #f4efe6 0%, #fcfaf6 100%);
    color: #1f2933;
    font-family: "Segoe UI", sans-serif;
}
.app-shell {
    width: min(1180px, calc(100vw - 32px));
    margin: 0 auto;
}
.brand-header {
    background: transparent;
    box-shadow: none;
}
.nav-link {
    color: #f6f1e7;
    font-weight: 600;
    text-decoration: none;
}
.nav-links {
    display: flex;
    gap: 1.5rem;
    align-items: center;
}
.hero-panel {
    background: linear-gradient(135deg, rgba(21, 67, 54, 0.96), rgba(37, 78, 112, 0.92));
    border-radius: 28px;
    box-shadow: 0 24px 60px rgba(26, 45, 64, 0.18);
    overflow: hidden;
    min-height: 420px;
}
.hero-copy {
    padding: 2.75rem 3rem;
}
.hero-title {
    font-size: clamp(2.5rem, 4vw, 4.4rem);
    font-weight: 800;
    line-height: 1.05;
    color: #fff8ed;
}
.hero-subtitle {
    color: rgba(255, 248, 237, 0.82);
    font-size: 1.05rem;
    line-height: 1.7;
    max-width: 38rem;
}
.hero-media {
    min-height: 420px;
    background:
        linear-gradient(145deg, rgba(255, 248, 237, 0.15), rgba(255, 248, 237, 0.03)),
        repeating-linear-gradient(
            135deg,
            rgba(255, 255, 255, 0.05),
            rgba(255, 255, 255, 0.05) 18px,
            transparent 18px,
            transparent 36px
        ),
        url('https://www.csueastbay.edu/_files/images/home/redesign/hero-impact.webp');
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    display: flex;
    align-items: center;
    justify-content: center;
    color: rgba(255, 248, 237, 0.72);
    font-size: 1rem;
    text-align: center;
    padding: 0;
}
.section-label {
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #49635b;
    font-weight: 700;
    font-size: 0.78rem;
}
.book-card {
    border-radius: 22px;
    background: rgba(255, 255, 255, 0.88);
    border: 1px solid rgba(50, 73, 72, 0.08);
    box-shadow: 0 14px 35px rgba(38, 51, 77, 0.08);
}
.book-cover {
    border-radius: 18px;
    min-height: 220px;
    padding: 1rem;
    color: rgba(255, 248, 237, 0.95);
    display: flex;
    align-items: end;
    justify-content: start;
    font-size: 1.2rem;
    font-weight: 700;
}
.stat-pill {
    border-radius: 999px;
    background: #edf4ee;
    color: #35574e;
    padding: 0.35rem 0.8rem;
    font-size: 0.86rem;
    font-weight: 600;
}
.site-footer {
    color: #52606d;
    border-top: 1px solid rgba(50, 73, 72, 0.1);
}
.books-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 1.25rem;
    width: 100%;
}
.surface-card {
    background: rgba(255, 255, 255, 0.96);
    border: 1px solid rgba(50, 73, 72, 0.08);
    box-shadow: 0 14px 35px rgba(38, 51, 77, 0.06);
    border-radius: 24px;
}
.primary-button {
    background: #1d5c63 !important;
    color: #fff8ed !important;
    font-weight: 700;
}
.primary-button .q-focus-helper {
    opacity: 0 !important;
}
.secondary-button {
    background: #f6d88d !important;
    color: #243b3f !important;
    font-weight: 700;
}
.secondary-button .q-focus-helper {
    opacity: 0 !important;
}
.outline-button {
    color: #fff8ed !important;
    border-color: rgba(255, 248, 237, 0.75) !important;
    font-weight: 700;
}
.neutral-outline-button {
    color: #1d5c63 !important;
    border-color: rgba(29, 92, 99, 0.35) !important;
    font-weight: 700;
}
.brand-heading {
    font-family: "Segoe UI", sans-serif;
}
@media (max-width: 700px) {
    .hero-copy {
        padding: 2rem;
    }
    .hero-panel {
        min-height: auto;
    }
    .hero-media {
        min-height: 260px;
    }
    .nav-links {
        display: none;
    }
    .site-footer {
        flex-direction: column;
        align-items: flex-start;
        gap: 0.5rem;
    }
}
"""

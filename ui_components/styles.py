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
.floating-shell {
    background: rgba(16, 32, 41, 0.94);
    border: 1px solid rgba(240, 185, 74, 0.12);
    border-radius: 24px;
    box-shadow: 0 14px 32px rgba(10, 18, 24, 0.12);
    backdrop-filter: blur(10px);
    padding: 1rem 1.5rem;
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
    position: relative;
    background:
        linear-gradient(90deg, rgba(0, 0, 0, 0.98) 0%, rgba(0, 0, 0, 0.96) 38%, rgba(0, 0, 0, 0.84) 52%, rgba(0, 0, 0, 0.58) 62%, rgba(0, 0, 0, 0.26) 72%, rgba(0, 0, 0, 0.08) 80%, rgba(0, 0, 0, 0) 88%),
        radial-gradient(circle at top right, rgba(240, 185, 74, 0.12), transparent 22%),
        url('https://www.csueastbay.edu/_files/images/home/redesign/hero-impact.webp'),
        linear-gradient(135deg, rgba(7, 13, 16, 0.98), rgba(16, 32, 41, 0.94));
    background-position: center, top right, right center, center;
    background-repeat: no-repeat;
    background-size: auto, auto, auto 100%, cover;
    border-radius: 34px;
    box-shadow: 0 32px 70px rgba(18, 30, 42, 0.24);
    overflow: hidden;
    min-height: 480px;
}
.hero-copy {
    position: relative;
    z-index: 2;
    padding: 4.25rem 3.5rem 4rem;
    max-width: 46rem;
}
.hero-kicker {
    font-family: "Segoe UI", sans-serif;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(255, 255, 255, 0.72);
    font-size: 0.78rem;
    font-weight: 700;
}
.hero-title {
    font-size: clamp(3rem, 5vw, 5.4rem);
    font-weight: 700;
    line-height: 0.95;
    color: #fffaf2;
}
.hero-title-accent {
    color: #f0b94a;
}
.hero-subtitle {
    color: rgba(255, 250, 242, 0.8);
    font-size: 1.06rem;
    line-height: 1.8;
    max-width: 30rem;
    font-family: "Segoe UI", sans-serif;
}
.hero-actions {
    gap: 0.9rem;
}
.hero-action-link {
    width: fit-content;
    color: #fffaf2;
    text-decoration: none;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    font-family: "Segoe UI", sans-serif;
    font-weight: 700;
    font-size: 1rem;
    position: relative;
    padding-left: 2rem;
}
.hero-action-link::before {
    content: "→";
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-52%);
    color: #f0b94a;
    font-size: 1.2rem;
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
    color: rgba(255, 250, 242, 0.78);
    border-top: 1px solid rgba(240, 185, 74, 0.18);
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
        padding: 2.25rem 2rem 1.25rem;
    }
    .hero-panel {
        min-height: auto;
        background-position: center, top right, center bottom, center;
        background-size: auto, auto, 100% auto, cover;
    }
    .hero-title {
        font-size: clamp(2.6rem, 12vw, 3.8rem);
    }
    .hero-copy {
        padding: 2.25rem 2rem 2rem;
    }
    .nav-links {
        display: none;
    }
    .floating-shell {
        padding: 0.9rem 1rem;
    }
    .site-footer {
        flex-direction: column;
        align-items: flex-start;
        gap: 0.5rem;
    }
}
"""

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
.brand-link {
    color: #f6f1e7;
    text-decoration: none;
}
.nav-link {
    color: #f6f1e7;
    font-family: "Segoe UI", sans-serif;
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    text-decoration: none;
}
.nav-links {
    display: flex;
    gap: 1.5rem;
    align-items: center;
}
.header-signin {
    color: #f6f1e7 !important;
    font-family: "Segoe UI", sans-serif;
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}
.header-signin .q-focus-helper {
    opacity: 0 !important;
}
.hero-panel {
    position: relative;
    background:
        linear-gradient(90deg, rgba(0, 0, 0, 0.98) 0%, rgba(0, 0, 0, 0.96) 38%, rgba(0, 0, 0, 0.84) 52%, rgba(0, 0, 0, 0.58) 62%, rgba(0, 0, 0, 0.26) 72%, rgba(0, 0, 0, 0.08) 80%, rgba(0, 0, 0, 0) 88%),
        radial-gradient(circle at top right, rgba(240, 185, 74, 0.12), transparent 22%),
        url('https://www.csueastbay.edu/_files/images/home/redesign/hero-impact.webp'),
        linear-gradient(135deg, rgba(7, 13, 16, 0.98), rgba(16, 32, 41, 0.94));
    background-position: center, top right, calc(100% + 24px) center, center;
    background-repeat: no-repeat;
    background-size: auto, auto, auto 104%, cover;
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
.login-page-shell {
    min-height: calc(100vh - 240px);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem 0 3rem;
}
.login-card {
    width: min(460px, 100%);
    padding: 2rem;
    border-radius: 28px;
    background: linear-gradient(180deg, rgba(255, 252, 246, 0.98), rgba(255, 248, 238, 0.95));
    border: 1px solid rgba(50, 73, 72, 0.08);
    box-shadow: 0 24px 54px rgba(18, 30, 42, 0.14);
}
.login-subtitle {
    color: #5f6c76;
    font-size: 1rem;
    line-height: 1.7;
    margin: 0.5rem 0 1rem;
}
.login-input {
    width: 100%;
    margin-top: 0.75rem;
}
.login-input .q-field__control {
    border-radius: 16px !important;
    background: rgba(255, 255, 255, 0.9);
}
.login-button,
.login-button.q-btn {
    width: 100%;
    margin-top: 1rem;
    background: rgba(16, 32, 41, 0.96) !important;
    color: #f6f1e7 !important;
    border: 1px solid rgba(240, 185, 74, 0.14);
    border-radius: 16px !important;
    font-family: "Segoe UI", sans-serif;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    min-height: 52px;
}
.login-button .q-btn__content {
    color: #f6f1e7 !important;
}
.login-button .q-focus-helper {
    opacity: 0 !important;
}
.login-caption {
    color: #6b7280;
    font-size: 0.82rem;
    line-height: 1.6;
    margin-top: 1rem;
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
    overflow: hidden;
}
.book-cover-shell {
    width: 100%;
    margin: 0;
    padding: 0;
}
.book-cover {
    border-radius: 22px 22px 0 0;
    min-height: 240px;
    width: 100%;
    margin: 0;
    padding: 1.25rem;
    color: rgba(255, 248, 237, 0.95);
    display: flex;
    align-items: end;
    justify-content: start;
    font-size: 1.2rem;
    font-weight: 700;
}
.book-card-body {
    padding: 1rem;
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
    align-items: center;
    min-height: 104px;
}
.site-footer-content {
    align-items: flex-end;
    text-align: right;
}
.site-footer-links {
    display: flex;
    gap: 1.25rem;
    align-items: center;
    justify-content: flex-end;
    flex-wrap: wrap;
}
.site-footer-link {
    color: #f6f1e7;
    text-decoration: none;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    font-size: 0.85rem;
    font-weight: 700;
}
.books-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 320px));
    gap: 1.25rem;
    width: 100%;
    justify-content: center;
    justify-items: center;
    margin: 0 auto;
}
.featured-shelf-intro {
    width: min(100%, 1010px);
    margin: 0 auto;
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
    .login-page-shell {
        min-height: auto;
        padding: 1.25rem 0 2rem;
    }
    .login-card {
        padding: 1.5rem;
    }
    .nav-links {
        display: none;
    }
    .floating-shell {
        padding: 0.9rem 1rem;
    }
    .site-footer {
        min-height: auto;
        flex-direction: column;
        align-items: flex-start;
        gap: 0.75rem;
    }
    .site-footer-content {
        align-items: flex-start;
        text-align: left;
    }
    .site-footer-links {
        justify-content: flex-start;
        gap: 0.9rem;
    }
}
"""

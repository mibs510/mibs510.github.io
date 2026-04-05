from __future__ import annotations

from nicegui import ui

from models import Book, featured_books

def create_header() -> None:
    with ui.header().classes('brand-header text-white q-py-md'):
        with ui.row().classes('app-shell floating-shell items-center justify-between no-wrap'):
            with ui.link(target='/').classes('brand-link'):
                with ui.row().classes('items-center q-gutter-sm no-wrap'):
                    ui.icon('local_library', size='md')
                    ui.label('ShelfWise').classes('text-h5 text-weight-bold brand-heading')
            with ui.row().classes('nav-links'):
                ui.link('Browse', '/').classes('nav-link')
                ui.link('Collections', '/').classes('nav-link')
                ui.link('About', '/').classes('nav-link')
            with ui.row().classes('items-center'):
                ui.button('Sign In', on_click=lambda: ui.navigate.to('/login')).props('flat color=white no-caps').classes('header-signin')


def create_footer() -> None:
    with ui.footer().classes('bg-transparent q-py-lg'):
        with ui.row().classes('app-shell floating-shell site-footer justify-between'):
            with ui.column().classes('q-gutter-xs'):
                ui.label('ShelfWise Library System').classes('text-subtitle2 text-weight-bold')
            with ui.column().classes('site-footer-content q-gutter-sm'):
                ui.label('Built to simplify discovery, circulation, and everyday library operations.')
                with ui.row().classes('site-footer-links'):
                    ui.link('Browse Catalog', '/app').classes('site-footer-link')
                    ui.link('Collections', '/').classes('site-footer-link')
                    ui.link('Member Access', '/login').classes('site-footer-link')


def create_hero_section() -> None:
    with ui.row().classes('app-shell hero-panel q-col-gutter-none items-stretch'):
        with ui.column().classes('col-12 hero-copy justify-center'):
            ui.label('ShelfWise').classes('hero-kicker')
            with ui.column().classes('q-gutter-none'):
                ui.label('Forge a Better Library').classes('hero-title')
                ui.label('Workflow.').classes('hero-title hero-title-accent')
            ui.label(
                'Manage inventory, member accounts, circulation, and admin tasks in one place '
                'without burying the project under spreadsheets and disconnected forms.'
            ).classes('hero-subtitle q-mt-lg')
            with ui.column().classes('hero-actions q-mt-xl'):
                ui.link('Open the catalog', '/app').classes('hero-action-link')
                ui.link('Prototype sign in', '/login').classes('hero-action-link')



def create_book_card(book: Book) -> None:
    with ui.card().classes('book-card full-height'):
        with ui.element('div').classes('book-cover-shell w-full'):
            with ui.element('div').classes('book-cover').style(f'background: {book.cover_color};'):
                ui.label(book.title)
        with ui.column().classes('book-card-body full-height no-wrap'):
            with ui.card_section().classes('q-pa-none'):
                ui.label(book.title).classes('text-h6 text-weight-bold')
                ui.label(f'by {book.author}').classes('text-subtitle2 text-grey-7')
                ui.label(book.summary).classes('text-body2 q-mt-sm')
            ui.space()
            with ui.row().classes('q-gutter-sm q-mt-md items-center'):
                ui.label(f'{book.rating:.1f} stars').classes('stat-pill')
                ui.label(f'{book.available_copies}/{book.total_copies} available').classes('stat-pill')


def create_homepage() -> None:
    create_header()
    create_footer()

    with ui.column().classes('w-full q-pb-xl'):
        create_hero_section()

        with ui.column().classes('app-shell q-mt-xl q-gutter-lg'):
            with ui.column().classes('featured-shelf-intro q-gutter-sm'):
                ui.label('Featured Shelf').classes('section-label')
                with ui.column().classes('q-gutter-xs'):
                    ui.label('Curated picks from the Featured Shelf').classes('text-h4 text-weight-bold brand-heading')
                    ui.label(
                        'Explore standout titles selected to highlight the breadth of the collection and invite '
                        'readers into their next great find.'
                    ).classes('text-body1 text-grey-7')

            with ui.element('div').classes('books-grid'):
                for book in featured_books():
                    create_book_card(book)

from __future__ import annotations

from nicegui import ui

from models import Book, featured_books


def create_header() -> None:
    with ui.header().classes('brand-header text-white q-py-md'):
        with ui.row().classes('app-shell items-center justify-between no-wrap'):
            with ui.row().classes('items-center q-gutter-sm'):
                ui.icon('local_library', size='md')
                ui.label('ShelfWise').classes('text-h5 text-weight-bold brand-heading')
            with ui.row().classes('nav-links'):
                ui.link('Browse', '/').classes('nav-link')
                ui.link('Collections', '/').classes('nav-link')
                ui.link('About', '/').classes('nav-link')
            with ui.row().classes('items-center q-gutter-sm'):
                ui.button('Sign In', on_click=lambda: ui.navigate.to('/login')).props('flat color=white no-caps')
                ui.button('Open App', on_click=lambda: ui.navigate.to('/app')).props('unelevated no-caps').classes('secondary-button')


def create_footer() -> None:
    with ui.footer().classes('bg-transparent q-py-lg'):
        with ui.row().classes('app-shell site-footer items-center justify-between q-pt-lg'):
            ui.label('ShelfWise Library System').classes('text-subtitle2 text-weight-bold')
            ui.label('NiceGUI + SQLite scaffold for circulation, inventory, and account workflows.')


def create_hero_section() -> None:
    with ui.row().classes('app-shell hero-panel q-col-gutter-none items-stretch'):
        with ui.column().classes('col-12 col-md-7 hero-copy justify-center'):
            ui.label('Library workflows without the spreadsheet pain.').classes('hero-title')
            ui.label(
                'Track inventory, circulate books, manage member accounts, and leave room for admin tools '
                'without turning a homework project into a mess.'
            ).classes('hero-subtitle q-mt-md')
            with ui.row().classes('q-gutter-sm q-mt-xl'):
                ui.button('Explore the catalog', on_click=lambda: ui.navigate.to('/app')).props('unelevated no-caps').classes('secondary-button')
                ui.button('Prototype login', on_click=lambda: ui.navigate.to('/login')).props('outline no-caps').classes('outline-button')
        ui.element('div').classes('col-12 col-md-5 hero-media')


def create_book_card(book: Book) -> None:
    with ui.card().classes('book-card full-height q-pa-md'):
        with ui.column().classes('full-height no-wrap'):
            with ui.card_section().classes('q-pa-none'):
                with ui.element('div').classes('book-cover').style(f'background: {book.cover_color};'):
                    ui.label(book.title)
            with ui.card_section().classes('q-px-none q-pb-none'):
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
            ui.label('Featured Shelf').classes('section-label')
            with ui.row().classes('items-end justify-between'):
                with ui.column().classes('q-gutter-xs'):
                    ui.label('Mocked-up book cards for the landing page').classes('text-h4 text-weight-bold brand-heading')
                    ui.label(
                        'These cards are seeded from SQLite now, so the same data model can grow into browse, '
                        'checkout, and admin CRUD pages.'
                    ).classes('text-body1 text-grey-7')
                ui.button('View user area', on_click=lambda: ui.navigate.to('/app')).props('outline no-caps').classes('neutral-outline-button')

            with ui.element('div').classes('books-grid'):
                for book in featured_books():
                    create_book_card(book)

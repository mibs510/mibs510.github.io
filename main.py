from urllib.parse import quote

from nicegui import app, ui

from models import featured_books, get_user_by_username, initialize_database
from ui_components import GLOBAL_CSS, create_book_card, create_footer, create_header, create_homepage


def add_global_styles() -> None:
    ui.colors(
        primary='#102029',
        secondary='#1d5c63',
        accent='#f0b94a',
        dark='#102029',
        dark_page='#070d10',
        positive='#2d7a55',
        negative='#b84444',
        info='#3f7ca8',
        warning='#f0b94a',
    )
    ui.add_head_html(f'<style>{GLOBAL_CSS}</style>')


def build_favicon_data_uri() -> str:
    svg = f"""
    <svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
      <rect width="64" height="64" rx="16" fill="#102029"/>
      <g transform="translate(8 8) scale(2)">
        <path d="M0 0h24v24H0z" fill="none"/>
        <path fill="#f6f1e7" d="M12 11.55C9.64 9.35 6.48 8 3 8v11c3.48 0 6.64 1.35 9 3.55 2.36-2.19 5.52-3.55 9-3.55V8c-3.48 0-6.64 1.35-9 3.55zM12 8c1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3 1.34 3 3 3z"/>
      </g>
    </svg>
    """.strip()
    return f'data:image/svg+xml;utf8,{quote(svg)}'


def user_is_logged_in() -> bool:
    return bool(app.storage.user.get('username'))


def require_login() -> bool:
    if not user_is_logged_in():
        ui.notify('Use the demo login first.', color='warning')
        ui.navigate.to('/login')
        return False
    return True


@ui.page('/')
def home_page() -> None:
    add_global_styles()
    create_homepage()


@ui.page('/login')
def login_page() -> None:
    add_global_styles()
    create_header()
    create_footer()

    with ui.column().classes('app-shell login-page-shell'):
        with ui.card().classes('login-card'):
            ui.label('Prototype Login').classes('text-h4 text-weight-bold brand-heading')
            ui.label(
                'This is a temporary sign-in flow so we can demonstrate the authenticated layout and floating menu.'
            ).classes('login-subtitle')
            username = ui.input('Username', value='student').props('outlined').classes('login-input')
            ui.input('Password', value='demo').props('outlined type=password').classes('login-input')

            def sign_in() -> None:
                account = get_user_by_username(username.value.strip() or 'student')
                if account is None:
                    ui.notify('User not found in the local database.', color='negative')
                    return

                app.storage.user['username'] = account.username
                app.storage.user['role'] = 'admin' if account.is_admin else 'member'
                ui.notify(f'Signed in as {account.username}', color='positive')
                ui.navigate.to('/app')

            ui.button('Enter library app', on_click=sign_in).props('unelevated no-caps').classes('login-button')
            ui.label(
                'Demo accounts available: student and admin. Password validation is not implemented yet.'
            ).classes('login-caption')


@ui.page('/app')
def app_page() -> None:
    add_global_styles()
    if not require_login():
        return

    with ui.left_drawer(value=False).classes('bg-white') as drawer:
        ui.label('Library Menu').classes('text-h6 text-weight-bold q-mb-md')
        ui.link('Dashboard', '/app').classes('text-body1')
        ui.link('Browse Books', '/').classes('text-body1')
        ui.link('My Checkouts', '/app').classes('text-body1')
        if app.storage.user.get('role') == 'admin':
            ui.separator().classes('q-my-md')
            ui.label('Admin Tools').classes('text-subtitle2 text-weight-bold')
            ui.link('Manage Inventory', '/app').classes('text-body1')
            ui.link('Create / Edit Books', '/app').classes('text-body1')

    with ui.page_sticky(position='bottom-right', x_offset=24, y_offset=24):
        ui.button(icon='menu', on_click=drawer.toggle).props('fab').classes('primary-button')

    with ui.header().classes('brand-header text-white q-py-sm'):
        with ui.row().classes('app-shell items-center justify-between'):
            ui.label('ShelfWise').classes('text-h5 text-weight-bold brand-heading')
            with ui.row().classes('items-center q-gutter-sm'):
                ui.label(f'User: {app.storage.user["username"]}').classes('text-subtitle2')

                def sign_out() -> None:
                    app.storage.user.clear()
                    ui.navigate.to('/')

                ui.button('Sign Out', on_click=sign_out).props('flat color=white no-caps')

    with ui.column().classes('app-shell q-py-xl q-gutter-lg'):
        ui.label('User Workspace').classes('section-label')
        ui.label('This is the signed-in layout. The floating action button opens the menu that will hold user and admin navigation.').classes(
            'text-h5 text-weight-bold brand-heading'
        )
        with ui.row().classes('q-col-gutter-lg w-full'):
            with ui.card().classes('surface-card col-12 col-md-7 q-pa-lg'):
                ui.label('Planned user workflows').classes('text-h6 text-weight-bold brand-heading')
                ui.markdown(
                    '- Browse the catalog and search by title or author\n'
                    '- Check books out and check them back in\n'
                    '- Track due dates and availability counts\n'
                    '- View a member account and borrowing history'
                )
            with ui.card().classes('surface-card col-12 col-md-5 q-pa-lg'):
                ui.label('Planned admin workflows').classes('text-h6 text-weight-bold brand-heading')
                ui.markdown(
                    '- Create, update, and remove books\n'
                    '- Adjust total inventory counts\n'
                    '- Review active checkouts\n'
                    '- Manage user roles'
                )

        with ui.card().classes('surface-card q-pa-lg'):
            ui.label('Current featured inventory').classes('text-h6 text-weight-bold brand-heading q-mb-md')
            with ui.element('div').classes('books-grid'):
                for book in featured_books()[:3]:
                    create_book_card(book)


if __name__ in {'__main__', '__mp_main__'}:
    initialize_database()
    ui.run(
        title='ShelfWise Library',
        favicon=build_favicon_data_uri(),
        storage_secret='library-homework-secret',
        reload=True,
    )

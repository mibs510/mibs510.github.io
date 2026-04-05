from nicegui import app, ui

from models import featured_books, get_user_by_username, initialize_database
from ui_components import GLOBAL_CSS, create_book_card, create_footer, create_header, create_homepage


def add_global_styles() -> None:
    ui.add_head_html(f'<style>{GLOBAL_CSS}</style>')


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

    with ui.column().classes('app-shell items-center q-py-xl'):
        with ui.card().classes('surface-card q-pa-xl').style('width: min(460px, 100%);'):
            ui.label('Prototype Login').classes('text-h4 text-weight-bold brand-heading')
            ui.label(
                'This is a temporary sign-in flow so we can demonstrate the authenticated layout and floating menu.'
            ).classes('text-body1 text-grey-7 q-mb-md')
            username = ui.input('Username', value='student').props('outlined')
            ui.input('Password', value='demo').props('outlined type=password')

            def sign_in() -> None:
                account = get_user_by_username(username.value.strip() or 'student')
                if account is None:
                    ui.notify('User not found in the local database.', color='negative')
                    return

                app.storage.user['username'] = account.username
                app.storage.user['role'] = 'admin' if account.is_admin else 'member'
                ui.notify(f'Signed in as {account.username}', color='positive')
                ui.navigate.to('/app')

            ui.button('Enter library app', on_click=sign_in).props('unelevated no-caps').classes('full-width q-mt-md primary-button')
            ui.label('Demo accounts seeded through the ORM: student and admin. Password validation is not implemented yet.').classes(
                'text-caption text-grey-7 q-mt-md'
            )


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
        storage_secret='library-homework-secret',
        reload=True,
    )

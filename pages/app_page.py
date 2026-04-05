from nicegui import app, ui

from app_state import add_global_styles, require_login
from ui_components import create_app_page


@ui.page('/app')
def app_page() -> None:
    add_global_styles()
    if not require_login():
        return

    def sign_out() -> None:
        app.storage.user.clear()
        ui.navigate.to('/')

    create_app_page(sign_out)

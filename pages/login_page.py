from nicegui import ui

from app_state import add_global_styles
from ui_components import create_login_page


@ui.page('/login')
def login_page() -> None:
    add_global_styles()
    create_login_page()

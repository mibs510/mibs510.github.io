from nicegui import ui

from app_state import add_global_styles
from ui_components import create_homepage


@ui.page('/')
def home_page() -> None:
    add_global_styles()
    create_homepage()

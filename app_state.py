from nicegui import app, ui

from ui_components import GLOBAL_CSS


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


def user_is_logged_in() -> bool:
    return bool(app.storage.user.get('username'))


def require_login() -> bool:
    if not user_is_logged_in():
        ui.notify('Use the demo login first.', color='warning')
        ui.navigate.to('/login')
        return False
    return True

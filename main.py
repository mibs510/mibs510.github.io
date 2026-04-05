import pages

from nicegui import ui

from models import initialize_database
from ui_components import build_favicon_data_uri


if __name__ in {'__main__', '__mp_main__'}:
    initialize_database()
    ui.run(
        title='ShelfWise Library',
        favicon=build_favicon_data_uri(),
        storage_secret='library-homework-secret',
        reload=True,
    )

from __future__ import annotations

from sqlalchemy import func, select

from models.database import Base, SessionLocal, engine
from models.entities import Book, User


BOOK_SEED_DATA = [
    {
        'title': 'The Midnight Catalog',
        'author': 'R. Elkins',
        'summary': 'A quiet archivist discovers that every missing book in the city is connected to a forgotten branch library below the train station.',
        'rating': 4.8,
        'total_copies': 6,
        'available_copies': 4,
        'cover_color': 'linear-gradient(160deg, #143642 0%, #27566b 100%)',
    },
    {
        'title': 'Atlas of Borrowed Worlds',
        'author': 'Mina Sol',
        'summary': 'A speculative adventure that follows a student courier delivering rare texts between impossible libraries built in parallel cities.',
        'rating': 4.6,
        'total_copies': 5,
        'available_copies': 2,
        'cover_color': 'linear-gradient(160deg, #3b1f2b 0%, #8a4f5d 100%)',
    },
    {
        'title': 'The Last Due Date',
        'author': 'J. Hart',
        'summary': 'Part campus drama and part mystery, this novel revolves around an overdue manuscript that changes hands once every decade.',
        'rating': 4.4,
        'total_copies': 8,
        'available_copies': 7,
        'cover_color': 'linear-gradient(160deg, #4f3824 0%, #bc8a5f 100%)',
    },
]


def initialize_database() -> None:
    Base.metadata.create_all(engine)

    with SessionLocal() as session:
        existing_books = session.scalar(select(func.count(Book.id))) or 0
        if existing_books == 0:
            session.add_all(Book(**book_data) for book_data in BOOK_SEED_DATA)

        existing_users = {user.username for user in session.scalars(select(User)).all()}
        if 'student' not in existing_users:
            session.add(User(username='student', password_hash='demo-password-placeholder', is_admin=False))
        if 'admin' not in existing_users:
            session.add(User(username='admin', password_hash='demo-password-placeholder', is_admin=True))

        session.commit()


def featured_books() -> list[Book]:
    with SessionLocal() as session:
        return list(
            session.scalars(
                select(Book)
                .order_by(Book.rating.desc(), Book.title.asc())
                .limit(6)
            ).all()
        )


def get_user_by_username(username: str) -> User | None:
    with SessionLocal() as session:
        return session.scalar(select(User).where(User.username == username))

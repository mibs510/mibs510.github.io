# ShelfWise Library App

ShelfWise is a NiceGUI-based library management system prototype for a homework assignment. The app currently focuses on establishing a clean UI foundation and a simple data model that can grow into book browsing, checkout/check-in flows, inventory tracking, and administrator CRUD tools.

## Current Tech Stack

- Python
- NiceGUI
- SQLite
- SQLAlchemy ORM

## Project Goals

The intended application scope includes:

- Browsing a book catalog
- User accounts
- Checking books out and checking them back in
- Tracking book inventory and availability
- Administrator tools for creating, updating, and deleting books

This project is local-only and intentionally simple. SQLite is used as the database because the app is not intended for public deployment.

## Current Objects

The app currently defines two ORM models in [main.py](C:/Users/Connor/SynologyDrive/CSUEB/CS%20351/mibs510.github.io/main.py):

### `User`

Represents a library account.

Current fields:

- `id`
- `username`
- `password_hash`
- `is_admin`
- `created_at`

Current usage:

- Seeds demo accounts for `student` and `admin`
- Supports the prototype login flow
- Determines whether the signed-in user should see admin menu items

### `Book`

Represents a catalog item in the library.

Current fields:

- `id`
- `title`
- `author`
- `summary`
- `rating`
- `total_copies`
- `available_copies`
- `cover_color`
- `created_at`

Current usage:

- Seeds homepage/demo inventory
- Drives the featured book cards on the landing page
- Supplies sample inventory data in the signed-in area

## Current Application Structure

At the moment, the app is still intentionally compact and lives mostly in a single file:

- [main.py](C:/Users/Connor/SynologyDrive/CSUEB/CS%20351/mibs510.github.io/main.py)
  Contains:
  - SQLAlchemy configuration
  - ORM models
  - database initialization and seed logic
  - shared UI styling
  - homepage layout
  - prototype login page
  - authenticated app shell with floating menu
- [requirements.txt](C:/Users/Connor/SynologyDrive/CSUEB/CS%20351/mibs510.github.io/requirements.txt)
  Lists the current Python dependencies
- [library.db](C:/Users/Connor/SynologyDrive/CSUEB/CS%20351/mibs510.github.io/library.db)
  SQLite database created locally by the app

## Current Pages

### `/`

Landing page with:

- top header
- hero section
- placeholder for a future hero image
- featured book cards
- footer

### `/login`

Prototype login page with:

- username input
- placeholder password input
- database-backed lookup for seeded users

This is not a secure authentication system yet. It is only a temporary scaffold.

### `/app`

Signed-in user workspace with:

- authenticated header
- floating button that opens a drawer menu
- placeholder sections for member workflows
- placeholder sections for admin workflows
- sample featured inventory cards

## Database Initialization

When the app runs directly, it:

1. Creates the SQLite tables for the ORM models if they do not exist.
2. Seeds sample book data if the database is empty.
3. Seeds two demo users:
   - `student`
   - `admin`

Startup is protected by a `__main__` guard so the models can be imported without launching the web server.

## Current Limitations

The following features are not implemented yet:

- real password hashing and authentication
- checkout/check-in records as an ORM model
- search and filtering
- book CRUD forms
- user management screens
- due dates and borrowing history
- database relationships between users and checkouts

## Running the App

Install dependencies:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Run the app:

```powershell
.venv\Scripts\python.exe main.py
```

## Likely Next Steps

- Move ORM models into a dedicated `models.py`
- Add a `Checkout` model and relationships
- Build catalog browsing and book detail pages
- Implement admin CRUD for books
- Replace the prototype login with real authentication

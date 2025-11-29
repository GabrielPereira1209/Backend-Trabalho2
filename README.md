# Backend - Parking API

This is a Django REST backend for the Parking project used by the frontend.

Quick start (development):

- Create a Python 3.12 venv and install requirements:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

- Endpoints:
  - `POST /api/auth/register` - register
  - `POST /api/auth/login` - login (returns `access_token`)
  - `GET /api/auth/me` - get current user
  - `PUT /api/auth/profile` - update profile
  - `POST /api/auth/change-password` - change password
  - `POST /api/auth/forgot-password` - forgot password (demo)
  - `GET /api/spots/` - list spots
  - `POST /api/spots/` - create spot (auth)
  - `GET /api/spots/my-spots/` - list current user's spots
  - `GET /api/rentals/` - list rentals for user
  - `POST /api/rentals/` - create rental
  - `GET /swagger/` - API docs

Notes:
- The project uses an SQLite DB by default for simplicity.
- For sending real emails (forgot-password), configure email backend in `project/settings.py`.

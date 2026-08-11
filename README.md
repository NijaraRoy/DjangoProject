# DjangoProject — Loginify (Login System)

A Django project implementing user signup, login, profile update, and account
deletion. It exposes the same functionality through two interfaces: server-rendered
HTML pages for browser use, and a JSON CRUD API for tools like Postman.

## Tech stack

- **Django 6.0** — web framework (ORM, views, templates, URL routing, admin, sessions)
- **Django REST Framework (DRF)** — serializers used by the JSON CRUD endpoints
- **SQLite** — local database (`db.sqlite3`)
- **Plain CSS** — no frontend framework; a single stylesheet served via Django's static files app

## Project setup

```bash
python -m venv DjangoAssignment          # create a virtual environment
DjangoAssignment\Scripts\activate        # activate it (Windows)
pip install django djangorestframework   # install Django + DRF inside the venv
django-admin startproject LoginSystem    # create the project
cd LoginSystem
python manage.py startapp Loginify       # create the app inside the project
```

`LoginSystem` is the Django project (settings, root URL configuration).
`Loginify` is the app that implements signup, login, and user CRUD.

## Project structure

```
DjangoProject/
├── DjangoAssignment/              # virtual environment
└── LoginSystem/                   # Django project root
    ├── manage.py                  # Django CLI entrypoint
    ├── db.sqlite3                 # local database file
    ├── LoginSystem/                # project-level config package
    │   ├── settings.py            # project configuration
    │   ├── urls.py                # root URL routing (includes Loginify's URLs)
    │   ├── wsgi.py / asgi.py      # deployment entrypoints
    ├── Loginify/                   # app: users, auth, CRUD
    │   ├── models.py              # UserDetails model
    │   ├── forms.py               # SignupForm, LoginForm, UpdateForm
    │   ├── views.py               # request-handling logic (HTML pages + JSON API)
    │   ├── urls.py                # app-level URL routing
    │   ├── serializers.py         # DRF serializer for the JSON API
    │   ├── admin.py               # registers UserDetails with Django admin
    │   ├── migrations/            # schema change history
    │   ├── static/loginify/css/style.css   # stylesheet
    │   └── templates/loginify/    # HTML templates
    └── Screenshots/               # screenshots for submission
```

## Models

`UserDetails`:
| Field | Type | Notes |
|---|---|---|
| `username` | `CharField(max_length=50)` | primary key |
| `email` | `EmailField` | unique |
| `password` | `CharField(max_length=255, blank=True)` | stores a hashed password, not plaintext |

Note: the password field is `max_length=255` rather than a shorter value, since
passwords are hashed with Django's `make_password()` (PBKDF2) before being
stored, and a hash is 70+ characters.

## Views

**Browser-facing (HTML):**
- `signup_view` — GET renders `SignupForm`; POST validates, hashes the password, creates the user, and redirects to login.
- `login_view` — GET renders `LoginForm`; POST validates credentials and, on success, stores the user's email in the session and renders a success page.
- `update_user_view(email)` — requires the logged-in session's email to match the URL's email; GET renders a pre-filled `UpdateForm`, POST applies changes (re-hashing any new password) and redirects to login.
- `delete_user_view(email)` — same session check; GET shows a confirmation page, POST deletes the account.

**API-facing (JSON, used with Postman):**
- `get_all_users` — GET lists all users, POST creates a user, via `UserDetailsModelSerializer`.
- `get_user_by_email(email)` — GET retrieves one user, PUT updates one, DELETE removes one.

The API views are decorated `@csrf_exempt` since Postman requests don't carry
Django's CSRF token; the browser-facing views rely on the normal CSRF
protection instead.

## Forms

- `SignupForm` — a `ModelForm` for `UserDetails`, plus a `confirm_password`
  field; validates that the email isn't already registered and that both
  password fields match.
- `LoginForm` — plain form with `email` and `password`.
- `UpdateForm` — optional `email`/`password` fields (a user may change either
  or both); validates that at least one is provided and that a changed email
  isn't already in use by another account.

## URLs

| Path | View | Purpose |
|---|---|---|
| `/loginify/hello/` | `hello_world` | plaintext test endpoint |
| `/loginify/signup/` | `signup_view` | signup form |
| `/loginify/login/` | `login_view` | login form |
| `/loginify/users/` | `get_all_users` | list/create users (JSON) |
| `/loginify/user/<email>/` | `get_user_by_email` | get/update/delete one user (JSON) |
| `/loginify/update/<email>/` | `update_user_view` | update profile (HTML) |
| `/loginify/delete/<email>/` | `delete_user_view` | delete account (HTML) |

## Templates

- `base.html` — shared layout (styling, branding, flash-message rendering) extended by every page.
- `login.html` / `signup.html` — render their respective forms.
- `success.html` — shown after a successful login; links to update/delete.
- `update.html` — renders the update form.
- `delete_confirm.html` — confirmation step before account deletion.

## How to run

```bash
cd LoginSystem
DjangoAssignment\Scripts\python.exe manage.py makemigrations
DjangoAssignment\Scripts\python.exe manage.py migrate
DjangoAssignment\Scripts\python.exe manage.py createsuperuser
DjangoAssignment\Scripts\python.exe manage.py runserver
```

Then visit `http://127.0.0.1:8000/loginify/signup/` in a browser, or use
`http://127.0.0.1:8000/loginify/users/` etc. from Postman for the JSON API.
Django admin is available at `http://127.0.0.1:8000/admin/`.

## Screenshots

Located in `LoginSystem/Screenshots/`:
- Signup, Login, Success, Update template screenshots
- Postman: signup, login, get-all-users, update, delete response screenshots
- Superuser verification screenshot

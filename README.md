# DjangoProject

This project demonstrates a Django-based login system with signup, login, profile management, and account deletion.

## Features
- User registration via signup page and API-style POST flow
- User login using Django authentication
- Profile retrieval and profile update
- Account deletion endpoint
- Django templates for the key user-interaction screens
- Postman-ready JSON responses for CRUD-style testing

## Project structure
- `DjangoProject/` – Django settings and URL configuration
- `accounts/` – authentication and profile logic
- `templates/accounts/` – HTML templates for signup and login

## Run locally
```bash
python manage.py migrate
python manage.py runserver
```

## Example endpoints
- `GET /signup/` – display signup form
- `POST /signup/` – create a new user
- `GET /login/` – display login form
- `POST /login/` – authenticate and log in a user
- `GET /profile/` – fetch the logged-in profile
- `POST /profile/` – update profile details
- `POST /delete-account/` – delete the logged-in account

## Screenshots
Add screenshots of the templates and Postman responses here after running the app.

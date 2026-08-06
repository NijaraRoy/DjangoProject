# DjangoProject

This project is a Django-based login system developed to support user signup, login, retrieval, update, and deletion workflows. The application uses Django models, views, URL routing, and HTML templates to manage user data.

## Project Objective
The project demonstrates a complete login and user management workflow with:
- User signup
- User login
- User retrieval
- User update
- User delete
- Django admin access
- CRUD verification through Postman

## Project Setup
1. Create a virtual environment named `DjangoAssignment`
2. Activate the virtual environment
3. Install Django inside the environment
4. Create a Django project named `LoginSystem`
5. Create a Django app named `Loginify`

## Project Structure
- `LoginSystem/` - main project folder
- `Loginify/` - application handling signup, login, and CRUD logic
- `templates/loginify/` - HTML templates for signup, login, success, and update
- `db.sqlite3` - local database

## Features
- Signup page to register users
- Login page to verify user credentials
- Success page after login
- Read-all-users API endpoint
- Read-single-user-by-email API endpoint
- Update-user API endpoint
- Delete-user API endpoint
- Django admin integration

## Models
The model used in the project is `UserDetails` with fields:
- `username` - primary key, max length 50
- `email` - unique email
- `password` - max length 12

## URLs
The app exposes the following routes:
- `/loginify/hello/`
- `/loginify/signup/`
- `/loginify/login/`
- `/loginify/users/`
- `/loginify/user/<email>/`
- `/loginify/user/update/<email>/`
- `/loginify/user/delete/<email>/`

## Views
The following views are implemented:
- `hello_world`
- `signup_view`
- `login_view`
- `get_all_users`
- `get_user_by_email`
- `update_user`
- `delete_user`

## Screenshots
The following screenshots should be added for submission:
- Signup template screenshot
- Login template screenshot
- Success template screenshot
- Update template screenshot
- Postman signup response screenshot
- Postman login response screenshot
- Postman get all users response screenshot
- Postman update response screenshot
- Postman delete response screenshot

## Verification
The project was verified through:
- Django system checks
- Live endpoint testing
- Admin URL verification


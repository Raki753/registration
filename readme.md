# Fullstack Registration CRUD App

This is a fullstack user registration CRUD application built using Django for the backend and HTML/CSS for the frontend.

## Features

- Add a new user (Name, Email, Date of Birth,Gender,Phone number)
- View list of registered users
- Update user information
- Delete a user
- Simple, responsive frontend using HTML and CSS
- Django-based backend with SQLite database (can be changed to MySQL/PostgreSQL)

---

## Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS
- Database: SQLite (default)

---
## Steps To Run The code

- Copy the project link: https://github.com/Raki753/registration.git
- Open Terminal and Clone The Repository: git clone https://github.com/Raki753/registration.git
- cd registration (if its in other dir)
- Run The development Server: python manage.py runserver

---

## Project Structure

registration_project/
├── registration_project/          # Django project settings
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── registration_app/              # Django app
│   ├── migrations/                # Database migrations
│   │   └── init.py
│   ├── templates/                 # HTML templates
│   │   ├── user_list.html
│   │   ├── user_form.html
│   │   └── user_confirm_delete.html
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── db.sqlite3                     # Default SQLite DB (optional: use MySQL/PostgreSQL)
├── manage.py                      # Django management script
├── README.md                      # Project overview and instructions

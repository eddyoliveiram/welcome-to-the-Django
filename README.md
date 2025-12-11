# Welcome to the Djungle

> A Django example project: a blog with users, posts, and comments.

## Features

- 👥 User authentication and profiles
- 📝 Create, edit, and delete posts
- 💬 Create, edit, and delete comments
- 🔒 Posts and comments can only be edited/deleted by their authors
- 📱 Responsive design with Bootstrap 5
- 🎨 Modern UI with smooth interactions

## Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Run migrations to create the database:

```bash
python manage.py migrate
```

3. Start the development server:

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Default Users

The database is pre-populated with 3 test users, 10 posts, and 10 comments:

| Username | Email | Name | Password |
|----------|-------|------|----------|
| user1 | user1@example.com | João Silva | password123 |
| user2 | user2@example.com | Maria Santos | password123 |
| user3 | user3@example.com | Pedro Oliveira | password123 |

## Admin Access

To create a superuser for Django admin:

```bash
python manage.py createsuperuser
```

Then access the admin panel at `http://127.0.0.1:8000/admin/`

## Project Structure

```
WelcomeToTheJungle/
├── config/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog/                # Blog app
│   ├── models.py        # Post and Comment models
│   ├── views.py         # Application views
│   ├── forms.py         # Django forms
│   ├── urls.py          # URL routing
│   ├── admin.py         # Admin configuration
│   └── migrations/      # Database migrations
├── templates/           # HTML templates
├── manage.py            # Django management
└── requirements.txt     # Project dependencies
```

## Technologies

- Django 4.2
- Bootstrap 5
- SQLite3
- Python 3.8+

## License

This project is open source and available under the MIT License.
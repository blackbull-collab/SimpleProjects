# Django Polls Application

This repository contains a **simple Polls web application** developed by following the **official Django tutorial**.  
The project is created for learning and practice purposes to understand Django fundamentals.

---

## 📘 Tutorial Reference

This project is based on the official Django documentation:

https://docs.djangoproject.com/en/stable/intro/tutorial01/

---

## 🎯 Purpose of This Project

The goal of this project is to learn and demonstrate:

- Django project & app structure
- Models and database migrations
- Views and URL routing
- Templates and template rendering
- Django Admin interface
- Handling forms and user input

---

## ✨ Application Features

- Display poll questions
- Vote on available choices
- View poll results
- Admin panel for managing polls

---

## 🛠️ Tech Stack

- **Python**
- **Django**
- **SQLite** (default Django database)

---

## 📁 Project Structure

```
mysite/
├── manage.py
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── polls/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
└── README.md
```


## ▶️ How to Run This Project Locally

## 1. Clone the repository
```
git clone https://github.com/blackbull-collab/Very-simple-Django-polls-app.git
```


## 2. Navigate to the project directory
```
cd Very-simple-Django-polls-app
```


## 3. (Optional) Create and activate a virtual environment
```
python -m venv venv
venv\Scripts\activate
```


## 4. Install Django
```
pip install django
```


## 5. Apply database migrations
```
python manage.py migrate
```


## 6. Create a superuser (for admin access)
```
python manage.py createsuperuser
```

## 7. Run the development server
```
python manage.py runserver
```


## 🌐 Access the Application
```
Polls App:
http://127.0.0.1:8000/polls/

Admin Panel:
http://127.0.0.1:8000/admin/
```


## ⚠️ Disclaimer
```
This project is strictly for educational purposes and follows the official Django tutorial.
All core concepts and examples are credited to the Django Software Foundation.

```


## 👤 Author

```
Vinoth
GitHub: https://github.com/blackbull-collab
```


## ✅ Next Steps (Optional but Recommended)
```
After adding this README:


git add README.md
git commit -m "Add project README"
git push -u origin main

```

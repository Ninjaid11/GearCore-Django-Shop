---

# GearCore Shop 🛒

**What is this?**
A simple online store backend built with Django + PostgreSQL. Users browse products, comment, add to cart, and place orders. Authentication handled by django-allauth 🔐.

---

## Features ✨

* Browse products by brand & category 🔍
* Product pages + user comments 💬
* Cart works for logged-in users & guests 🛍️
* Place orders + get email confirmation 📧
* User profile: update info & view order history 👤
* Change password with email notification 🔑
* User registration/login via **django-allauth**
* Logs key actions & shows friendly messages 📋

---

## Tech Stack 🛠️

* Python & Django
* PostgreSQL
* django-allauth (auth & registration)
* SMTP email for notifications
* Django messages framework

---

## Quick Start 🚀

```bash
git clone https://github.com/Ninjaid11/GearCore.git
cd gearcore_shop
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
# configure settings.py (DB, email, secret key)
python manage.py migrate
python manage.py runserver
```

Open: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ⚙️ Environment Setup (.env)

This project uses a `.env` file to keep sensitive data safe (like database credentials, secret keys, and email settings).
Make sure you create a `.env` file in the project root with all required variables before running the app! 🔐

Example `.env` variables you might need:

```env
SECRET_KEY=your_secret_key_here
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/dbname
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
DEFAULT_FROM_EMAIL=your_email@example.com
```

Without `.env` or proper environment variables, the app **won't work properly** ⚠️

---

## How it works ⚙️

* Browse & search products
* Add comments on product pages
* Add/remove/change product quantities in cart
* Place orders with confirmation emails
* Manage user profile & password
* Auth via django-allauth with email verification

---

# 🛒 GearCore Django Shop

![GearCore Logo](images/favicon.ico)

Django e-commerce shop with support for shopping cart, orders, users and admin panel.
 
The project is implemented as a backend practice using Django, PostgreSQL and Docker.
The main focus is working with databases, user authentication and building e-commerce logic.
 
---
 
# Features
 
Product catalog with categories and brands
Shopping cart (for guests and authenticated users)
Product comments
Order checkout
Email notifications for orders
User profile and order history
Registration and authentication (django-allauth)
Data storage in PostgreSQL
Full Docker support
 
---
 
# Technologies
 
Python 3.11
Django
PostgreSQL 15
django-allauth
SMTP (email notifications)
Docker & Docker Compose
 
---
 
# Environment Setup
 
Before running the project, you MUST create a `.env` file in the project root.
 
Without it, the application will NOT be able to start, as there are no database, Django and email settings.
 
---
 
# Required Step
 
# Example `.env`
 
Open the `.env` file and fill it in:
 
```env
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
 
DB_NAME=mydb
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=db
DB_PORT=5432
 
EMAIL_HOST_USER=example@gmail.com
EMAIL_HOST_PASSWORD=your_password
DEFAULT_FROM_EMAIL=example@gmail.com
```
 
---
 
# Important
 
.env file is NOT stored in the repository
it is created locally by each user
without it the application will NOT be able to connect to the database
incorrect configuration will result in a startup error
 
---
 
# Full Project Launch
 
1. Clone the repository
```bash
git clone https://github.com/Ninjaid11/GearCore-Django-Shop.git
cd gearcore_shop
```
 
---
 
2. Run containers
```bash
docker compose up --build
```
 
---
 
3. Apply migrations
```bash
docker compose exec web python manage.py migrate
```
 
---
 
4. Create administrator
```bash
docker compose exec web python manage.py createsuperuser
```
 
---
 
# Access to the application
 
Website: http://localhost:8000
Admin panel: http://localhost:8000/admin
 
---
 
# Project Architecture
 
Django runs in the `web` container
PostgreSQL runs in the `db` container
Connection via Docker network (db:5432)
Data is stored in Docker volume
Migrations create the database structure

---
 
# Notes
 
The project is designed for development (development mode)
DEBUG=True is enabled by default
For production you need:
 
Gunicorn
Nginx
disable DEBUG
secure .env
 
---
 
# Project Goal
 
The project was created for backend development practice:
 
Django ORM and working with models
Building e-commerce logic
Working with Docker and PostgreSQL
User authentication
Architecture of a real backend project
 
---

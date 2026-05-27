# 🛒 GearCore Django Shop

![GearCore Logo](images/favicon.ico)

Django интернет-магазин с поддержкой корзины, заказов, пользователей и административной панели.

Проект реализован как backend-практика с использованием **Django**, **PostgreSQL** и **Docker**.
Основной фокус — работа с базой данных, авторизация пользователей и построение e-commerce логики.

---

# 🚀 Возможности

* 📦 Каталог товаров с категориями и брендами
* 🛍 Корзина (для гостей и авторизованных пользователей)
* 💬 Комментарии к товарам
* 📑 Оформление заказов
* 📧 Email-уведомления о заказах
* 👤 Профиль пользователя и история заказов
* 🔐 Регистрация и авторизация (django-allauth)
* 🗄 Хранение данных в PostgreSQL
* 🐳 Полная поддержка Docker

---

# ⚙️ Технологии

* 🐍 Python 3.11
* 🎯 Django
* 🐘 PostgreSQL 15
* 🔐 django-allauth
* 📨 SMTP (email-уведомления)
* 🐳 Docker & Docker Compose

---

# ⚙️ Environment Setup

Перед запуском проекта **обязательно необходимо создать `.env` файл** в корне проекта.

Без него приложение **не сможет запуститься**, так как отсутствуют настройки базы данных, Django и email.

---

## ⚠️ Обязательный шаг

## 📄 Пример `.env`

Откройте файл `.env` и заполните его:

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

## ❗ Важно

* `.env` файл **не хранится в репозитории**
* он создаётся локально каждым пользователем
* без него приложение **не сможет подключиться к базе данных**
* неправильная конфигурация приведёт к ошибке запуска

---

# 🐳 Полный запуск проекта

## 1️⃣ Клонирование репозитория

```bash
git clone https://github.com/Ninjaid11/GearCore-Django-Shop.git
cd gearcore_shop
```

---

## 2️⃣ Запуск контейнеров

```bash
docker compose up --build
```

---

## 3️⃣ Применение миграций

```bash
docker compose exec web python manage.py migrate
```

---

## 4️⃣ Создание администратора

```bash
docker compose exec web python manage.py createsuperuser
```

---

# 🌐 Доступ к приложению

* 🏠 Сайт: [http://localhost:8000](http://localhost:8000)
* ⚙️ Админка: [http://localhost:8000/admin](http://localhost:8000/admin)

---

# 🧠 Архитектура проекта

* Django работает в контейнере `web`
* PostgreSQL работает в контейнере `db`
* Связь через Docker network (`db:5432`)
* Данные сохраняются в Docker volume
* Миграции создают структуру базы данных

---

# 🗄 База данных

* PostgreSQL 15
* Persistent volume: `postgres_data`
* Изолированная Docker среда

---

# 📌 Примечания

* Проект предназначен для разработки (development mode)
* `DEBUG=True` включён по умолчанию
* Для production требуется:

  * Gunicorn
  * Nginx
  * отключение DEBUG
  * безопасный `.env`

---

# 💡 Цель проекта

Проект создан для практики backend-разработки:

* Django ORM и работа с моделями
* Построение e-commerce логики
* Работа с Docker и PostgreSQL
* Авторизация пользователей
* Архитектура реального backend-проекта

---
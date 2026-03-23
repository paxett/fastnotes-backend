# FastNotes Backend 🚀

Учебный проект персональных заметок на современном стеке Python. Реализован полный цикл CRUD (создание, чтение, обновление, удаление) с использованием асинхронности и контейнеризации.

## Стек технологий
*   **Фреймворк:** [FastAPI](https://fastapi.tiangolo.com) (Async)
*   **База данных:** PostgreSQL 15
*   **ORM:** SQLAlchemy 2.0 + [asyncpg](https://magicstack.github.io)
*   **Миграции:** Alembic
*   **Контейнеризация:** Docker & Docker Compose
*   **Валидация:** Pydantic v2

## Как запустить проект

### 1. Клонирование репозитория
```bash
git clone https://github.com
cd fastnotes-backend
```

### 2. Настройка окружения
Создайте файл .env в корне проекта и добавьте туда настройки (пример):
```text
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_DB=myapp_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

SECRET_KEY=5ab0dcf21f6b6c8069bd2bf4af123670b70bd9cff56de2e2e8a2d053c6036757
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

SUPERUSER_EMAIL=admin@example.com
SUPERUSER_PASSWORD=admin_pwd
```

### 3. Запуск в Docker (Settings.DEBUG=False)
Проект настроен на автоматическое применение миграций при старте.
```bash
docker-compose up --build
```

### 3. Запуск в Idea (Settings.DEBUG=True)
1. Запуск db контейнера:
```bash 
docker-compose up --build db
```
2. Применение alembic миграции и создание суперюзера:
```bash 
   alembic upgrade head && python -m app.initial_data
```
3. Запуск через конфигурацию fast-notes.run.xml в Idea

## 🔐 Доступы (Swagger)

После запуска перейдите на: [http://localhost:8000/docs](http://localhost:8000/docs)
1. Зарегистрируйтесь через `/register`.
2. Нажмите **Authorize** сверху, введите Email и Пароль.
3. Теперь вы можете создавать и видеть только свои заметки.

## 🛠 Быстрые команды

### Контейнеры (Docker)
* `docker compose up -d` — запустить проект в фоне
* `docker compose up --build` — пересобрать (после правки requirements.txt)
* `docker compose logs -f web` — смотреть "живые" логи приложения
* `docker compose down -v` — **СБРОС**: удалить контейнеры и данные базы

### База данных (Alembic)
* `docker compose exec web alembic revision --autogenerate -m "Init"` — создать миграцию
* `docker compose exec web alembic upgrade head` — применить миграции (обновить таблицы)
* `docker compose exec web python -m app.initial_data` — создать админа вручную

---

## 📂 Структура проекта

| Файл / Папка | Описание |
| :--- | :--- |
| **app/main.py** | Точка входа, подключение роутеров FastAPI |
| **app/database.py** | Настройка асинхронного движка SQLAlchemy |
| **app/models/** | Таблицы БД (User, Note) |
| **app/schemas/** | Валидация данных Pydantic |
| **app/api/v1/** | Эндпоинты (логика заметок и пользователей) |
| **app/api/deps.py** | Зависимости (проверка токенов, права доступа) |
| **app/core/** | Безопасность (JWT, хеширование паролей) |
| **.env** | Секретные ключи и пароли к БД |

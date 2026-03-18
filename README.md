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
POSTGRES_HOST=db
POSTGRES_PORT=5432
DATABASE_URL=postgresql+asyncpg://myuser:mypassword@db:5432/myapp_db
```

### 3. Запуск в Docker
Проект настроен на автоматическое применение миграций при старте.
```bash
docker-compose up --build
```

После запуска API будет доступно по адресу: http://localhost:8000

### Документация API
FastAPI автоматически генерирует интерактивную документацию:
Swagger UI: http://localhost:8000/docs — здесь можно потестировать все эндпоинты (GET, POST, PATCH, DELETE).
ReDoc: http://localhost:8000/redoc

### Структура проекта
app/api/ — маршруты (endpoints) приложения.
app/models/ — таблицы базы данных (SQLAlchemy).
app/schemas/ — схемы валидации данных (Pydantic).
app/database.py — конфигурация подключения к БД.
app/main.py — точка входа в приложение.


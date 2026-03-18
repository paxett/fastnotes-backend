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

SUPERUSER_EMAIL=admin@example.com
SUPERUSER_PASSWORD=admin_pwd
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
app/main.py	          Точка входа, подключение роутеров и запуск FastAPI.
app/database.py	      Настройка асинхронного движка и сессий SQLAlchemy.
app/config.py	        Чтение переменных из .env через Pydantic Settings.
app/models/	          Структура таблиц БД (SQLAlchemy классы).
app/schemas/	        Правила валидации входящих/исходящих JSON (Pydantic).
app/api/v1/	          Бизнес-логика: эндпоинты для заметок и пользователей.
app/api/deps.py	      Зависимости: получение юзера из токена, проверка прав.
app/core/security.py	Инструменты: хеширование паролей и работа с JWT.
.env	                Твои секреты: пароль к базе и секретный ключ JWT.

🔥 Шпаргалка по управлению проектом
🐳 Docker Compose (Инфраструктура)
docker compose up -d — запустить проект в фоне.
docker compose up --build — пересобрать образы (нужно, если обновил requirements.txt).
docker compose logs -f web — смотреть «живые» логи приложения.
docker compose down — остановить проект.
docker compose down -v — СБРОС: удалить всё (контейнеры, базу, таблицы и данные).
🛠 Alembic (Миграции базы данных)
docker compose exec web alembic revision --autogenerate -m "Init" — создать «чертеж» новой миграции (после изменений в models/).
docker compose exec web alembic upgrade head — применить все миграции (создать/обновить таблицы в БД).
docker compose exec web alembic history — посмотреть список всех созданных миграций.
👤 Пользователи и скрипты
docker compose exec web python -m app.initial_data — запустить скрипт создания админа вручную.



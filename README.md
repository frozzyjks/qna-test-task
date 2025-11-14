# QnA API

Готовая реализация тестового задания (API для вопросов и ответов).

## Запуск через Docker Compose

1. Построить и запустить контейнеры:
```bash
docker-compose up --build
```

2. API: http://localhost:8000
   Docs: http://localhost:8000/docs

## Примечание о миграциях

База данных создаётся автоматически при запуске приложения с помощью:
`SQLModel.metadata.create_all(engine)`

## Tests

Для запуска тестов локально (нужен запущенный PostgreSQL и переменная окружения DATABASE_URL):
```bash
pytest
```


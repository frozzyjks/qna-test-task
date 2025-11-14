# QnA API (FastAPI + SQLModel, no Alembic)

This is a ready-to-run implementation of the test task (questions & answers API) without Alembic.
It uses SQLModel's `create_all()` to create tables automatically at startup (so no migrations).

## Run with Docker Compose

1. Build and start:
```bash
docker-compose up --build
```

2. API: http://localhost:8000
   Docs: http://localhost:8000/docs

## Notes about migrations

This project **does not** use Alembic. It creates DB tables automatically on startup:
`SQLModel.metadata.create_all(engine)`. This is fine for small test projects but:
- There are no migration history or safe schema upgrades.
- For production, add Alembic or another migration tool.

## Tests

Run tests locally (requires PostgreSQL running and DATABASE_URL set accordingly):
```bash
pytest
```


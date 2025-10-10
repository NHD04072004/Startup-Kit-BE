.PHONY: help build up down logs shell test clean migration migrate

help:
	@echo "Available commands:"
	@echo "  make build        - Build Docker images"
	@echo "  make up           - Start containers in development mode"
	@echo "  make up-prod      - Start containers in production mode"
	@echo "  make down         - Stop and remove containers"
	@echo "  make logs         - View container logs"
	@echo "  make shell        - Access app container shell"
	@echo "  make db-shell     - Access database shell"
	@echo "  make migrate      - Run database migrations"
	@echo "  make migration    - Create new migration"
	@echo "  make test         - Run tests"
	@echo "  make clean        - Remove all containers, volumes, and images"

build:
	docker-compose build

up:
	docker-compose up -d
	@echo "Application started at http://localhost:8000"

up-prod:
	docker-compose -f docker-compose.prod.yml up -d
	@echo "Application started in production mode"

down:
	docker-compose down

logs:
	docker-compose logs -f

shell:
	docker-compose exec app /bin/bash

db-shell:
	docker-compose exec db mysql -u root -p

migrate:
	docker-compose exec app alembic upgrade head

migration:
	@read -p "Enter migration message: " msg; \
	docker-compose exec app alembic revision --autogenerate -m "$$msg"

test:
	docker-compose exec app pytest

clean:
	docker-compose down -v
	docker system prune -af

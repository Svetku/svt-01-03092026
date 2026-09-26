.PHONY: install run docker-build docker-run

export PYTHONPATH := src

install:
	uv sync

run:
	uv run python -m bot.main

docker-build:
	docker build -t svt-assistant .

docker-run:
	docker run --rm --env-file .env svt-assistant

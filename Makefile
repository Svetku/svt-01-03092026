.PHONY: install run

export PYTHONPATH := src

install:
	uv sync

run:
	uv run python -m bot.main

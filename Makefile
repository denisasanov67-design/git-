# Переменные окружения
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
MYPY = $(VENV)/bin/mypy
RUFF = $(VENV)/bin/ruff
DEPTRY = $(VENV)/bin/deptry

# Целевая директория с кодом
SRC_DIR = src

# Файлы-маркеры для отслеживания состояния
VENV_MARKER = $(VENV)/bin/activate
REQUIREMENTS = requirements.txt

.PHONY: all help venv run format lint typecheck check-requirements check clean

all: check

help:
	@echo "Доступные команды:"
	@echo "  make venv               - Создать виртуальное окружение и установить зависимости"
	@echo "  make run                - Запустить приложение (app.py)"
	@echo "  make format             - Автоматически отформатировать код"
	@echo "  make lint               - Проверить код на соответствие стилю (без исправлений)"
	@echo "  make typecheck          - Проверка статических типов (mypy)"
	@echo "  make check-requirements - Проверка соответствия импортов и requirements.txt"
	@echo "  make check              - Запустить все проверки (lint + typecheck + check-requirements)"
	@echo "  make clean              - Удалить виртуальное окружение и кэш"

# 1. Управление окружением (Stateless)
venv: $(VENV_MARKER)

$(VENV_MARKER): $(REQUIREMENTS)
	@echo "==> Создание виртуального окружения и установка зависимостей..."
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r $(REQUIREMENTS)
	@touch $(VENV_MARKER)

# 2. Запуск приложения
run: venv
	@echo "==> Запуск приложения..."
	$(PYTHON) $(SRC_DIR)/app.py

# 3. Проверка стилей (Форматирование)
format: venv
	@echo "==> Форматирование кода..."
	$(RUFF) format $(SRC_DIR)
	$(RUFF) check --fix $(SRC_DIR)

# 4. Проверка стилей (Только отчет)
lint: venv
	@echo "==> Линтинг кода..."
	$(RUFF) check $(SRC_DIR)

# 5. Проверка типов
typecheck: venv
	@echo "==> Статическая проверка типов..."
	$(MYPY) $(SRC_DIR)

# 6. Проверка зависимостей (импорты vs requirements.txt)
check-requirements: venv
	@echo "==> Проверка декларированных зависимостей..."
	$(DEPTRY) $(SRC_DIR)

# 7. Цепочка проверок (Композиция действий)
# Если один из таргетов завершится с ошибкой (exit code != 0), выполнение остановится
check: lint typecheck check-requirements
	@echo "==> Все проверки успешно пройдены!"

# Очистка артефактов
clean:
	@echo "==> Очистка окружения и кэша..."
	rm -rf $(VENV)
	rm -rf .mypy_cache .ruff_cache .pytest_cache __pycache__
	find . -type d -name __pycache__ -exec rm -rf {} +
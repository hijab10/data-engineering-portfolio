.PHONY: install package test dbt-compile dbt-build ci

DBT_DIR=dbt/orders
DBT_PROFILES_DIR=dbt/profiles

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

package:
	python -m compileall .
	@if python -m pip show black >/dev/null 2>&1; then black --check .; else echo "black not installed, skipping"; fi
	@if python -m pip show ruff >/dev/null 2>&1; then ruff check .; else echo "ruff not installed, skipping"; fi

test:
	@if [ -d tests ]; then pytest; else echo "No tests directory found, skipping tests"; fi

load-env:
	@export $$(grep -v '^#' .env | xargs)

dbt-compile:
	@export $$(grep -v '^#' .env | xargs) && \
	dbt deps --project-dir $(DBT_DIR) --profiles-dir $(DBT_PROFILES_DIR) && \
	dbt debug --project-dir $(DBT_DIR) --profiles-dir $(DBT_PROFILES_DIR) && \
	dbt compile --project-dir $(DBT_DIR) --profiles-dir $(DBT_PROFILES_DIR)

dbt-build:
	dbt deps --project-dir $(DBT_DIR) --profiles-dir $(DBT_PROFILES_DIR)
	dbt debug --project-dir $(DBT_DIR) --profiles-dir $(DBT_PROFILES_DIR)
	dbt seed --project-dir $(DBT_DIR) --profiles-dir $(DBT_PROFILES_DIR)
	dbt build --project-dir $(DBT_DIR) --profiles-dir $(DBT_PROFILES_DIR)

ci: package test dbt-build
# Batch Pipeline (Airflow + Postgres)

This project ingests a transactional dataset into PostgreSQL using an Airflow DAG.

## Structure

- `schemas/l0/` → raw schema definitions (JSON)
- `scripts/` → ingestion logic
- `airflow/dags/` → orchestration layer
- `data/` → source dataset

## Run locally

```bash
docker compose up -d
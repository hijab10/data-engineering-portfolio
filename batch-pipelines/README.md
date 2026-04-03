# Data Engineering Portfolio

This repository contains hands-on data engineering projects built using open-source tools.

## 🧱 Current Project: Batch Data Pipeline

Built a local data platform simulating production workflows:

- Orchestration: Airflow
- Storage: PostgreSQL
- Ingestion: Python
- Containerization: Docker

## 📊 Pipeline Overview

CSV → Airflow DAG → PostgreSQL (raw layer)

## 🧠 Key Features

- Schema-driven ingestion using JSON configs
- Environment-based configuration (no hardcoded credentials)
- Modular pipeline design (parsers, schema, ingestion separated)
- Dockerized local environment

## 🚀 Next Steps

- Add dbt for transformation layer
- Build analytics models (facts & dimensions)
- Add data quality checks
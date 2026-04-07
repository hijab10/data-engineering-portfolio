# Batch Pipelines

This folder contains a local batch data platform built with Airflow, PostgreSQL, Python, and dbt. It mirrors a production-style setup with layered data modeling, environment-based configuration, and CI validation.

## Project overview

The pipeline ingests a retail orders dataset into PostgreSQL through Airflow, then transforms it into layered analytical models using dbt.

In CI, raw data ingestion is simulated using dbt seeds to ensure reproducibility without relying on Airflow.

## Architecture

- **Ingestion / orchestration:** Airflow  
- **Storage:** PostgreSQL  
- **Transformation:** dbt  
- **Containerization:** Docker  
- **CI/CD:** GitHub Actions  

## Components

- `airflow/`  
  DAG definitions for orchestration

- `scripts/`  
  Python ingestion logic and parsers

- `schemas/`  
  JSON schema definitions for raw ingestion

- `data/`  
  Input dataset files

- `dbt/`  
  Transformation layer (sources, staging, and business models)

- `Makefile`  
  Standardized commands for local development and CI

- `requirements.txt`  
  Python dependencies

## Data model

- `raw.l0_orders`  
  Raw ingested data (Airflow in local, dbt seeds in CI)

- `staging.l1_orders`  
  Cleaned and standardized data (type casting, trimming, normalization)

- `business.l2_orders_daily`  
  Aggregated daily order metrics

## Pipeline flow

```text
CSV → Airflow DAG → raw.l0_orders → dbt source() → staging.l1_orders → dbt ref() → business.l2_orders_daily
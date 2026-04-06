
# Batch Pipelines

This folder contains a local batch data platform project built with Airflow, PostgreSQL, Python, and dbt.

## Project overview

The pipeline ingests a retail orders dataset into PostgreSQL through Airflow, then transforms it into layered analytical models using dbt.

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
  Transformation layer and business models

## Current warehouse layers

- `raw.l0_orders`
- `staging.l1_orders`
- `business.l2_orders_daily`

## Current functionality

- Load raw orders data from CSV into PostgreSQL via Airflow
- Standardize and enrich raw data in dbt staging models
- Build a business-facing daily orders summary model

## Tech stack

- Airflow 3
- PostgreSQL
- Python
- dbt
- Docker

## Next step

Set up CI/CD for testing and deployment workflows.
# Data Engineering Portfolio

This repository contains hands-on data engineering projects built with open-source tools and production-style design patterns.

## Current project: Batch pipeline for retail orders

This project implements a layered batch data pipeline using Airflow, PostgreSQL, Python, and dbt.

### Architecture

- **Ingestion / orchestration:** Airflow
- **Storage:** PostgreSQL
- **Transformation:** dbt
- **Containerization:** Docker

### Layered data model

- **raw.l0_orders**  
  Raw ingested source data loaded from CSV through an Airflow DAG

- **staging.l1_orders**  
  Cleaned and standardized staging model built in dbt

- **business.l2_orders_daily**  
  Business-facing daily sales summary model built in dbt

### Current pipeline flow

```text
CSV → Airflow DAG → raw.l0_orders → dbt source() → staging.l1_orders → dbt ref() → business.l2_orders_daily
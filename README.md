# Data Engineering Portfolio

Production-style data pipeline with dbt, Postgres, and CI validation.

This repository contains hands-on data engineering projects built with open-source tools and production-style design patterns.

## Current project: Batch pipeline for retail orders

This project implements a layered batch data pipeline using Airflow, PostgreSQL, Python, and dbt. It follows a medallion-style architecture (raw → staging → business) and includes CI validation using GitHub Actions.

### Architecture

- **Ingestion / orchestration:** Airflow  
- **Storage:** PostgreSQL  
- **Transformation:** dbt  
- **Containerization:** Docker  
- **CI/CD:** GitHub Actions  

### Layered data model

- **raw.l0_orders**  
  Raw ingested source data loaded from CSV through an Airflow DAG (simulated in CI using dbt seeds)

- **staging.l1_orders**  
  Cleaned and standardized staging model (type casting, trimming, data normalization)

- **business.l2_orders_daily**  
  Business-facing daily sales summary model

### Current pipeline flow

```text
CSV → Airflow DAG → raw.l0_orders → dbt source() → staging.l1_orders → dbt ref() → business.l2_orders_daily
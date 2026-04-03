import csv
import json
import os
from typing import Any

import psycopg2
from psycopg2.extensions import connection as PgConnection

from parsers import PARSERS


SCHEMA_PATH = "/opt/airflow/schemas/l0/orders.json"


def load_schema(schema_path: str) -> dict[str, Any]:
    with open(schema_path, "r", encoding="utf-8") as schema_file:
        return json.load(schema_file)


def get_db_connection() -> PgConnection:
    return psycopg2.connect(
        host=os.environ["POSTGRES_HOST"],
        port=int(os.environ.get("POSTGRES_PORT", "5432")),
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
    )


def build_create_table_sql(table_name: str, columns: list[dict[str, Any]]) -> str:
    column_definitions = [
        f"{column['target_name']} {column['sql_type']}"
        for column in columns
    ]
    columns_sql = ",\n    ".join(column_definitions)

    return f"""
DROP TABLE IF EXISTS {table_name};
CREATE TABLE {table_name} (
    {columns_sql}
);
"""


def create_table(conn: PgConnection, table_name: str, columns: list[dict[str, Any]]) -> None:
    create_table_sql = build_create_table_sql(table_name, columns)

    with conn.cursor() as cur:
        cur.execute(create_table_sql)

    conn.commit()


def transform_row(row: dict[str, str], columns: list[dict[str, Any]]) -> tuple[Any, ...]:
    transformed_values: list[Any] = []

    for column in columns:
        parser_type = column["parser_type"]
        parser = PARSERS[parser_type]
        raw_value = row.get(column["csv_column"])
        transformed_values.append(parser(raw_value, column))

    return tuple(transformed_values)


def insert_rows_from_csv(
    conn: PgConnection,
    csv_path: str,
    table_name: str,
    columns: list[dict[str, Any]],
) -> int:
    target_columns = [column["target_name"] for column in columns]
    columns_sql = ", ".join(target_columns)
    placeholders = ", ".join(["%s"] * len(target_columns))

    insert_sql = f"""
INSERT INTO {table_name} ({columns_sql})
VALUES ({placeholders})
"""

    inserted_rows = 0

    with open(csv_path, "r", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)

        with conn.cursor() as cur:
            for row in reader:
                values = transform_row(row, columns)
                cur.execute(insert_sql, values)
                inserted_rows += 1

    conn.commit()
    return inserted_rows


def main() -> None:
    schema = load_schema(SCHEMA_PATH)

    table_name = schema["table_name"]
    csv_path = schema["csv_path"]
    columns = schema["columns"]

    conn = get_db_connection()

    try:
        create_table(conn, table_name, columns)
        inserted_rows = insert_rows_from_csv(
            conn=conn,
            csv_path=csv_path,
            table_name=table_name,
            columns=columns,
        )
        print(f"{table_name} loaded successfully: {inserted_rows} rows inserted")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
from datetime import datetime
from typing import Any


def parse_text(value: str | None, _: dict[str, Any] | None = None) -> str | None:
    if value is None:
        return None

    cleaned_value = value.strip()
    return cleaned_value if cleaned_value else None


def parse_int(value: str | None, _: dict[str, Any] | None = None) -> int | None:
    if value is None:
        return None

    cleaned_value = value.strip()
    if not cleaned_value:
        return None

    return int(cleaned_value)


def parse_float(value: str | None, _: dict[str, Any] | None = None) -> float | None:
    if value is None:
        return None

    cleaned_value = value.strip()
    if not cleaned_value:
        return None

    return float(cleaned_value)


def parse_timestamp(value: str | None, column_config: dict[str, Any] | None = None) -> datetime | None:
    if value is None:
        return None

    cleaned_value = value.strip()
    if not cleaned_value:
        return None

    if column_config is None or "format" not in column_config:
        raise ValueError("Timestamp column is missing required 'format' in schema config.")

    return datetime.strptime(cleaned_value, column_config["format"])


PARSERS = {
    "text": parse_text,
    "int": parse_int,
    "float": parse_float,
    "timestamp": parse_timestamp,
}
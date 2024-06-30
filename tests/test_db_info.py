
import os
import asyncio

def test_get_db_all_tables():
    from src.database_utils.db_info import get_db_all_tables

    tables = asyncio.run(get_db_all_tables(os.getenv("DB_URL","")))

    print(tables)


def test_get_table_all_columns():
    from src.database_utils.db_info import get_table_all_columns

    columns = asyncio.run(get_table_all_columns(os.getenv("DB_URL",""), "stock_info"))

    print(columns)


def test_get_db_schema():
    from src.database_utils.db_info import get_db_schema

    schema = asyncio.run(get_db_schema(os.getenv("DB_URL","")))

    print(schema)
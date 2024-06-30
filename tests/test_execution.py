import asyncio
import os


def test_execute_sql():
    from src.database_utils.execution import execute_sql

    res = asyncio.run(execute_sql(os.getenv("DB_URL", ""), "SELECT * FROM stock_info;"))

    print(res)
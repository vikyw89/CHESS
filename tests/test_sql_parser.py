import asyncio
import os


def test_get_sql_tables():
    from src.database_utils.sql_parser import get_sql_tables

    tables = asyncio.run(
        get_sql_tables(
            os.getenv("DB_URL", ""),
            """SELECT * FROM stock_info JOIN stock_analyst ON stock_info.stock_code = stock_analyst.stock_code;""",
        )
    )

    print(tables)

def test_get_sql_columns_dict():
    from src.database_utils.sql_parser import get_sql_columns_dict

    columns = asyncio.run(get_sql_columns_dict(
        os.getenv("DB_URL", ""),
        """SELECT * FROM stock_info JOIN stock_analyst ON stock_info.stock_code = stock_analyst.stock_code;""",
    ))

    print(columns)


def test_get_sql_condition_literals():
    from src.database_utils.sql_parser import get_sql_condition_literals

    literals = asyncio.run(get_sql_condition_literals(
        os.getenv("DB_URL", ""),
        """SELECT * FROM stock_info JOIN stock_analyst ON stock_info.stock_code = stock_analyst.stock_code WHERE stock_code = '7203';""",
    ))

    print(literals)
import asyncio
import logging
from typing import List, Dict

from src.database_utils.execution import execute_sql


async def get_db_all_tables(db_path: str) -> List[str]:
    """
    Retrieves all table names from the database.

    Args:
        db_path (str): The path to the database file.

    Returns:
        List[str]: A list of table names.
    """
    try:
        raw_table_names = await execute_sql(db_path, "SHOW TABLES;")
        table_names = []
        for table in raw_table_names:
            table_names.append(table[0])
        return table_names
    except Exception as e:
        logging.error(f"Error in get_db_all_tables: {e}")
        raise e


async def get_table_all_columns(db_path: str, table_name: str) -> List[str]:
    """
    Retrieves all column names for a given table.

    Args:
        db_path (str): The path to the database file.
        table_name (str): The name of the table.

    Returns:
        List[str]: A list of column names.
    """
    try:
        table_columns_raw = await execute_sql(
            db_path, f"SHOW COLUMNS FROM {table_name};"
        )
        table_columns = []
        for column in table_columns_raw:
            table_columns.append(column[0])
        return table_columns
    except Exception as e:
        logging.error(f"Error in get_table_all_columns: {e}\nTable: {table_name}")
        raise e


async def get_db_schema(db_path: str) -> Dict[str, List[str]]:
    """
    Retrieves the schema of the database.

    Args:
        db_path (str): The path to the database file.

    Returns:
        Dict[str, List[str]]: A dictionary mapping table names to lists of column names.
    """
    try:
        table_names = await get_db_all_tables(db_path)
        tasks = []

        for table_name in table_names:
            tasks.append(get_table_all_columns(db_path, table_name))

        table_columns = await asyncio.gather(*tasks)

        table_map = {}

        for table_name, columns in zip(table_names, table_columns):
            table_map[table_name] = columns
            
        return table_map
    except Exception as e:
        logging.error(f"Error in get_db_schema: {e}")
        raise e

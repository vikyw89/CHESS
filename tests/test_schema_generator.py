import os


def test_get_schema_with_connections():
    from src.database_utils.schema_generator import DatabaseSchemaGenerator

    generator = DatabaseSchemaGenerator(db_path=os.getenv("DB_URL", ""))
    schema = generator.get_schema_with_connections()
    print(schema)
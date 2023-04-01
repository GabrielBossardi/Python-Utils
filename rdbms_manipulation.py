from sqlalchemy import create_engine
from typing import Optional
from sqlalchemy.engine import Engine
from pandas import DataFrame
from pangres import pg_upsert


def create_engine_postgresql(username: str, password: str, host: str, port: str, database: str) -> create_engine:
    return create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

def postresql_upsert(
    df_result: DataFrame,
    schema: str,
    database_table: str,
    engine: Engine,
    chunksize: Optional[int] = 10000,
) -> None:
    """
    Upsert a pandas DataFrame into a PostgreSQL table using pg_upsert.

    Parameters:
    -----------
    df_result: pandas.DataFrame
        DataFrame to be upserted
    schema: str
        Name of the schema where the table is located
    database_table: str
        Name of the table to upsert into
    engine: sqlalchemy.engine.Engine
        SQLalchemy engine instance to connect to the database
    chunksize: int, optional
        Number of rows to be inserted per batch, default is 10000.

    Returns:
    --------
    None
    """
    if not engine.has_table(database_table, schema=schema):
        raise ValueError(f"Table {database_table} does not exist in schema {schema}")

    try:
        pg_upsert(
            engine=engine,
            df=df_result,
            schema=schema,
            table_name=database_table,
            if_exists="upsert_overwrite",
            create_schema=False,
            add_new_columns=False,
            adapt_dtype_of_empty_db_columns=True,
            clean_column_names=True,
            chunksize=chunksize,
        )
    except IndexError:
        pass

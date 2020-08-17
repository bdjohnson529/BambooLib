"""
SQL.py
====================================
SQL module
"""

import time
import pandas as pd
import numpy as np
import pyodbc
import sqlalchemy





def readTableFromQuery(server_name, db_name, query):
    """
    Read table from SQL query, using Pyodbc.

    :param server_name: Server name
    :type server_name: str
    :param db_name: Database name
    :type db_name: str
    :param query: SQL query
    :type query: str
    """

    # Create the connection
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server_name + 
                          ';DATABASE=' + db_name + ';Trusted_Connection=yes')

    # Read in query
    start = time.time()
    input_df = pd.io.sql.read_sql(query, conn)
    end = time.time()

    # Print descriptive statistics
    print("\nRead time :\t", int(end-start), "s")
    rows = input_df.shape[0]
    cols = input_df.shape[1]

    print(f"Rows : \t\t {rows:,d}")
    print(f"Columns : \t {cols:,d}")

    # Close connection
    conn.close()

    return input_df


def executeQueryFromFile(server_name, db_name, file_name):
    """
    Excutes a query from a file.

    :param server_name: Server name
    :type server_name: str
    :param db_name: Database name
    :type db_name: str
    :param file_name: SQL file
    :type query: str
    """

    # Create the connection
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server_name + ';DATABASE=' + db_name + ';Trusted_Connection=yes')

    # read query into string
    with open(file_name) as file:
        query = file.read()

    # Read in query
    start = time.time()
    df = pd.io.sql.read_sql(query, conn)
    end = time.time()

    # Close connection
    conn.close()

    # Print descriptive statistics
    print("\nRead time :\t", int(end-start), "s")
    rows = df.shape[0]
    cols = df.shape[1]

    print(f"Rows : \t\t {rows:,d}")
    print(f"Columns : \t {cols:,d}")

    return df


def writeDfToSQL(df, server, database, table, driver='SQL+Server', chunksize=200):
    """
    Wrapper for pd.to_sql()

    :param df: table
    :type df: pd.DataFrame
    :param server_name: Server name
    :type server_name: str
    :param db_name: Database name
    :type db_name: str
    :param table_name: Database name
    :type table_name: str
    """

    # initialize SQL engine
    if(True):
        connection_str = 'mssql+pyodbc://' + server_name + '/' + db_name + '?driver=' + driver
        engine = sqlalchemy.create_engine(connection_str)
    else:
        params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db)
        engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

    start = time.time()

    # table name needs to be lower case
    table_name = table_name.lower()

    df.to_sql(table_name, con=engine,
                      if_exists='replace', index=False,
                      method='multi', chunksize=chunksize)


    end = time.time()

    # diagnostic timing
    print("Write time :\t", int(end - start), " s")
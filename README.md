# Bamboo Library

This library contains wrappers for data analysis functions in Python. The functions in this library provide a way to standardize, and simplify code.

Builds are tested on a Windows 64 bit machine.


## Installation
From the base directory, run

```
python setup.py install
```

If you have already installed BambooLib, and are installing an update, you may need to delete the old distribution files before installing again. The source files are usually located here:

`C:\ProgramData\Anaconda3\Lib\site-packages`

To determine the location of the distribution file,

```
import BambooLib.SQL as sql
sql.__file__
```

## SQL Library
SQL functions use Windows authentication and SQL Server Native client.

`import BambooLib.SQL as sql`


Read a table into a Pandas dataframe :

```
df = sql.readTableFromQuery(SERVER_NAME, DB_NAME, query)
```

Execute SQL query from a file :

```
df = sql.executeQueryFromFile(SERVER_NAME, DB_NAME, fileName)
```

Write table to SQL:

```
sql.writeTableToSQL(df, server_name, db_name, table_name, driver, chunksize=200)
```

## Clustering Library

`import BambooLib.Clustering as cluster`

K-means clustering on one column :

```
df['Cluster Number'] = cluster.kmeansOnColumn(df, column, n_clusters)
```

## Hashing Library

`import BambooLib.Clustering as cluster`

Hash a string :

```
generate_uniqueid(input_str)
```

## Address Library

`import BambooLib.Address as address`

Parse full address into components:

```
df[['Street', 'City', 'State', 'Zip5', 'Zip9']] = \
    df['FullAddress'].apply(address.parseStreetAddress)
```

import BambooLib.SQL as sql
import pandas as pd
from datetime import datetime

SERVER_NAME = 'KSIREAD'
DB_NAME = 'PDIAnalytics'

query = "SELECT CHECKSUM_AGG(CHECKSUM(*)) FROM PDIAnalytics.dbo.T_Analytics_AppDetails"


start = datetime.now()

df = sql.readTableFromQuery(SERVER_NAME, DB_NAME, query)

stop = datetime.now()




print(df)
print(stop - start, ' seconds')
import os
import sys
import subprocess
from datetime import datetime


start = datetime.now()
#os.system(command)
stop = datetime.now()


process = subprocess.check_output('sqlcmd -S KSIREAD -h -1 -Q \"SELECT CHECKSUM_AGG(CHECKSUM(*)) FROM PDIAnalytics.dbo.T_Analytics_AppDetails\"', shell=True)

print(process.split())
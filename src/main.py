import os
import pandas as pd
import subprocess
import time
from datetime import datetime
import re

#Check Java version and availability
def java_check():
    try:
        jre = os.popen("java -version 2>&1").read()
        return jre
    except:
        return None

#Install JRE if unavailable
def java_install():
    try:
        current_folder = str(os.path.abspath(os.getcwd()).replace('\\', '/'))
        installer_path = current_folder + r'*.exe'
        subprocess.Popen([installer_path, 'INSTALL_SILENT=1', 'STATIC=0', 'AUTO_UPDATE=0'])
        print("Installation started in the background")
        time.sleep(20)
        return 'available'
    except:
        print("Error")
        return 'unavailable'

#Save the CSV file
now = datetime.today().isoformat()
now = now.replace(':', '-')
now = now

#Create a DataFrame
availability_data = [now]
df = pd.DataFrame(availability_data, columns=['date-time'])

#Regular expression to select the Java version
text = java_check()
pattern = r'java version "(.*?)"'
match = re.search(pattern, text)

if match:
    java_version = match.group(1)
else:
    java_version = java_install()

if java_version == 'unavailable':
    java_available = 'unavailable'
else:
    java_available = 'available'

df['java-version'] = java_version
df['available'] = java_available

#Export the processed CSV
df.to_csv('java-availability.csv', sep=';', decimal=',', encoding='utf-8', index=False, mode='a', header=False)

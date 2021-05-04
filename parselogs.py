import re
import pandas as pd
import logging
from helper import *
import logging
logging.basicConfig(level=logging.INFO)

logging.info('Reading access logs ...')
with open('accesslog', 'r') as f:
    data = f.readlines()
logging.info('Done.')

pattern = re.compile(r'([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+ \d+) "(.*?)" "(.*?)"')
logs = []

logging.info('Parsing access logs ...')
for line in data:
    match = pattern.match(line).groups()
    logs.append(match)
    # print(match, end = '\n\n')
logging.info('Done.')

ip_addresses = [log[0] for log in logs]
browsers = []
operatingsystems = []
devices = []

logging.info('Collecting data ...')
for log in logs:
    result = parse_useragent(log[5])
    # print(result)
    browsers.append(result["software_name"])
    operatingsystems.append(result["operating_system_name"])
    if result["operating_system_name"] == 'macOS':
        devices.append('Macintosh')
    elif result["operating_system_name"] == 'Windows':
        devices.append('Windows Device')
    else:
        devices.append(result["simple_operating_platform_string"])
logging.info('Done.')

# print(ip_addresses)
# print(browsers)
# print(operatingsystems)
# print(devices)

dic = {'ip_addresses' : ip_addresses,
        'browsers' : browsers,
        'operatingsystems' : operatingsystems,
        'devices' : devices}

logging.info('Saving data to csv file ...')
df = pd.DataFrame(dic)
df.to_csv('log_data.csv')
logging.info('Done.')
# -----------------------------------------------------------------------

# print(get_IP_details(ip_addresses[0]))
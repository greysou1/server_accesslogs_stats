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


browsers = []
operatingsystems = []
devices = []
cities = []
ip_addresses = []

logging.info('Collecting data ...')
for log in logs:
    result = parse_useragent(log[5])
    # print(result)
    if result["operating_system_name"] == 'macOS':
        device = 'Macintosh'
        devices.append(device)
        ip_addresses.append(log[0])
        cities.append(get_IP_details(log[0])['city'])
        browsers.append(result["software_name"])
        operatingsystems.append(result["operating_system_name"])
    elif result["operating_system_name"] == 'Windows':
        device = 'Windows Device'
        devices.append(device)
        ip_addresses.append(log[0])
        cities.append(get_IP_details(log[0])['city'])
        browsers.append(result["software_name"])
        operatingsystems.append(result["operating_system_name"])
    elif result["simple_operating_platform_string"]:
        device = result["simple_operating_platform_string"]
        devices.append(device)
        ip_addresses.append(log[0])
        cities.append(get_IP_details(log[0])['city'])
        browsers.append(result["software_name"])
        operatingsystems.append(result["operating_system_name"])

logging.info('Done.')
print(devices)
print(cities)

# print(ip_addresses)
# print(browsers)
# print(operatingsystems)
# print(devices)

dic = {'cities' : cities,
        'browsers' : browsers,
        'operatingsystems' : operatingsystems,
        'devices' : devices,
        'ip_addresses': ip_addresses}

logging.info('Saving data to csv file ...')
df = pd.DataFrame(dic)


df.to_csv('log_data.csv')
logging.info('Done.')
# -----------------------------------------------------------------------

# print(get_IP_details(ip_addresses[0]))
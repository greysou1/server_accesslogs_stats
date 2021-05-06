from numpy import nan
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('log_data.csv')
# ip_addresses = [value for value in list(df['ip_addresses']) if str(value) != 'nan']
browsers = [value for value in list(df['browsers']) if str(value) != 'nan']
operatingsystems = [value for value in list(df['operatingsystems']) if str(value) != 'nan']
devices = [value for value in list(df['devices']) if str(value) != 'nan']
cities = [value for value in list(df['cities']) if str(value) != 'nan']

def plot_pie(input_list, explode_list=[]):
    labels =  list(set(input_list))
    data = []
    total = len(input_list)
    explode = []
    for label in labels:
        data.append((input_list.count(label)/total) * 100)
        if label in explode_list:
            explode.append(0.1)
        else:
            explode.append(0)

    return data, labels, explode

# plot browsers
browser_data, browser_labels, browser_explode = plot_pie(browsers, ['Safari, Chrome'])
plt.pie(browser_data, labels = browser_labels, explode = browser_explode, autopct='%1.1f%%',shadow=False)
plt.savefig('plots/browser_pie.png')
plt.close()

# plot operatingsystems
os_data, os_labels, os_explode = plot_pie(operatingsystems, ['macOS', 'Windows'])
plt.pie(os_data, labels = os_labels, explode = os_explode, autopct='%1.1f%%',shadow=False)
plt.savefig('plots/os_pie.png')
plt.close()

# plot devices
device_data, device_labels, device_explode = plot_pie(devices)
plt.pie(device_data, labels = device_labels, explode = device_explode, autopct='%1.1f%%',shadow=False)
plt.savefig('plots/device_pie.png')
plt.close()

# plot cities
cities_data, cities_labels, cities_explode = plot_pie(cities)
plt.pie(cities_data, labels = cities_labels, explode = cities_explode, autopct='%1.1f%%',shadow=False)
plt.savefig('plots/cities_pie.png')
plt.close()
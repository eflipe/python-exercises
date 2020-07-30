import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # saco el encabezado
    # print(header_row)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        highs.append(high)
        dates.append(current_date)

print(highs)
print(dates)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

plt.title("Temperaturas máx diarias", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

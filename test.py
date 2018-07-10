import json
from pprint import pprint

import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_data.csv")

newpath = r'results'
if not os.path.exists(newpath):
    os.makedirs(newpath)


print("Minimum Temperature Summary:")
print(df['minTemp'].describe())



fig = plt.figure()
ax = plt.subplot(111)
ax.plot(df['time'], df['minTemp'])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Minimum Temperature per day for June")


fig.savefig('results/minTemperature.png')




print("Maximum Temperature Summary:")
print(df['maxTemp'].describe())



fig = plt.figure()
ax = plt.subplot(111)
ax.plot(df['time'], df['maxTemp'])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Maximum Temperature per day for June")


fig.savefig('results/maxTemperature.png')

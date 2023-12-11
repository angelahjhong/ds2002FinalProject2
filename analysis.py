import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt

# The lists for analyzing
factors = []
time = []
piValue = []
time2 = []
piValue2 = []
factors2 = []

# Connecting to the sql and grabbing data
connection = sqlite3.connect('api_data.db')
db = connection.cursor()
db.execute('SELECT * FROM api_data')
data = db.fetchall()

# Plot relationship between timestamps and factors
# Append data items
for entry in data:
    factors.append(entry[1])
    time.append(datetime.strptime(entry[3], "%Y-%m-%d %H:%M:%S"))

# Plot factor vs timestamp
plt.plot(time, factors, marker='o', linestyle='-', color='b')
plt.title('Factor vs. Time')
plt.xlabel('Time in Min')
plt.ylabel('Factor')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Mapping the relationship between pi and timestamp
for entry in data:
    piValue.append(entry[2])
    time2.append(datetime.strptime(entry[3], "%Y-%m-%d %H:%M:%S"))

# Plotting pi vs. time
plt.plot(time2, piValue, marker='o', linestyle='-', color='r')
plt.title('Pi vs. Time')
plt.xlabel('Time in Min')
plt.ylabel('Pi')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Mapping the relationship between pi vs factor
for entry in data:
    piValue2.append(entry[2])
    factors2.append(entry[1])

# Plotting the pi vs factor
plt.plot(factors2, piValue2, marker='o', linestyle='-', color='c')
plt.title('Pi vs. Factor')
plt.xlabel('Factor')
plt.ylabel('Pi Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

connection.close()
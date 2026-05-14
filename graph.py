import mysql.connector
import matplotlib.pyplot as plt

# connect to MYSQL
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Jyotisah@123",
    database = "solar_db"
)

cursor = db.cursor()

#fetch data
cursor.execute("SELECT cycle,sunlight,moisture,power FROM records")
data = cursor.fetchall()

#separate data 
cycles = []
sunlight = []
moisture = []
power = []

for row in data:
    cycles.append(row[0])
    sunlight.append(row[1])
    moisture.append(row[2])
    power.append(row[3])
    
db.close()

plt.plot(cycles, moisture)
plt.xlabel("Cycle")
plt.ylabel("Moisture")
plt.title("Soil Moisture Over Time")

plt.show()


plt.plot(sunlight, power)
plt.xlabel("Sunlight")
plt.ylabel("Power")
plt.title("Power vs Sunlight")

plt.show()
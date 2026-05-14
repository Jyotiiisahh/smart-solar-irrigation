from solar import SolarPanel
from sensor import SoilSensor
from pump import Pump
from controller import Controller

import random
import time
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jyotisah@123",
    database="solar_db"
)

cursor = db.cursor()



#creating objects
solar = SolarPanel(0.2)
sensor = SoilSensor()
pump = Pump()
controller = Controller()


#store records
records = []



#simulation
for i in range(5): #simulate 5 cycles
       sunlight = random.randint(20,100)
       power = solar.generate_power(sunlight)

       moisture = sensor.read_moisture()

       decision = controller.decide(moisture,power)

       if decision == "ON":
           pump.turn_on()
       else:
         pump.turn_off()
      

       print("\nCycle:", i+1)
       print("Sunlight:", sunlight)
       print("Moisture:", moisture)
       print("Power:", power)
       print("Pump Status:", pump.status)

       #store data
       records.append({
           "cycle":i+1,
           "Sunlight":sunlight,
           "moisture":moisture,
           "power":power,
           "pump":pump.status
        })
       cursor.execute("""
        INSERT INTO records( cycle,sunlight,moisture,power,pump) 
        VALUES(%s,%s,%s,%s,%s)             
        """,(i+1, sunlight , moisture, power,pump.status))
        
       db.commit()
      
       time.sleep(1)
       
db.close()
       
#print all stored records
print("\nAll Records:")
for r in records:
     print(r)
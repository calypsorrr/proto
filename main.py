import mysql.connector
from mysql.connector import errorcode
from sht20 import SHT20
from time import sleep
import time
import gpiozero

RELAY_PIN = 19

relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)

config = {
  'host':'protonxt.mysql.database.azure.com',
  'user':'boclaes',
  'password':'KdGaBhg4?',
  'database':'proto',
  'client_flags': [mysql.connector.ClientFlag.SSL],
  'ssl_ca': 'Cert/DigiCertGlobalRootCA.crt.pem'
}

def temp_hum():
  # making def global
  global temp_2
  global humid_2

  # getting the data out of the SHT20
  sht = SHT20(1, resolution=SHT20.TEMP_RES_14bit)
  temp = sht.read_temp()
  humid = sht.read_humid()

  # rounding out my floats
  temp_1 = round(temp)
  humid_1 = round(humid)

  # putting everyting into tubles
  temp_2 = [temp_1]
  humid_2 = [humid_1]

  # printing reslults
  print(temp_1)
  print(humid_1)

def azure():
  try:
     conn = mysql.connector.connect(**config)
     print("Connection established")
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    cursor = conn.cursor()

  # Insert some data into table
    cursor.execute("INSERT INTO temp (temp) VALUES (%s);", (temp_2))
    cursor.execute("INSERT INTO hum (hum) VALUES (%s);", (humid_2))    
    print("Temp and Hum are now into the database")

  # Cleanup
    conn.commit()
    cursor.close()
    conn.close()
    print("Done.")

def main():
  temp_hum()
  azure()
  time.sleep(3000)

if __name__ == '__main__':  # code to execute if called from command-line
    main()
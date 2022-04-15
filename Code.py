#open a serial port in python and send a message down it

import serial
import mysql.connector
import asyncio
import time
from datetime import datetime
import serial.tools.list_ports
import math


# port_name = "/dev/ttyUSB4"
# port = serial.Serial(port_name, baudrate=9600, timeout=5)
# 
# 
# print (port)
# port.write(b'Hi, this is a test message from the Comms Section 1 radio: Radio: "Zach"')     # write a string
#

#def get_new_rfid():
    
    # access database and get all new RFID entries
    
    # pull entries into lists of tuples (uid, time, RFID tag)
    
    # return list of tuples
    #return

#def mark_RFID_as_sent(entries):
    
    # for each of these entries (uid) mark the SENT field as sent
    
    #return

# Trying out an async function to constantly send messages to test for signal connection -------------------------

def testing():
        message = ("...")
        port.write(message)
        print(message)
        
#time.time
             
# Asyncrounous listening loop----------------------

def listening():
        message = port.readline(10)
        print(message)
        print (".")
        

    

# Sending a Data File------------------------------

# Data = open (r"TextFile1.txt", "r")
# print (Data.read())
# port.write(open(r"TextFile1.txt","rb").read())
# Data.close()

# Accessing the Database---------------------------





def accessing_database():
    Section1DAQ = mysql.connector.connect(
      host="localhost",
      user="JMUWAM",
      password="rockcity",
      database="Section1DAQ",
      
    )

    print(Section1DAQ)

    mycursor = Section1DAQ.cursor()

    mycursor.execute("SHOW DATABASES")
    databases = mycursor.fetchall()

    for database in databases:
        print(database)
        
    mycursor.execute("SHOW TABLES")

    tables = mycursor.fetchall()

    for table in tables:
        print(table)
    #----------------------------------------------
    
    return Section1DAQ

def get_gps_data(Section1DAQ):
    
    mycursor = Section1DAQ.cursor()
    mycursor.execute("SELECT * FROM GPS")
    rows = mycursor.fetchall()

    for row in rows:
        print (rows)
        uid = row[0]
        lat = row[1]
        lon = row[2]
        time = row[3]
        if_sent = row[4]
        
    print (rows)
    #--------------------------------------------------------
    
def get_RFID_data(Section1DAQ):
    mycursor = Section1DAQ.cursor()
    mycursor.execute("SELECT * FROM RFID")
    rows1 = mycursor.fetchall()

    for row in rows1:
        print (rows1)
        uid = row[0]
        lat = row[1]
        lon = row[2]
        time = row[3]
        if_sent = row[4]
        
    print (rows1)
    #-------------------------------------------------------
def get_temp_data(Section1DAQ):
    mycursor = Section1DAQ.cursor()
    mycursor.execute("SELECT * FROM Temp")
    rows2 = mycursor.fetchall()
    unsent_entries = ("SELECT * FROM Temp WHERE Sent = '0'")
    mycursor.execute (unsent_entries)
    number_to_be_sent = mycursor.fetchall()
    
    for x in number_to_be_sent:
        print (x)

    for row in rows2:
        print (rows2)
        uid = row[0]
        lat = row[1]
        lon = row[2]
        time = row[3]
        #if_sent = row[4]
    print(rows2)

    #-------------------------------------------------------    
def send_data_to_other_radios():
    port.write(r, 'The GPS Data is:' 'results')
    port.write(r, 'The RFID Data is:' 'results1')
    port.write(r,'The Temp Data is:' 'results2')
        
        #to do - Create a way to log the number of entries in the databases in order to not send duplicate data
        #to do - Signal hop information
        #to do - Respond to incoming commands
        #to do - Boot program on startup
     #port.close
     
#def mark_sent_gps_data():



#def mark_sent_RFID_data():



def mark_sent_temp_data(Section1DAQ):
    mycursor = Section1DAQ.cursor()
    unsent_entries = ("SELECT * FROM Temp WHERE Sent = '0'")
    mycursor.execute (unsent_entries)
    number_to_be_sent = mycursor.fetchall()
    entries_to_be_marked = "INSERT INTO Temp (Sent) VALUES (0)"
    marked_sent = ("1")
    mycursor.execute(entries_to_be_marked, marked_sent)
  
    
    
    
    
    
    
    
    
    
#-------------------------------------------------------------------------------------------------------------------------
#on_board_time = command to get time from GPS and decode



internal_time = datetime.now()

time_of_last_report_temp = math.trunc(datetime.timestamp(internal_time))
time_of_last_report_GPS = math.trunc(datetime.timestamp(internal_time))
time_of_last_report_RFID = math.trunc(datetime.timestamp(internal_time))
print('The starting time is: ' , time_of_last_report_temp)
database_handle = accessing_database()

while True:
    time_Current_temp = datetime.now()
    Current_Time_temp = math.trunc(datetime.timestamp(time_Current_temp))
    if Current_Time_temp - time_of_last_report_temp >= 20:
        print('20 seconds have passed')
        print('The current time is: ' , Current_Time_temp)
        time_of_last_report_temp = Current_Time_temp
        get_temp_data(database_handle)
#        mark_sent_temp_data(database_handle)
        
#     testing()
# 
#     listening()
#test

    time_Current_GPS = datetime.now()
    Current_Time_GPS = math.trunc(datetime.timestamp(time_Current_GPS))
    if Current_Time_GPS - time_of_last_report_GPS >= 10:
        print('10 seconds have passed')
        print('The current time is: ' , Current_Time_GPS)
        time_of_last_report_GPS = Current_Time_GPS
        get_gps_data(database_handle)
#       mark_sent_gps_data()

    time_Current_RFID = datetime.now()
    Current_Time_RFID = math.trunc(datetime.timestamp(time_Current_RFID))
    if Current_Time_RFID - time_of_last_report_RFID >= 30:
        print('5 seconds have passed')
        print('The current time is: ' , Current_Time_RFID)
        time_of_last_report_RFID = Current_Time_RFID
        get_RFID_data(database_handle)
#       mark_RFID_sent_data()

#         
#     send_data_to_other_radios()
#     Send to a particular radio (Homebase)


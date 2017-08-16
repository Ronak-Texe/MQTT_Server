#import pymysql
#pymysql.install_as_MySQLdb()
#import MySQLdb
#db = MySQLdb.connect(host="127.0.0.1", user="root",passwd="rapidfire",db="sensor_trial")
#cursor = db.cursor()
#
##sql = """CREATE TABLE Sensor1(DeviceNumber INT(3), DeviceType CHAR(20), TimeofRequest CHAR(10), Temperature INT(4),DeviceAlert CHAR(20), DeviceStatus CHAR(30), DevicePath CHAR(20), RouteSignalStrength CHAR(20), LastPolledminsago FLOAT)"""
#
#sql = "CREATE TABLE Sensors(DeviceNumber INT(3), DeviceType CHAR(20),Temperature INT(4))"
#
#r=("""INSERT INTO Sensors VALUES (%s,%s)""",(12,18))
#s=("""INSERT INTO Sensors VALUES (%s,%s)""",(2,24))
#
#cursor.execute(sql)
#cursor.execute(r)
#cursor.execute(s)

#import MySQLdb
#
#db = MySQLdb.connect("localhost","root","rapidfire","sensor_trial" )
#cursor = db.cursor()
#
#sql = """CREATE TABLE Sensor1(DeviceNumber INT, DeviceType CHAR, TimeofRequest CHAR, Temperature INT, DeviceAlert CHAR, DeviceStatus CHAR, DevicePath CHAR, RouteSignalStrength CHAR, LastPolledminsago INT)"""
#cursor.execute(sql)
#
#try:
#    #cursor.execute("""INSERT INTO Sensors00 VALUES (%s,%s,%s)""",(12,18))
#    #cursor.execute("""INSERT INTO Sensors VALUES (%s,%s)""",(2,24))
#    cursor.execute("""INSERT INTO Sensors12 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(12,'HELLO WORLD','12:10',24,'[gjhg]','normal','1-0-0','-70dbm',12))
#    db.commit()
#    
#except:     
#    db.rollback()
#
#cursor.execute("""SELECT * FROM Sensors12;""")
#
#db.close()
#




##    WORKS

#import MySQLdb
#
#db = MySQLdb.connect("localhost","root","rapidfire","sensor_trial" )
#cursor = db.cursor()
#
#sql = """CREATE TABLE Sensors12 (DeviceNumber INT,Temperature INT, ID CHAR(25))"""
#cursor.execute(sql)
#
#try:
#    #cursor.execute("""INSERT INTO Sensors00 VALUES (%s,%s,%s)""",(12,18))
#    #cursor.execute("""INSERT INTO Sensors VALUES (%s,%s)""",(2,24))
#    cursor.execute("""INSERT INTO Sensors12 VALUES (%s,%s,%s)""",(12,18,'HELLO WORLD'))
#    db.commit()
#    
#except:     
#    db.rollback()
#
#cursor.execute("""SELECT * FROM Sensors12;""")
#
#db.close()

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

db = MySQLdb.connect(host="52.56.146.236", user="root", passwd="rapidfire", db="sensor_trial")
cursor = db.cursor()

sql = """CREATE TABLE Sensor26 (DeviceNumber INT, DeviceType CHAR(25), TimeofRequest CHAR(25), Temperature INT, DeviceAlert CHAR(25), DeviceStatus CHAR(25), DevicePath CHAR(25), RouteSignalStrength CHAR(25), LastPolledminsago INT)"""
cursor.execute(sql)

try:
    #cursor.execute("""INSERT INTO Sensors00 VALUES (%s,%s,%s)""",(12,18))
    #cursor.execute("""INSERT INTO Sensors VALUES (%s,%s)""",(2,24))
    cursor.execute("""INSERT INTO Sensor26 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",('35','HELLO WORLD','12:10',34,'[gjhg]','normal','1-0-0','-70dbm',12))
    db.commit()
    
except:     
    db.rollback()

cursor.execute("""SELECT * FROM Sensor26;""")

db.close()
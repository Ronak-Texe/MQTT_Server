import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

db = MySQLdb.connect("localhost","root","rapidfire","sensor_trial" )
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
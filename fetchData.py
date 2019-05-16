#Program to fetch weather data from database

#import mysql module
import MySQLdb

#connection handler
db = MySQLdb.connect(host="localhost",
					 user="your_username",passwd="your_password",
					 db="your_db_name")
					 
#cursor to execute queries
cur = db.cursor()

#query
cur.execute("SELECT * FROM your_table_name LIMIT 10")

#list to save the data
data = []

#iterate through the fetched rows
for row in cur.fetchall():
	#create a dictionary
	dataDictionary = {'id': row[0], 'time': row[1], 'location': row[2], 'temperature': row[3], 'pressure': row[4], 'humidity': row[5]}	
	#append to list
	data.append(dataDictionary)
	
#display the mausam data
print(data)

db.close()
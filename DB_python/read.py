import mysql.connector

mysqlConnection = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="univali",
  database="univalidb",
)

cursor = mysqlConnection.cursor()

sql = "SELECT * FROM usuarios"

cursor.execute(sql)
results = cursor.fetchall()

cursor.close()
mysqlConnection.close()

for result in results:
  print(result)
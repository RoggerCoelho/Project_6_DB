import mysql.connector

mysqlConnection = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="univali",
  database="univalidb",
)

cursor = mysqlConnection.cursor()

sql = "DELETE FROM usuarios WHERE id = %s"
values = (1,)

cursor.execute(sql, values)
mysqlConnection.commit()

recordsaffected = cursor.rowcount

cursor.close()
mysqlConnection.close()

print(recordsaffected, " registro deletado")
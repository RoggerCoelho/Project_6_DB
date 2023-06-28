import mysql.connector;

mysqlConnection = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="univali",
  database="univalidb",
)

cursor = mysqlConnection.cursor()

sql = "INSERT INTO usuarios (name, email) VALUES (%s, %s)"
values = (
  'Leonardo',
  'leonardo@gmail.com.br',
)

cursor.execute(sql, values)
mysqlConnection.commit()

userid = cursor.lastrowid

cursor.close()
mysqlConnection.close()

print("Foi cadastrado o usuário de ID:", userid)
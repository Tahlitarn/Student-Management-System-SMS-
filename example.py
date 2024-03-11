import mysql.connector

db= mysql.connector.connect(
    
    host = "localhost",
    user = "root",
    passwd = "Happylink234$",
    database = "testdatabase"
)

my_cursor = db.cursor()

# my_cursor.execute("CREATE DATABASE testdatabase")
# my_cursor.execute("SHOW DATABASES")

# for d in my_cursor:
#     print(d[0])
# my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
# my_cursor.execute("SHOW TABLES")
# for table in my_cursor:
#     print(table[0])

sqlstaff = "INSERT INTO users (name, email,age) VALUES(%s,%s,%s)"
record1= ("JOHN","johnme.com",22)
my_cursor.execute(sqlstaff,record1)
db.commit()
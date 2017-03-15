import MySQLdb as sqlDb
import cursor as cursor
db = sqlDb.connect("localhost", "root", "password", "test")
cursor = db.cursor()
cursor.execute("insert into sara values(100) ")
#result = cursor.fetchall()
db.close()


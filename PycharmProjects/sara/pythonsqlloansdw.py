import MySQLdb as sqlDb
import cursor as cursor
#db = sqlDb.connect("localhost", "root", "password", "test")
db1=sqlDb.connect("localhost",'root','password','loany')
cursor = db1.cursor()
query = "select * from loans"
cursor.execute(query)
#result = cursor.fetchall()
db1.close()


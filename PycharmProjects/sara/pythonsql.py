import MySQLdb as sqlDb
import cursor as cursor
db = sqlDb.connect("localhost", "root", "password", "loany")
cursor = db.cursor()
query="select * from loans"
cursor.execute(query)
result = cursor.fetchall()
for r in result:
    print r
db.close()

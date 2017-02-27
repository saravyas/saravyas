import MySQLdb as Sql
import cursor as cursor
loan=open('loans.txt','w')
loancsv=open('loans.csv','w')
loantsv=open('loans.tsv','w')
db=Sql.connect("localhost","root","password","loany")
cursor=db.cursor()
query="select * from loans"
cursor.execute(query)
result=cursor.fetchall()
for r in result:
    loan.write(str(r))
    loancsv.write(str(r))
    loantsv.write(str(r))
loan.close()
db.close
import MySQLdb as Sql
import cursor as cursor
import os
import sys
import subprocess
loan=open('loans.txt','r+')
loancsv=open('loans.csv','r+')
loantsv=open('loans.tsv', "r+")
db=Sql.connect("localhost","root","password","loany")
cursor=db.cursor()
query="select * from loans"
cursor.execute(query)
result=cursor.fetchall()
def txt():
    for r in result:
        loan.write(str(r))
def csv():
    for r in result:
        loancsv.write(str(r))
def tsv():
    for r in result:
        loantsv.write(str(r))
def default():
    print "please try again"
option={1:txt,2:csv,3:tsv}
print "enter the number\n"
try:
    num =int(raw_input())
    print type(num)
    option[num]()
except KeyError:
    default()
loan.close()
loancsv.close()
loantsv.close()
db.close
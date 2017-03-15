import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'password', 'test');

with con:
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS name")
    #cur.execute("CREATE TABLE name(Id INT PRIMARY KEY AUTO_INCREMENT, \
    #            Name VARCHAR(25))")
    # cur.execute("INSERT INTO name(Name) VALUES('saravyas')")
    # cur.execute("INSERT INTO name(Name) VALUES('vignesh')")
    # cur.execute("INSERT INTO name(Name) VALUES('malar')")
    # cur.execute("INSERT INTO name(Name) VALUES('shyam')")
    # cur.execute("INSERT INTO name(Name) VALUES('gomal')")
    # cur.execute("INSERT INTO name(Name) VALUES('maha')")
    cur.execute("INSERT INTO name(Name) "
                "VALUES('mahas'),(udhyan),(trim)")

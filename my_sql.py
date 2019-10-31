import sqlite3 as db
con = db.connect('test.db')
cur = con.cursor()

#################################################
#create a string with sql create table code
#################################################
sql = '''CREATE TABLE users(
            id INT PRIMARY KEY,
            username VARCHAR(64),
            password VARCHAR(64))'''

################################################
#execute the sql code
################################################
#cur.execute(sql)

sql = '''INSERT INTO users
         VALUES (?,?,?)'''
###############################################
#execute the query with one row
###############################################
cur.execute(sql,[44,'Billy','1234'])

###############################################
#execute many rows as a list of tuples
###############################################

#cur.executemany(sql,[(55,'AA','1'),(56,'BB','2')])

##############################################
#sqlite does not auot commit
##############################################

con.commit()
sql = "SELECT * FROM users"
cur.execute(sql)
print(cur.fetchall())

cur.execute(sql)
for row in cur:
    print(row)


import sqlite3


#print(dir(sqlite3))

# Data base Create
db=sqlite3.connect("studentsDB.db")

# Object create
cursor=db.cursor()

#Table create
cursor.execute('''CREATE TABLE IF NOT EXISTS studentsDB (ID INTEGER, NAME TEXT NOT NULL , GRADE TEXT)''')
db.commit()
print('Databse create')


'''
# INSERT VALUE
cursor.execute('INSERT INTO studentsDB(ID,NAME,GRADE) VALUES(?,?,?)',(111,'rifat','a+'))
cursor.execute('INSERT INTO studentsDB(ID,NAME,GRADE) VALUES(?,?,?)',(101,'david','a+'))
cursor.execute('INSERT INTO studentsDB(ID,NAME,GRADE) VALUES(?,?,?)',(131,'alex','b'))


db.commit()
'''

# read data
cursor.execute("SELECT * FROM studentsDB")
rows= cursor.fetchall()
print(rows)























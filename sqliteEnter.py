import sqlite3
db=sqlite3.connect('sample.db')
cr=db.cursor()
x= str("dorosara")
y= int(2345678)
cr.execute("insert into login(user, password)VALUES('%s','%d')"%(x,y))
db.commit()
db.close()

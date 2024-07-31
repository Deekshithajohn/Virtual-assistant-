import sqlite3
db=sqlite3.connect('sample.db')
cr=db.cursor()
x= str(input("Enter User Name:"))
y= str(input("Enter Password:"))
cr.execute("insert into login(user,password)VALUES('"+x+"', '"+y+"')")
db.commit()
db.close()
print("Successfully Record Inserted…")

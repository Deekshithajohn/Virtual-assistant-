import sqlite3
db=sqlite3.connect('sample.db')
cr=db.cursor()
cr.execute("insert into login(user, password) VALUES ('sreeranjan', '12345678')")
db.commit()
db.close()
print("Successfully Record Inserted…")

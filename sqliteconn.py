import sqlite3
db = sqlite3.connect('sample.db')
cr = db.cursor()
cr.execute("create table login(user text, password text)")
db.commit()
db.close()
print("Successful Created DataBase….")




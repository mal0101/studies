import sqlite3

db = sqlite3.connect("gestion.db")

db.execute("create table if not exists person(id integer)")
db.execute("insert into person(id) values(?)", (10, ))
db.execute("insert into person(id) values(?)", (11, ))

db.commit()

db.row_factory=sqlite3.Row
cursor = db.execute("select * from person")
for row in cursor:
    print(row["id"])
db.close()
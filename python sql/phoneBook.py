import sqlite3

with sqlite3.connect("phoneBook.db") as db:
	cursor = db.cursor()
	print(cursor)

	# cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
	# 	ID integer PRIMARY KEY,
	# 	"First Name" text NOT NULL,
	# 	Surname text NOT NULL,
	# 	"Phone Number" integer);""")
	# cursor.execute("""INSERT INTO Names(id, "First Name", Surname, "Phone Number")
	# 	VALUES("1", "Simon", "Howels", "4758475805749")
	# 	""")
	# db.commit()
	cursor.execute("SELECT * FROM Names")
	print(cursor.fetchall())
	
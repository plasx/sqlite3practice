import sqlite

connection = sqlite3.connect("test_database.db")

c = connection.cursor()

c.execute("CREATE TABLE People(FristName TEXT, LastName TEXT, Age INT)")

c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")


connection.commit()
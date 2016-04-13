import _sqlite3
import os
if os.path.exists('test_database.db'):
	os.remove('test_database.db')

first_name = input("Enter your first name: ")
last_name = "Rivera"
age = 291

people_values =	(
	('Ron',	'Obvious', 32),
	('Luigi', 'Vercotti', 43),
	('Arthur', 'Belling', 28)
)

person_data = first_name, last_name, age 

with _sqlite3.connect('test_database.db') as connection:
	c = connection.cursor()
	c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
	c.execute("INSERT INTO People VALUES(?, ?, ?)", person_data)
	c.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)
	c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",(28, 'Daniel','Rivera'))
	c.execute("SELECT * FROM People")
	for row in c.fetchall():
		print(row)

	c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
	while True:
		row = c.fetchone()
		if row is None:
			break
		print(row)

	connection.commit()
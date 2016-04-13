import _sqlite3

with sqlite3.connect("test_database.db") as connection:
	# perform any SQL operations using connection here
	c = connection.cursor()
	c.executescript("""
		DROP TABLE IF EXISTS People;
		CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
		INSERT INTO People VALUES('Ron', 'Obvious','42');
		""")
	# another way is to use tuples in this situation this is a parametereized statement which is good for security!
	people_values = (
		('Ron', 'Obvious', 42),
		('Luigi', 'Vercotti', 43),
		('Arthur', 'Belling', 28)
	)
	c.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)
	connection.commit()
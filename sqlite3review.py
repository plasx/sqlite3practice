import _sqlite3

roster_values = (
	('Jean-Baptiste Zorg', 'Human', 122),
	('Korbeen Dallas', 'Meat Popsicle', 100),
	("Ak'not", "Mangalore", -5)
	)
with _sqlite3.connect('test_database.db') as connection:
	c = connection.cursor()
	c.execute("CREATE Table Roster(Name TEXT, Species TEXT, IQ INT)")
	c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", roster_values)
	c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?", ("Human", "Korbeen Dallas", 100))
	c.execute("SELECT Name, IQ FROM Roster WHERE Species ='Human'")
	print("using fetchall()")
	for row in c.fetchall():
		print(row)

	## OR this one which doesn't stay in memory supposidly 
	print("using fetchone()")
	c.execute("SELECT Name, IQ FROM Roster WHERE Species ='Human'")
	while True:
		row = c.fetchone()
		if row is None:
			break
		print(row)
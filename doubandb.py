import sqlite3

conn = sqlite3.connect('dbmovie.db')
conn.execute('''CREATE TABLE MOVIE
	(ID AUTOINCRIMENT NOT NULL
	NAME CHAR(100) NOT NULL
	DIRECTOR CHAR(50) NOT NULL
	ACTCOR );

	''')
conn.close()
import sqlite3

conn = sqlite3.connect('test.db')
# conn.execute("""insert into movie values('这个杀手不太冷 Léon','吕克·贝松 Luc Besson','/subject/1295644/');
# 	""")
# conn.execute("""insert into celebrity values('吕克·贝松 Luc Besson','/celebrity/1031876/');
# 	""")
# conn.execute("""insert into celebrity values('让·雷诺 Jean Reno','/celebrity/1025182/');
# 	""")
conn.execute("""insert into movie_artist values('/subject/1295644/','/celebrity/1031876/');
	""")
conn.execute("""insert into movie_artist values('/subject/1295644/','/celebrity/1025182/');
	""")
conn.commit()
conn.close()
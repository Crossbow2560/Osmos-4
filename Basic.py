import  sqlite3

con = sqlite3.connect('database.db')
c = con.cursor()

c.execute("CREATE TABLE database(song_name varchar(30), initial_bpm int(4), final_bpm int(4))")
c.execute("insert into database values(lehra_do)")

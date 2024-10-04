import sqlite3

con = sqlite3.connect('database.db')
c = con.cursor()

c.execute("CREATE TABLE database(song_name varchar(30), song_lang varchar(20), initial_bpm int(4), final_bpm int(4))")
c.execute("INSERT INTO database VALUES('Moves like Jagger','English',70,85)")
c.execute("INSERT INTO database VALUES('kamariya','hindi',70,85)")
c.execute("INSERT INTO database VALUES('chammak challo','hindi',70,85)")
c.execute("INSERT INTO database VALUES('aaj ki raat','hindi',70,85)")
c.execute("INSERT INTO database VALUES('kaala chasma','hindi',70,85)")
c.execute("INSERT INTO database VALUES('bye bye bye','English',70,85)")
c.execute("INSERT INTO database VALUES('Funk of galactico','English',70,85)")
c.execute("INSERT INTO database VALUES('sunflower','English',85,95)")
c.execute("INSERT INTO database VALUES('Shinonuga E-wa','Japanese',85,95)")
c.execute("INSERT INTO database VALUES('Honeypie','English',85,95)")
c.execute("INSERT INTO database VALUES('Matargasti','hindi',85,95)")
c.execute("INSERT INTO database VALUES('senorita','hindi',85,95)")
c.execute("INSERT INTO database VALUES('cold','English',95,110)")
c.execute("INSERT INTO database VALUES('The lost soul','English',95,110)")
c.execute("INSERT INTO database VALUES('A birds last look','English',95,110)")
c.execute("INSERT INTO database VALUES('cupid','English',95,110)")
c.execute("INSERT INTO database VALUES('Kun Faya Kun','urdu',95,110)")
c.execute("INSERT INTO database VALUES('Tumhare hi Rahenge','hindi',95,110)")




import sqlite3
conector = sqlite3.connect("musicas.db")
cursor = conector.cursor()
sql = """
    CREATE TABLE Musicas
    (nummusica INTEGER PRIMARY KEY AUTOINCREMENT,
    nomemus TEXT,
    artista TEXT,
    album TEXT, 
    ano INTEGER,
    arquivo TEXT)
"""
cursor.execute(sql)
sql = """CREATE TABLE Nomespl
(nomepl TEXT PRIMARY KEY, data DATE)"""
cursor.execute(sql)
sql = """CREATE TABLE Playlist
    (nomepl NOT NULL, nummusica NOT NULL,
    PRIMARY KEY (nomepl, nummusica))
"""
cursor.execute(sql)
conector.commit()
cursor.close()
conector.close()
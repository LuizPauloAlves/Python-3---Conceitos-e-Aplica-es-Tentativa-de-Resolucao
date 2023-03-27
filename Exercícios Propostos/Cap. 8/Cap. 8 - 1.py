import sqlite3
conector = sqlite3.connect("Agenda.db")
cursor = conector.cursor()
sql = """
    create table Agenda
    (NumContato INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT,
    Cel TEXT,
    Tel TEXT,
    Email  TEXT,
    Aniver  TEXT)
"""
cursor.execute(sql)
sql = """
    insert into Agenda
    (Nome, Cel, Tel, Email, Aniver)
    VALUES ("ANA DO TESTE", "55 987654321", "55 123456789", "teste@email.com", "12/12/2000")
"""
cursor.execute(sql)
conector.commit()
cursor.close()
conector.close()
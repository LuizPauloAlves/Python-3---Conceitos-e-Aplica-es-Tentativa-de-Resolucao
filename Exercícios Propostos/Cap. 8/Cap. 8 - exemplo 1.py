import sqlite3
conector = sqlite3.connect("academia.db")
cursor = conector.cursor()
sql = """
    create table cadastro
    (codigo integer, nome text, idade integer)
"""
cursor.execute(sql)
sql = """
    insert into cadastro
    (codigo, nome, idade) values (1284, 'Pedro de Oliveira', 32)
"""
cursor.execute(sql)
sql = """
    insert into cadastro
    (codigo, nome, idade) values (1309, 'Maria Lúcia Machado', 37)
"""
cursor.execute(sql)
conector.commit()
cursor.close()
conector.close()
print("abra a pasta do programa e veja o arquivo la")
print("fim")
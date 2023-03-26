import sqlite3
conector = sqlite3.connect("academia.db")
cursor = conector.cursor()
sql = """
create table cursos (
    codcurso integer NOT NULL PRIMARY KEY,
    nomecurso text,
    valores double)"""
cursor.execute(sql)
sql = """
    insert into cursos (codcurso, nomecurso, valores) values (10, 'Musculacao', 110.00)
"""
cursor.execute(sql)
sql = """
    insert into cursos
    (codcurso, nomecurso, valores) values (?, ?, ?)
"""
arq = open("cursos.txt","r")
L = arq.readlines()
arq.close()
for s in L:
    d = s.rstrip()
    d = d.split(';')
    cursor.execute(sql, d)
    conector.commit()
    print(d," ...processado")
cursor.close()
conector.close()
print("\n\nBanco de dados atualizado com sucesso")
print("\n\nFim do programa")
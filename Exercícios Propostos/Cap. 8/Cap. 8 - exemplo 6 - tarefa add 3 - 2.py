import sqlite3
arq = open("cursos.txt",'r')
L = arq.readlines()
arq.close()
sql = """update cursos set nomecurso = ?, valores = ?
    where codcurso = ?"""
conector = sqlite3.connect("academia.db")
cursor = conector.cursor()
for s in L:
    d = s.rstrip()
    d = d.split(';')
    cursor.execute(sql, ( d[1], d[2], d[0] ))
    conector.commit()
    print(d," ...processado")
cursor.close()
conector.close()
print("\n\nBanco de dados atualizado com sucesso")
print("\n\nFim do programa")
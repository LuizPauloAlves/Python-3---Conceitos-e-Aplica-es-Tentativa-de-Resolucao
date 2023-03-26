import sqlite3
conector = sqlite3.connect("academia.db")
cursor = conector.cursor()
arq = open("Novos Alunos.txt","r")
L = arq.readlines()
arq.close()
sql = """
    insert into cadastro
    (codigo, nome, idade, curso, dtingr, peso, altura)
    values ( ?, ?, ?, ?, ?, ?, ?)
"""
print(" ...processado")
D = []
for s in L:
    d = s.rstrip()
    D.append(d.split(';'))
cursor.executemany(sql, D)
conector.commit()
cursor.close()
conector.close()
print("\n\nBanco de dados atualizado com sucesso")
print("\n\nFim do programa")
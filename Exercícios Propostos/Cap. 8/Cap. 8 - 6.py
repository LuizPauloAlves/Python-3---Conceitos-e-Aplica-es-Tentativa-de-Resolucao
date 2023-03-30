import sqlite3
conector = sqlite3.connect("loja.db")
cursor = conector.cursor()
sql = """CREATE TABLE vendas
    (codigo INTEGER PRIMARY KEY,
    qtde INTEGER,
    pccompra DOUBLE,
    pcvenda DOUBLE)
"""
cursor.execute(sql)
conector.commit()
arq = open("Vendas.txt","r")
L = arq.readlines()
arq.close()
sql = """INSERT INTO vendas (codigo, qtde, pccompra, pcvenda) VALUES (?,?,?,?)"""
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
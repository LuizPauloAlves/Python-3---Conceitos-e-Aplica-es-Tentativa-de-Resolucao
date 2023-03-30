import string
import secrets
import sqlite3

conector = sqlite3.connect("ra.db")
cursor = conector.cursor()
x = 1
if x == 1:
    sql = """CREATE TABLE RA
        (ra INTEGER PRIMARY KEY,
        senha TEXT)
    """
    cursor.execute(sql)
    conector.commit()
arq = open('RA.txt','r')
texto = arq.readlines()
arq.close()
alphabet = string.ascii_letters + string.digits
sql = """INSERT INTO RA (ra, senha) VALUES (?,?)"""
for s in texto:
    d = int(s)
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    cursor.execute(sql, (d,password))
    conector.commit()
    print(d," ...processado")
cursor.close()
conector.close()
print("\n\nBanco de dados atualizado com sucesso")
print("\n\nFim do programa")
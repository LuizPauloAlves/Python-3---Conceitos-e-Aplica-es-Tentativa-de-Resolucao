import sqlite3

conector = sqlite3.connect("academia.db")
cursor = conector.cursor()
sql = "alter table cadastro add curso integer"
cursor.execute(sql)
sql = "alter table cadastro add dtingr date"
cursor.execute(sql)
sql = "alter table cadastro add peso double"
cursor.execute(sql)
sql = "alter table cadastro add altura double"
cursor.execute(sql)
sql = "update cadastro set curso = 10, dtingr = '01/07/2017'"
cursor.execute(sql)
conector.commit()
cursor.close()
conector.close()
print("\n\nBanco de dados atualizados com sucesso")
print("\n\nFim do programa")
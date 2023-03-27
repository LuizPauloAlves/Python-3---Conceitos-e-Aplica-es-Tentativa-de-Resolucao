import sqlite3
conector = sqlite3.connect("Agenda.db")
cursor = conector.cursor()
sql = "select * from Agenda"
cursor.execute(sql)
dados = cursor.fetchall()
print("\nConsulta ao Banco de dados 'academia.db'\n")
print("Dados da tabela 'Agenda'")
print('-' * 120)
print("{:^7} {:<30} {:^15} {:^15} {:<30} {:^11}".format("Código", "Nome", "Cel", "Tel", "Email", "Data"))
print('- ' * 60)
for d in dados:
    print("{:^7} {:<30} {:^15} {:^15} {:<30}  {:^11}".format(d[0], d[1], d[2], d[3], d[4], d[5]))
print('-' * 120)
print("Encontrados {} registros\n".format(len(dados)))
cursor.close()
conector.close()
print("\n\nFim do programa")
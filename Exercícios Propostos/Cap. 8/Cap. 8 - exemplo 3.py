import sqlite3

def ExibeDados(L):
    """ Exibe uma saida formatada dos dados contidos em L"""
    print("\n Consulta ao Banco de Dados 'academia.db'\n")
    print("Dados da Tabela 'cadastro'")
    print('-' * 35)
    print("{:7} {:20} {:>6}".format("Código", "Nome", "Idade"))
    print('- '*18)
    for d in dados:
        print("{:<7} {:20} {:>6}".format(d[0], d[1], d[2]))
    print("-" * 35)
    print("Encontrados {} registros".format(len(dados)))

conector = sqlite3.connect("academia.db")
cursor = conector.cursor()
sql = """
    insert into cadastro
    (codigo, nome, idade) values (?, ?, ?)
"""
print("Digite os dados separados por virgula")
print("Código,Nome,Idade")
Ler = input()
while Ler != '':
    d = Ler.split(',')
    try:
        cursor.execute(sql,d)
        conector.commit()
    except:
        print("{} Dados Inválidos".format(d))
    else:
        print("."*30, "... dados inseridos com sucesso")
    finally:
        print("Código,Nome,Idade")
    Ler = input()

sql = "select * from cadastro"
cursor.execute(sql)
dados = cursor.fetchall()
cursor.close()
conector.close()
ExibeDados(dados)
print("\n\nFim do programa")
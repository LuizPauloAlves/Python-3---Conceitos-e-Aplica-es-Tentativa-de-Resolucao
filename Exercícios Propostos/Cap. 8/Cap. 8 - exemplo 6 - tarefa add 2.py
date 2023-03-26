import sqlite3

def ExibeDados(L):
    """ Exibe uma saida formatada dos dados contidos em L"""
    print("\nConsulta ao Banco de Dados ‘academia.db’ \n")
    print("Dados da tabela ‘cadastro’")
    print("-" * 76)
    print("{:7} {:26} {:6} {:6} {:13} {:4} {:>7}".format("Código", "Nome", "Idade", "Curso", "Ingresso", "Peso",
                                                         "Altura"))
    print("- " * 38)
    for d in dados:
        print("{:<7} {:25} {:5} {:6} {:>12} {:7} {:>6}".format(d[0], d[1], d[2], d[3], d[4], d[5], d[6]))
    print("-" * 76)
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
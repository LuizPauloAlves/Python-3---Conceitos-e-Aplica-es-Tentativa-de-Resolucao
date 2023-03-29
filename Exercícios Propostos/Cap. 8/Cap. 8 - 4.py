import sqlite3
import time


def alterar():
    qual = input("Qual musica quer alterar:")
    print("O que você quer alterar na musica:")
    print("1.Nome\n2.Artista\n3.Album\n4.Ano\n5.Arquivo")
    n = input("Digite sua mudança:")
    sqlalterar = ["nomemus = ", "artista = ", "album = ", "ano = ", "arquivo = "]
    NP, N = ["Nome", "Artista", "Album", "Ano", "Arquivo"], []
    while n != "" and len(N) <= 5:
        n = int(n)
        N.append(n - 1)
        n = input("Digite sua mudança:")
    print("Digite os novos ", end="")
    for i in N:
        print(NP[i], end=", ")
    print("separando por virgula (,):")
    Ler = input()
    d = Ler.split(',')
    sql = "UPDATE Musicas SET "
    for i in range(len(d)):
        sql = sql + sqlalterar[N[i]]+ '"' + d[i] + '"'
        if i != len(d)-1:
            sql += ", "
    sql = sql + " Where nummusica = "+ qual
    print(sql)
    try:
        cursor.execute(sql)
        conector.commit()
    except:
        print("Dados Invalidos")
    else:
        print("Dados inseridos com sucesso")


def excluir():
    print("Para excluir digite o Código")
    print("Para sair digite 0 (zero)")
    opc = int(input("sua escolha >>"))
    sql = """select Count(nummusica) from Musicas
                where nummusica = :param"""
    cursor.execute(sql, {'param': opc})
    x = cursor.fetchone()
    if x[0] == 0:
        return "Curso {} não existe".format(opc)
    else:
        sql = """delete from Musicas where nummusica = :param"""
        cursor.execute(sql, {'param': opc})
        conector.commit()
        return "Curso {} Excluido".format(opc)


def exibir():
    sql = "select * from Musicas"
    cursor.execute(sql)
    dados = cursor.fetchall()
    print("\nConsulta ao Banco de dados 'musicas.db'\n")
    print("Dados da tabela 'Musicas'")
    print('-' * 170)
    print("{:^7} {:^50} {:^25} {:^50} {:<5} {:>25}".format("Código", "Nome da Musica", "Artista", "Album", "Ano", "Nome do arquivo"))
    print('- ' * 85)
    for d in dados:
        print("{:^7} {:^50} {:^25} {:^50} {:<5} {:>25}".format(d[0], d[1], d[2], d[3], d[4], d[5]))
    print('-' * 170)
    print("Encontrados {} registros\n".format(len(dados)))

def inserir():
    sql = """INSERT INTO Musicas (nomemus, artista, album, ano, arquivo)
    VALUES (?, ?, ?, ?, ?)
    """
    print("Coloque o Nome,Artista,Album,Ano,Arquivo(.mp3)")
    print("separando por , os itens")
    Ler = input(">>")
    d = Ler.split(",")
    try:
        cursor.execute(sql, d)
        conector.commit()
    except:
        print("Dados Invalidos")
    else:
        for i in range(1, 4):
            print("." * i, end="")
            time.sleep(1)
        print("Dados inseridos com sucesso")

#codigo principal
conector = sqlite3.connect("musicas.db")
cursor = conector.cursor()
print("O que deseja:\n1.Adicionar uma musica\n2.Alterar uma musica\n3.Excluir uma musica")
print("4.Exibir as musicas atuais")
N = input("Digite sua escolha:")
while N != '':
    if N == '1':
        inserir()
    elif N == '2':
        exibir()
        alterar()
    elif N == '3':
        exibir()
        excluir()
    elif N == '4':
        exibir()
    print("O que deseja agora:\n1.Adicionar uma musica\n2.Alterar uma musica\n3.Excluir uma musica")
    print("4.Exibir as musicas atuais")
    N = input("Digite sua escolha:")
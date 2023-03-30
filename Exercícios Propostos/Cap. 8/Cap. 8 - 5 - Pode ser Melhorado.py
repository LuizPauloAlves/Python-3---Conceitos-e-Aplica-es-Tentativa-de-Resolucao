import sqlite3
import time


def alterar():
    sql = """update Nomespl set data = ?
        where nomepl = ?"""
    qual = input("Qual Código deseja alterar:")
    if qual != '':
        print("Escreva data")
        Ler = input()
        try:
            cursor.execute(sql, (Ler, qual))
            conector.commit()
        except:
            print("{} Dados Inválidos".format(d))
        else:
            print("." * 30, "... dados inseridos com sucesso")


def excluir(M):
    print("Para excluir digite o Código")
    print("Para sair digite 0 (zero)")
    opc = input("sua escolha >>")
    if M == '1':
        sql = """select Count(nomepl) from Nomespl
                    where nomepl = :param"""
    else:
        sql = """select Count(nummusica) from Playlist
                            where nummusica = :param"""
    cursor.execute(sql, {'param': opc})
    x = cursor.fetchone()
    if x[0] == 0:
        return "Curso {} não existe".format(opc)
    else:
        if M == '1':
            sql = """delete from Nomespl where nomepl = :param"""
        else:
            sql = """delete from Playlist where nummusica = :param"""
        cursor.execute(sql, {'param': opc})
        conector.commit()
        return "Curso {} Excluido".format(opc)


def exibirplaylist():
    sql = "select * from Nomespl"
    cursor.execute(sql)
    dados = cursor.fetchall()
    print("\nConsulta ao Banco de dados 'musicas.db'\n")
    print("Dados da tabela 'Nomespl'")
    print('-' * 40)
    print("{:^30} {:<10}".format("Nome", "Data"))
    print('- ' * 20)
    for d in dados:
        print("{:^30} {:<10}".format(d[0], d[1]))
    print('-' * 40)
    print("Encontrados {} registros\n".format(len(dados)))


def inserir(M):
    if M == "1":
        sql = """INSERT INTO Nomespl (nomepl, data)
        VALUES (?, ?)
        """
        print("Coloque o Nome da Playist, data")
    else:
        sql = """INSERT INTO Playlist (nomepl, nummusica)
                VALUES (?, ?)
                """
        print("Coloque o Nome da Playist e musica")
    print("separando por , os itens")
    Ler = input(">>")
    d = Ler.split(",")
    opc = d[1]
    sql1 = """select Count(nummusica) from Musicas
            where nummusica = :param"""
    cursor.execute(sql1, {'param': opc})
    x = cursor.fetchone();
    if x[0]!=0:
        try:
            cursor.execute(sql, d)
            conector.commit()
        except:
            print("Dados Invalidos")
        else:
            print("Dados inseridos com sucesso")
    else:
        print("musica não está na tabela musica")

#codigo principal
conector = sqlite3.connect("musicas.db")
cursor = conector.cursor()
print("O que deseja:\n1.Criar, alterar, excluir ou exibir Playliste\n2.Adicionar, remover ou exibir musicas de uma Playlist")
M = input("Digite sua escolha:")

while M != '':
    if M == "1":
        print("O que deseja:\n1.Adicionar uma Playlist\n2.Alterar dados de uma Playlist\n3.Remover uma Playlist")
        print("4.Exibir as playlist atuais")
        N = input("Digite sua escolha:")
        while N != '':
            if N == '1':
                inserir(M)
            elif N == '2':
                exibirplaylist()
                alterar(M)
            elif N == '3':
                exibirplaylist()
                excluir(M)
            elif N == '4':
                exibirplaylist()
            print("O que deseja:\n1.Adicionar uma Playlist\n2.Alterar dados de uma Playlist\n3.Remover uma Playlist")
            print("4.Exibir as playlist atuais")
            N = input("Digite sua escolha:")
    elif M == "2":
        print("O que deseja:\n1.Adicionar uma musica\n2.Remover uma musica")
        N = input("Digite sua escolha:")
        while N != '':
            while N != '':
                if N == '1':
                    inserir(M)
                elif N == '2':
                    exibirmusica()
                    excluir(M)
                print("O que deseja:\n1.Adicionar uma musica\n2.Remover uma musica")
                print("3.Exibir as musicas atuais")
                N = input("Digite sua escolha:")

    print("O que deseja:\n1.Criar, alterar, excluir ou exibir Playliste\n2.Adicionar, remover ou exibir musicas de uma Playlist")
    M = input("Digite sua escolha:")

conector.commit()
cursor.close()
conector.close()
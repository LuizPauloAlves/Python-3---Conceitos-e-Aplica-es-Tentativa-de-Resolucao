import sqlite3

def alterar():
    sql = """update Agenda set Cel = ?, Tel = ?, Email = ?
        where NumContato = ?"""
    qual = input("Qual Código deseja alterar:")
    if qual != '':
        print("Escreva o Cel, Tel, Email")
        print("Separando os dados por ,")
        Ler = input()
        d = Ler.split(',')
        try:
            cursor.execute(sql, (d[0], d[1], d[2], qual))
            conector.commit()
        except:
            print("{} Dados Inválidos".format(d))
        else:
            print("." * 30, "... dados inseridos com sucesso")

def cadastro():
    sql = """
        insert into Agenda
        (Nome, Cel, Tel, Email, Aniver)
        VALUES (?,?,?,?,?)
    """
    print("Escreva o nome, cel, tel, email, data de aniversario")
    print("Separando os dados por ,")
    Ler = input()
    d = Ler.split(',')
    try:
        cursor.execute(sql, d)
        conector.commit()
    except:
        print("{} Dados Inválidos".format(d))
    else:
        print("." * 30, "... dados inseridos com sucesso")

def excluir():
    print("Para excluir digite o Código")
    print("Para sair digite 0 (zero)")
    opc = int(input("sua escolha >>"))
    sql = """select Count(NumContato) from Agenda
            where NumContato = :param"""
    cursor.execute(sql, {'param': opc})
    x = cursor.fetchone()
    print(x[0])
    if x[0] == 0:
        return "Curso {} não existe".format(opc)
    else:
        sql = """delete from Agenda where NumContato = :param"""
        cursor.execute(sql, {'param': opc})
        conector.commit()
        return "Curso {} Excluido".format(opc)

def exibe():
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

conector = sqlite3.connect("Agenda.db")
cursor = conector.cursor()
qual = input("O que você deseja:\n1.Cadastrar\n2.Alterar os Telefones\n3.Excluir\nDigite sual Opção:")
while qual != "":
    if qual == "1":
        cadastro()
    elif qual == "2":
        exibe()
        alterar()
    elif qual == "3":
        exibe()
        excluir()
    qual = input("O que você deseja agora:\n1.Cadastrar\n2.Alterar os Telefones\n3.Excluir\nDigite sual Opção:")
cursor.close()
conector.close()
import sqlite3

def ExibeCursos():
    """Exibe os cursos existentes em daida formatada"""
    sql = "select * from cursos"
    cursor.execute(sql)
    dados  = cursor.fetchall()
    print("\nConsulta ao Banco de dados 'academia.db'\n")
    print("Dados da tabela 'cursos'")
    print('-'*49)
    print("{:7} {:30} {:>11}".format("Código","Nome do Curso","Val./Mês"))
    print('- '*25)
    for d in dados:
        print("{:7} {:30} {:>10.2f}".format(d[0],d[1],d[2]))
    print('-' * 49)
    print("Encontrados {} registros\n".format(len(dados)))

def ExcluiCurso(Codigo):
    """Verifica se o curso existe e o exclui"""
    sql = """select Count(codcurso) from cursos
        where codcurso = :param"""
    cursor.execute(sql, {'param' : Codigo})
    x = cursor.fetchone()
    print(x[0])
    if x[0] == 0:
        return "Curso {} não existe".format(Codigo)
    else:
        sql = """delete from cursos where codcurso = :param"""
        cursor.execute(sql, {'param': Codigo})
        conector.commit()
        return "Curso {} Excluido".format(Codigo)

#O programa começa a executar aqui
conector = sqlite3.connect("academia.db")
cursor = conector.cursor()
while True:
    ExibeCursos()
    print("Para excluir um curso digite o Código")
    print("Para sair do programa digite 0 (zero)")
    Opc = int(input("sua escolha >>"))
    if Opc == 0:
        break
    else:
        Msg = ExcluiCurso(Opc)
        print(Msg)
        dummy = input("pressione enter para prosseguir ... ")
cursor.close()
conector.close()
print("\n\nFim do programa")
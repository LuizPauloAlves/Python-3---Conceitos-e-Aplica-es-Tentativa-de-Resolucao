def GerenciaTorneio(t):
    global Times, Torneio, Turnos
    Torneio = t["nome"]
    Turnos = t["turnos"]
    Times = CarregaTimes()
    Qtde, NRod, NJog = CalcPramsTorneio()
    while True:
        TopoTela("Gerenciamento de Torneio")
        ExibeTimes()
        ExibeClassificacao()
        print("Opções: ")
        print(" (.) Para ver uma rodada digite seu número.")"
        print("     Rodadas Válidas de 1 a {}".format(Nrod))
        print(" (G) Grava o Torneio em HTML")
        print(" (E) Exclui o Torneio")
        print(" (S) Voltar ao Menu Principal")
        opc = input("sua opção? >>> ")
        opc = opc.upper()
        if opc == "N":
            NovoTorneio()
        elif opc.isnumeric():
            n = int(opc)
        if 1 <= n <= NRod:
            GerenciaRodada(n)
        elif opc == "G":
            GravaHTML()
        elif opc == "E":
            if ExcluiTorneio(Torneio):
                break
        elif opc == "S":
            break
    del(Times, Torneio, Turnos)
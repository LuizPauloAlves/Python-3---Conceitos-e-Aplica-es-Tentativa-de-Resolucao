def CalcPramsTorneio():
    global Times, Turnos
    Qtde = len(Times)
    if Qtde % 2 == 0:
        NRod = (Qtde - 1) * Turnos
    else:
        NRod = Qtde * Turnos
    NJog = (Qtde - 1) * Qtde // 2 * Turnos
    return Qtde, NRod, NJog

def ExibeTimes():
    global Times
    Qtde, NRod, NJog = CalcPramsTorneio()
    ExibeLinha("Times deste Torneio " + Torneio, 64)
    cont = 1
    s = ""
    for t in Times:
        s = s + "{:<15}".format(t[0])
        if cont % 4 == 0:
            ExibeLinha(s, 64)
            s = ""
        cont += 1
        if s != "":
            ExibeLinha(s, 64)
        ExibeLinha("", 64)
        s = "No de Rodadas: {} - No de Jogos: {}"
        ExibeLinha(s.format(NRod, NJog), 64)
        print("-" * LargTela)
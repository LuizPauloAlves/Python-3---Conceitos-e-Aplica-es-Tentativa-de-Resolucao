def GeraGravaJogos(NomeTorneio, QtdeTurnos, ListaTimes):
    Jogos = {}
    NJogo = 1
    Qtde = len(ListaTimes)
    if Qtde % 2 == 1:
    ListaTimes.append(“FOLGA”)
    Qtde += 1
    for r in range(Qtde-1):
        for i in range(Qtde//2):
            if ListaTimes[i] == “FOLGA” or
            ListaTimes[Qtde-1-i] == “FOLGA”:
                continue
            umJogo = {}
            umJogo[“rodada”] = r+1
            umJogo[“time1”] = ListaTimes[i]
            umJogo[“time2”] = ListaTimes[Qtde-1-i]
            Jogos[NJogo] = umJogo
            NJogo += 1
        aux = ListaTimes[1]
        del(ListaTimes[1])
        ListaTimes.append(aux)
    conector = sqlite3.connect(NomeTorneio + “.db”)
    cursor = conector.cursor()
    sql = '''
        insert into jogos (numjogo, numrod, time1, time2) values (?, ?, ?, ?)
    '''
    for NJogo, Jogo in Jogos.items():
        cursor.execute(sql, (NJogo, Jogo[“rodada”],
                             Jogo[“time1”], Jogo[“time2”]))
    if QtdeTurnos == 2:
        for NJogo, Jogo in Jogos.items():
            cursor.execute(sql, (NJogo+(Qtde-1)*Qtde/2,
                                 Jogo[“rodada”]+Qtde-1,
                                 Jogo[“time2”], Jogo[“time1”]))
    conector.commit()
    cursor.close()
    conector.close()

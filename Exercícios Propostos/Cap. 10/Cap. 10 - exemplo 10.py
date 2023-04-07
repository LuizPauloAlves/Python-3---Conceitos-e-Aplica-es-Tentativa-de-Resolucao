def generateRecordGame(nameTournament, numberShift, teamList):
    game = {}
    numberGames = 1
    amount = len(teamList)
    if amount % 2 == 1:
        teamList.append("Break")
        amount += 1
    for r in range(amount-1):
        for i in range(amount//2):
            if teamList[i] == "Break" or teamList[amount-1-i] == "Break":
                continue
            aGame = {}
            aGame["round"] = r+1
            aGame["team1"] = teamList[i]
            aGame["team2"] = teamList[amount-1-i]
            game[numberGames] = aGame
            numberGames += 1
        aux = teamList[1]
        del(teamList[1])
        teamList.append(aux)
    conector = sqlite3.connect(nameTournament + ".db")
    cursor = conector.cursor()
    sql = '''
        insert into jogos (numjogo, numrod, team1, team2) values (?, ?, ?, ?)
    '''
    for numberGames, games in game.items():
        cursor.execute(sql, (numberGames, games["round"],
                             games["team1"], games["team2"]))
    if numberShift == 2:
        for numberGames, games in game.items():
            cursor.execute(sql, (numberGames+(amount-1)*amount/2,
                                 games["round"]+amount-1,
                                 games["team2"], games["team1"]))
    conector.commit()
    cursor.close()
    conector.close()

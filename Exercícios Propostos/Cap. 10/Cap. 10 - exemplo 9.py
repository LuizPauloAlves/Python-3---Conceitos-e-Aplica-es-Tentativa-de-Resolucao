def createDBTournament(nameTournament, teamList):
    connector = sqlite3.connect(nameTournament+'.db')
    cursor = connector.cursor()
    sql = 'CREATE TABLE teams (nameteam TEXT)'
    cursor.execute(sql)
    sql = 'INSERT INTO teams (nameteam) VALUES (?)'
    for name in teamList:
        cursor.execute(sql, (name,))
    connector.commit()
    sql = '''
        CREATE TABLE games(
        numgame INT NOT NULL PRIMARY KEY ASC,
        numrod INT,
        team1 TEXT, gol1 INT,
        team2 TEXT, gol2 INT)'''
    cursor.execute(sql)
    cursor.close()
    connector.close()

def recordTournamentName(nameTournament, amountShift):
    connector = sqlite3.connect('tournament.db')
    cursor = connector.cursor()
    sql = 'INSET INTO tournament (nametournament , shift) VALUES (?,?)'
    cursor.execute(sql, (nameTournament, amountShift))
    connector.commit()
    cursor.close()
    connector.close()
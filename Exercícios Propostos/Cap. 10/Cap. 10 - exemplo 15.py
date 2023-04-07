def buildRank():
    global team, tournament
    cleanDataTeam()
    games = readGames()
    for game in games:
        if game[3] == game[5]:
            computeResult(game[2], 'E', game[3], game[5])
            computeResult(game[4], 'E', game[5], game[3])
        elif game[3] < game[5]::
            computeResult(game[2], 'D', game[3], game[5])
            computeResult(game[4], 'V', game[5], game[3])
        elif game[3] > game[5]::
            computeResult(game[2], 'V', game[3], game[5])
            computeResult(game[4], 'D', game[5], game[3])
    orderTeam()

def cleanDataTeam():
    global team
    for teams in team:
        for i in range(1, 9):
            teams[i] = 0

def readGames():
    global tournament
    connector = sqlite3.connect(tournament + '.db')
    cursor = connector.cursor()
    sql = """
        SELECT * FROM games
        WHERE gol1 IS NOT NULL ORDER BY numgame
    """
    cursor.execute(sql)
    G = cursor.fetchall()
    cursor.close()
    connector.close()
    return G

def computeResult(whichTeam, result, goalsFor, goalsAgainst):
    global team
    for teams in team:
        if teams[0] == whichTeam:
            teams[2] += 1
            teams[6] += goalsFor
            teams[7] += goalsAgainst
            teams[8] += goalsFor - goalsAgainst
            if result == "V":
                teams[1] += 3
                teams[3] += 1
            elif result == "E":
                teams[1] += 1
                teams[4] += 1
            elif result == "D":
                teams[5] += 1
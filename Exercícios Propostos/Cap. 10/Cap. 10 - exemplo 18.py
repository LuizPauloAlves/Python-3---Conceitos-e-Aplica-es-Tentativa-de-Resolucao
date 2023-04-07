import sqlite3


def getGamesRound(numberRound):
    global tournament
    connector = sqlite3.connect(tournament + '.db')
    cursor = connector.cursor()
    sql = "SELECT * FROM games WHERE numrod = ? ORDER BY numgame"
    cursor.execute(sql, (numberRound,))
    G = cursor.fetchall()
    cursor.close()
    connector.close()
    return G

def showGames(games):
    showLine("*** Round {} ***".format(games[0][1]),64)
    s = '{:<6}{:<16}{:<5}x{:>5}{:>16}'
    gRound = []
    for g in games:
        gRound.append(g[0])
        if g[3] == g[5] == None:
            showLine(s.format(g[0],g[2],'','',g[4]),64)
        else:
            showLine(s.format(g[0],g[2],g[3],g[5],g[4]),64)
    print('-'*widthScreen)
    return gRound
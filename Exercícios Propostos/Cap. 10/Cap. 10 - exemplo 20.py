import sqlite3


def cleanGame(game):
    global tournament
    connector = sqlite3.connect(tournament + ".db")
    cursor = connector.cursor()
    sql = """
        UPDATE games SET goals1 = NULL, goals2 = NULL
        WHERE numgame = ?
    """
    cursor.execute(sql, (game,))
    connector.commit()
    cursor.close()
    connector.close()

def updateGame(game, goals1, goals2):
    global tournament
    connector = sqlite3.connect(tournament + ".db")
    cursor = connector.cursor()
    slq = """
        UPDATE games SET goals1 = ?, goals2= ?
        WHERE numgame = ?
    """
    cursor.execute(sql, (goals1, goals2, game))
    connector.commit()
    cursor.close()
    connector.close()
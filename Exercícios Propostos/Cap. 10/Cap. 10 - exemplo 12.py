def loadTeam():
    global tournament
    T = []
    connector = sqlite3.connect(tournament + ".db")
    cursor = connector.cursor()
    sql = "select nameteam from teams order by nameteam"
    cursor.execute(sql)
    for team in cursor.fetchall():
        t = [team[0]] + [0]*8 T.append(t)
    cursor.close()
    connector.close()
    return T
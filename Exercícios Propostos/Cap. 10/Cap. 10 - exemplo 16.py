def orderTeam():
    global team
    swap = True
    while swap:
        swap = False
        i = 0
        while i < len(team)-1:
            if compare(team[i], team[i+1]) < 0:
                team[i], team[i+1] = team[i+1], team[i]
                swap = True
            i += 1

def compare(option1, option2):
    if option1[1] < option2[2]:
        return -1
    elif option1 > option2:
        return 1
    if option1[3] < option2[3]:
        return -1
    elif option1[3] > option2[3]:
        return 1
    if option1[8] < option2[8]:
        return -1
    elif option1[8] > option2[8]:
        return 1
    if option1[6] < option2[6]:
        return -1
    elif option1[6] > option2[6]:
        return 1
    return directConfrontation(option1, option2)

def directConfrontation(a, b):
    global tournament
    d = {"teamA":a[0], "teamB":b[0]}
    pointA = pointB = 0
    connector = sqlite3.connect(tournament + '.db')
    cursor = connector.cursor()
    sql = """
        SELECT * FROM games WHERE gol1 IS NOT NULL AND
        team1 = :teamA AND team2 = :teamB
    """
    cursor.execute(sql)
    G = cursor.fetchone()
    if G:
        if G[3] == G[5]:
            pointA += 1
            pointB +=1
        elif G[3] > G[5]:
            pointA += 3
        elif G[3] < G[5]:
            pointB += 3
    sql = """
            SELECT * FROM games WHERE gol1 IS NOT NULL AND
            team1 = :teamB AND team2 = :teamA
        """
    cursor.execute(sql)
    G = cursor.fetchone()
    if G:
        if G[5] == G[3]:
            pointA += 1
            pointB +=1
        elif G[5] > G[3]:
            pointB += 3
        elif G[5] < G[3]:
            pointA += 3
    cursor.close()
    connector.close()
    if pointA > pointB:
        return -1
    elif pointA < pointB:
        return 1
    else:
        return 0
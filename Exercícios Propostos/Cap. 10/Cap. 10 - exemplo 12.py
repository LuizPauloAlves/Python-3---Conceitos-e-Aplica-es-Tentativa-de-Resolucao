def CarregaTimes():
    global Torneio
    T = []
    conector = sqlite3.connect(Torneio + ".db")
    cursor = conector.cursor()
    sql = "select nometime from times order by nometime"
    cursor.execute(sql)
    for time in cursor.fetchall():
        t = [time[0]] + [0]*8 T.append(t)
    cursor.close()
    conector.close()
    return T
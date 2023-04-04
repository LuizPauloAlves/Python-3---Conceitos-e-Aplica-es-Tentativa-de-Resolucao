def prepareEnvironment():
    '''If the DB tournament.db exists, then read the tournament
       Otherwise, create DB necessary on first use of the program
    '''
    connector = sqlite3.connect('tournament.db')
    cursor = connector.cursor()
    sql = '''
        SELECT name FROM sqlite_master
        WHERE type = 'table' AND name = 'tournament'
    '''
    cursor.execute(sql)
    R = {}
    N = 1
    if cursor.fetchone() == None:
        sql = 'CREATE TABLE tournament (nametournament TEXT, shift INT)'
        cursor.execute(sql)
    else:
        sql = 'SELECT * FROM tournament'
        cursor.execute(sql)
        for x in sorted(cursor.fetchall()):
            item = {}
            item['nome'] = x[0]
            item['shift'] = x[1]
            R[N] = item
            N += 1
    cursor.close()
    connector.close()
    return R
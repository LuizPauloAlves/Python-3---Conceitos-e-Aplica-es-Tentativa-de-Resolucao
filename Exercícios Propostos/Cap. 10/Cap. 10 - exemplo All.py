#exemplo 1
from datetime import date
import os
import sqlite3
widthScreen = 70

#exemplo 2
mainMenu()
print('\n'*2)
showLine('Closed Tournament Program')
print('\n')
stop('Press Entrer to exit')

#exemplo 3
def mainMenu():
    while True:
        tournament = prepareEnvironment()
        topScreen('Main Menu')
        print('Options: ')
        print(' (N) Create New Tournament')
        print(' (.) Manage Existing Tournament')
        if len(tournament) == 0:
            print('      { There are no registered tournament}')
        else:
            for i, t in tournament.itens():
                print('         ({}) {}'.format(i, t['Name']))
        print(' (E) Exit the program')
        print('\nto choose type what is in parentheses')
        option = input('Your Option? >>>')
        option = option.upper()
        if option == 'N':
            createNewTournament()
        elif option.isnumeric():
            n = int(option)
            if n in tournament:
                manageTournament(Tournament[n])
        elif opc == 'E':
            break

#exemplo 4
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
            item['Name'] = x[0]
            item['shift'] = x[1]
            R[N] = item
            N += 1
    cursor.close()
    connector.close()
    return R

#exemplo 5
def showLine(msg, size = 0, align = '^'):
    edge = (widthScreen - size - 2) // 2
    sfmt = '{:'+ align + str(size) + '}'
    print('-'*edge,sfmt.format(msg),'-'*edge)

def stop(msg, size = 64):
    if msg != '':
        showLine(msg, size)
    input()

def topScreen(msg = ''):
    print('\n'*2, '-' * widthScreen, sep = '')
    showLine('Tournament Program', 40, '^')
    if msg != '':
        showLine(msg, 40, '^')
    print('-'*widthScreen)


#exemplo 6
def createNewTournament():
    nameTournament = input('\nName of new Tournament:')
    if not validateTournament(nameTournament):
        return None
    numberShift = getNumberShift()
    if numberShift == 0:
        return None
    topScreen('Create a New Tournament')
    showLine('New Tournament: '+ nameTournament, 64)
    showLine('(at any time type "quit" to quit',64)
    print('-'*widthScreen)
    showLine('Enter the names of participáting teams',70)
    showLine('Type "end" to complete and save team names',70)
    teamList = getNameTeam()
    if teamList:
        createDBTournament(nameTournament, teamList)
        recordTournamentName(nameTournament, numberShift)
        generateRecordGame(nameTournament, numberShift, teamList)

#exemplo 7
def validateTournament(nameTournament):
    if nameTournament == '':
        return False
    elif existTournament(nameTournament):
        stop(nameTournament + 'already exists (press Enter)')
        return False
    else:
        return True

def getNumberShift():
    while True:
        print('Type the number of shifts (1 or 2):')
        print('Type 0 for cancel')
        number = input('How many shifts? >>>')
        try:
            number = int(number)
        except:
            print('Invalid Input {}'.format(number))
        else:
            if 0 <= number <= 2:
                return number

#exemplo 8
def getNameTeam():
    L = []
    counter = 1
    while True:
        s = input('Team {:d}'.format(counter))
        if s.upper() == 'exit': return None
        if s.upper() == 'End': break
        L.append(s)
        counter += 1
    return L

#exemplo 9
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
        team1 TEXT, goals1 INT,
        team2 TEXT, goals2 INT)'''
    cursor.execute(sql)
    cursor.close()
    connector.close()

def recordTournamentName(nameTournament, numberShift):
    connector = sqlite3.connect('tournament.db')
    cursor = connector.cursor()
    sql = 'INSET INTO tournament (nametournament , shift) VALUES (?,?)'
    cursor.execute(sql, (nameTournament, numberShift))
    connector.commit()
    cursor.close()
    connector.close()

#exemplo 10
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
        insert into games (numgame, numrod, team1, team2) values (?, ?, ?, ?)
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


#exemplo 11
def manageTournament(t):
    global team, tournament, shift
    tournament = t["name"]
    shift = t["shift"]
    team = loadTeams()
    number, numberRound, numberGame = calculationsTournamentParameter()
    while True:
        topScreen("Manage Tournoment")
        showTeams()
        showRank()
        print("Options: ")
        print(" (.) To view a round enter its number.")"
        print("     Rounds Valid from 1 to {}".format(numberRound))
        print(" (R) Record tournament in HTML")
        print(" (D) Delete tournament")
        print(" (B) Back to Main Menu")
        option = input("your option? >>> ")
        option = option.upper()
        if option == "N":
            newTournoment()
        elif option.isnumeric():
            n = int(option)
        if 1 <= n <= numberRound:
            manageRounds(n)
        elif option == "R":
            recordHTML()
        elif option == "D":
            if deleteTournament(tournament):
                break
        elif option == "B":
            break
    del(team, tournament, shift)

#exemplo 12
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

#exemplo 13
def calculationsTournamentParameter():
    global team, shift
    number = len(team)
    if number % 2 == 0:
        numberRound = (number - 1) * shift
    else:
        numberRound = number * shift
    numberGame = (number - 1) * number // 2 * shift
    return number, numberRound, numberGame

def showTeams():
    global team
    number, numberRound, numberGame = calculationsTournamentParameter()
    showLine("Teams of this Tournament" + tournament, 64)
    counter = 1
    s = ""
    for t in team:
        s = s + "{:<15}".format(t[0])
        if counter % 4 == 0:
            showLine(s, 64)
            s = ""
        counter += 1
        if s != "":
            showLine(s, 64)
        showLine("", 64)
        s = "Number of Rounds: {} - Number of Games: {}"
        showLine(s.format(numberRound, numberGame), 64)
        print("-" * widthScreen)

#exemplo 14
def showRank():
    global team, tournament
    buildRank()
    sfmt = "{:>3} {:<16}" + "{:>6}"*8
    print("-" * widthScreen)
    s = "Rank;Team;PG;J;W;D;L;GF;GA;GD"
    print(sfmt.format(*s.split(";")))
    print("-" * widthScreen)
    rank = 1
    for teams in team:
        data = (rank,) + tuple(teams)
        print(sfmt.format(*data))
        rank += 1
    print("-" * widthScreen)

#exemplo 15
def buildRank():
    global team, tournament
    cleanDataTeam()
    games = readGames()
    for game in games:
        if game[3] == game[5]:
            computeResult(game[2], 'E', game[3], game[5])
            computeResult(game[4], 'E', game[5], game[3])
        elif game[3] < game[5]:
            computeResult(game[2], 'D', game[3], game[5])
            computeResult(game[4], 'V', game[5], game[3])
        elif game[3] > game[5]:
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
        WHERE goals1 IS NOT NULL ORDER BY numgame
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

#exemplo 16
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
        SELECT * FROM games WHERE goals1 IS NOT NULL AND
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
            SELECT * FROM games WHERE goals1 IS NOT NULL AND
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

#exemplo 17
def manageRounds(numberRound):
    global team, tournamnt, shift
    games = getGamesRound(numberRound)
    while True:
        topScreen("Manage Tournament")
        showTeams()
        gamesRound = showGames(games)
        print("Option:")
        print("  (.)  To update the score of a game type:")
        print("       Number Game, Goals A, Goals B example: 12,2,1")
        print("  (.)  To clean the score of a game type:")
        print("       Number Game, clean            example: 12,clean")
        print("  (B)  Back to Main Menu")
        option = input("your option? >>>")
        option = option.upper()
        if option == "B":
            break
        else:
            msg = processRoundEntry(option, gamesRound)
            if msg != None:
                stop(msg + " press Enter")
            else:
                games = getGamesRound(numberRound)

#exemplo 18
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

#exemplo 19
def processRoundEntry(option, gamesRound):
    option =  option.replace(" ", "")
    L = option.split(",")
    if len(L) != 2 and len(L) != 3:
        return "Invalid Input"
    if len(L) == 2:
        if L[0].isnumeric() and L[1] == "clean":
            game = int(L[0])
            if game in gamesRound:
                cleanGame(game)
                return None
            else:
                return "Another Round Game"
        else:
            return "Invalid Input"
    if len(L) == 3:
        try:
            game = int(L[0])
            goals1 = int(L[1])
            goals2 = int(L[2])
            if game in gamesRound:
                updateGame(game, goals1, goals2)
            else:
                return "Another Round Game"
        except:
            return "Invalid Input"
        finally:
            return None

#exemplo 20
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

#exemplo 21
import sqlite3


def deleteTournament(tournament):
    print("\n"*3)
    showLine("Confirm Exclusion From Tournament " + tournament, 40)
    print("Option: ")
    print("    (C) for Confirm")
    print("    any other key to return")
    option = input("your option? >>> ")
    option = option.upper()
    if option == "C":
        connector = sqlite3.connect("tournament.db")
        cursor = connector.cursor()
        sql = "DELETE FROM tournament WHERE nametournament = '" + \
            tournament + "'"
        print(tournament)
        print(sql)
        stop("-"*58)
        cursor.execute(sql)
        connector.commit()
        cursor.close()
        connector.close()
        os.remove(tournament + ".db")
        return True
    else:
        return False

#exemplo 22
def recordHTML():
    global team, tournament
    today = date.today()
    today = "{}/{}/{}".format(today.day, today.month, today.year)
    buildRank()
    sfmt = "<tr><td>{}</td><td style=’text-align:left’>{}</td>" + \
            "<td>{}</td>"*8 + "</tr>"
    position = 1
    table = ""
    for teams in team:
        data = (position,) + tuple(teams)
        table = table + sfmt.format(*data)
        position += 1
    file = open("gabarito.html", "r", encoding="UTF-8")
    html = file.read()
    file.close;
    html = html.replace("<...NomeTorneio...>", tournament)
    html = html.replace("<...today...>", today)
    html = html.replace("<...table...>", table)
    file = open(tournament+".html", "w", encoding="UTF-8")
    file.write(html)
    file.close()
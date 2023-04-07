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
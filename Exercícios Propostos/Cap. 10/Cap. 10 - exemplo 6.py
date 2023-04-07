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
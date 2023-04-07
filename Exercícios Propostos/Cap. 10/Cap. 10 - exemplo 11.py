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
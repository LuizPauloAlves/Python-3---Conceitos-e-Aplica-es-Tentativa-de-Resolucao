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
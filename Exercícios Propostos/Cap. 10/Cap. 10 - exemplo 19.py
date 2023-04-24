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
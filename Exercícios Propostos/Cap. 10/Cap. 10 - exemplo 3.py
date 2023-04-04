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
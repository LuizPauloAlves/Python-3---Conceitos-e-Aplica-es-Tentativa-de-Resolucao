def validateTournament(nameTournament):
    if nameTournament == '':
        return False
    elif existTournament(nameTournament):
        stop(nameTournament + 'already exists (press Enter)')
        return False
    else:
        return True

def getAmountTournament():
    while True:
        print('Type the amount of shifts (1 or 2):')
        print('Type 0 for cancel')
        amount = input('How many shifts? >>>')
        try:
            amount = int(amount)
        except:
            print('Invalid Input {}'.format(amount))
        else:
            if 0 <= amount <= 2:
                return amount
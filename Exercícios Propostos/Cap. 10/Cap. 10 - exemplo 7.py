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
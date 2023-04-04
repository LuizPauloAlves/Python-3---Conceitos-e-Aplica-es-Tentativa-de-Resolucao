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
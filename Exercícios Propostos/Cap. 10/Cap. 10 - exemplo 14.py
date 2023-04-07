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
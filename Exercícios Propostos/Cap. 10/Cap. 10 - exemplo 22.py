def recordHTML():
    global team, tournament
    today = date.today()
    today = "{}/{}/{}".format(today.day, today.month, today.year)
    buildRank()
    sfmt = "<tr><td>{}</td><td style=’text-align:left’>{}</td>" + \
            "<td>{}</td>"*8 + "</tr>"
    position = 1
    table = ""
    for teams in team:
        data = (position,) + tuple(teams)
        table = table + sfmt.format(*data)
        position += 1
    file = open("gabarito.html", "r", encoding="UTF-8")
    html = file.read()
    file.close;
    html = html.replace("<...NomeTorneio...>", tournament)
    html = html.replace("<...today...>", today)
    html = html.replace("<...table...>", table)
    file = open(tournament+".html", "w", encoding="UTF-8")
    file.write(html)
    file.close()
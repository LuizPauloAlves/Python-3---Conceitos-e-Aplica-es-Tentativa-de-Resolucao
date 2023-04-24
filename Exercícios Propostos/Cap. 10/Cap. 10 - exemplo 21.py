import sqlite3


def deleteTournament(tournament):
    print("\n"*3)
    showLine("Confirm Exclusion From Tournament " + tournament, 40)
    print("Option: ")
    print("    (C) for Confirm")
    print("    any other key to return")
    option = input("your option? >>> ")
    option = option.upper()
    if option == "C":
        connector = sqlite3.connect("tournament.db")
        cursor = connector.cursor()
        sql = "DELETE FROM tournament WHERE nametournament = '" + \
            tournament + "'"
        print(tournament)
        print(sql)
        stop("-"*58)
        cursor.execute(sql)
        connector.commit()
        cursor.close()
        connector.close()
        os.remove(tournament + ".db")
        return True
    else:
        return False
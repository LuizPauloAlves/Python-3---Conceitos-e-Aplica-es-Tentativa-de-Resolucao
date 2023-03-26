import sqlite3
conector = sqlite3.connect("academia2.db")
cursor = conector.cursor()
sql = """
create table cursos (
    codcurso integer NOT NULL PRIMARY KEY,
    nomecurso text,
    valores double)"""
cursor.execute(sql)
print("Código")
Ler = input()
while Ler != '':
    d = Ler.split(',')
    print(d)
    try:
        cursor.execute(sql,d)
        conector.commit()
    except:
        print("{} Dados Inválidos".format(d))
    else:
        print("."*30, "... dados inseridos com sucesso")
    finally:
        print("Código")
    Ler = input()
cursor.close()
conector.close()
print("\n\nBanco de dados criado e atualizado com sucesso")
print("\n\nFim do programa")
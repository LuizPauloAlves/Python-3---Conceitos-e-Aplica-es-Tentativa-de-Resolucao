import sqlite3
print("\n\nCria e carrega tabela ‘cursos’")
conector = sqlite3.connect("academia.db")
cursor = conector.cursor() 
#Cria a nova tabela
sql = """
    create table cursos
    (codcurso integer not NULL Primary Key,
    nomecurso text, valores double)
"""
cursor.execute(sql)
print("\n ...tabela cursos criada")
#Carrega com dados dos cursos
sql = """
    insert into cursos
    (codcurso, nomecurso, valores) values(?, ?, ?)
"""
DadosCursos = [
    (10, "Musculação", 110.00),
    (11, "Treino Aeróbico", 110.00),
    (12, "Combo 1: Musculação + Aeróbico", 180.00),
    (15, "Natação", 180.00),
    (22, "Pilates", 165.00),
    (25, "Combo 2: Pilates + Aeróbico", 240.00),
    (30, "Crossfit", 180.00),
    (41, "Muay Thai" , 140.00),
    (42, "Jiu Jitsu", 140.00),
    (43, "Boxe", 140.00)]
print("\n ...dados a serem carregados")
for dados in DadosCursos:
    print("    ", dados)
cursor.executemany(sql, DadosCursos)
conector.commit()
cursor.close()
conector.close()
print("\nTabela ‘cursos’ criada e carregada com sucesso")
print("\nFim do programa")
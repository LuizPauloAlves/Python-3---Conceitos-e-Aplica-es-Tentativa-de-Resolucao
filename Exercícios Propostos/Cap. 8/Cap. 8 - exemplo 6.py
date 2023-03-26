import sqlite3
print("\nCriação de Chave Primaria na tabela 'cadastro'")
conector = sqlite3.connect("academia.db")
cursor = conector.cursor()
sql = "create table temp as select * from cadastro"
cursor.execute(sql)
sql = "drop table cadastro"
cursor.execute(sql)
sql = """
create table cadastro (
    codigo integer NOT NULL PRIMARY KEY,
    nome text,
    idade integer,
    curso integer,
    dtingr date,
    peso double,
    altura double)"""
cursor.execute(sql)
sql = """
    insert into cadastro
    (codigo, nome, idade, curso, dtingr, peso, altura)
    select codigo, nome, idade, curso, dtingr, peso, altura
    from temp
"""
cursor.execute(sql)
conector.commit()
sql = "drop table temp"
cursor.execute(sql)
cursor.close()
conector.close()
print("\n\nBanco de dados atualizado com sucesso")
print("\n\nFim do programa")
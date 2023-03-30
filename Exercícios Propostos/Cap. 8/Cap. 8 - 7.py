import sqlite3
conector = sqlite3.connect("IR.db")
cursor = conector.cursor()
x = 2
if x == 1:
    sql = """CREATE TABLE IR
        (codigo INTEGER PRIMARY KEY AUTOINCREMENT,
        SalBruto DOUBLE,
        AliqINSS DOUBLE,
        VALINSS DOUBLE,
        AliqIR DOUBLE,
        DeducaoIR DOUBLE,
        VALIR DOUBLE,
        SalLiquido DOUBLE)
    """
    cursor.execute(sql)
    conector.commit()
arq = open("salario.txt","r")
textsalario = arq.readlines()
arq.close()
textS, textC = [], []
i = 0
for textsalario in textsalario:
    if i == 0:
        textS.append(textsalario.replace("\n",""))
        i += 1
    else:
        textS.append(float(textsalario.rstrip("\n")))
i=0
for textS in textS:
    textC.append([])
    if 'Bruto' == textS:
        a = 'SalBruto'
        textC[i].append(a)
        a = 'AliqINSS'
        textC[i].append(a)
        a = 'VALINSS'
        textC[i].append(a)
        i += 1
    elif textS < 1556.95:
        textC[i].append(textS)
        textC[i].append(8)
        textC[i].append(round(textS*0.08,2))
        i += 1
    elif textS < 2594.93 and textS >= 1556.95:
        textC[i].append(textS)
        textC[i].append(9)
        textC[i].append(round(textS * 0.09,2))
        i += 1
    elif textS < 5189.83 and textS >= 2594.93:
        textC[i].append(textS)
        textC[i].append(11)
        textC[i].append(round(textS * 0.11,2))
        i += 1
    elif textS >= 5189.83:
        textC[i].append(textS)
        textC[i].append(11)
        textC[i].append(570.88)
        i += 1
a = 'AliqIR'
textC[0].append(a)
a = 'DeducaoIR'
textC[0].append(a)
a = 'VALIR'
textC[0].append(a)
a = 'SalLiquido'
textC[0].append(a)
for i in range((len(textC))):
    if i != 0:
        valor = textC[i][0]-textC[i][2]
        if valor < 1903.99:
            textC[i].append(0)
            textC[i].append(0)
            textC[i].append(round((valor*0-0),2))
            textC[i].append(round((textC[i][0]-textC[i][2]-textC[i][5]),2))
        elif valor < 2826.66 and valor >= 1903.99:
            textC[i].append(7.5)
            textC[i].append(142.80)
            textC[i].append(round((valor * 0.075 - 142.80), 2))
            textC[i].append(round((textC[i][0] - textC[i][2] - textC[i][5]), 2))
        elif valor < 3751.06 and valor >= 2826.66:
            textC[i].append(15)
            textC[i].append(354.80)
            textC[i].append(round((valor * 0.15 - 354.80), 2))
            textC[i].append(round((textC[i][0] - textC[i][2] - textC[i][5]), 2))
        elif valor < 4664.68 and valor >= 3751.06:
            textC[i].append(22.5)
            textC[i].append(636.13)
            textC[i].append(round((valor * 0.225 - 636.13), 2))
            textC[i].append(round((textC[i][0] - textC[i][2] - textC[i][5]), 2))
        elif valor >= 4664.68:
            textC[i].append(27.5)
            textC[i].append(869.36)
            textC[i].append(round((valor * 0.275 - 869.36), 2))
            textC[i].append(round((textC[i][0] - textC[i][2] - textC[i][5]), 2))
    i += 1

sql = """INSERT INTO IR (SalBruto ,AliqINSS ,VALINSS ,AliqIR ,DeducaoIR ,VALIR ,SalLiquido )
        VALUES (?,?,?,?,?,?,?)"""

for s in textC[1:]:
    d = s
    print(d)
    cursor.execute(sql, d)
    conector.commit()
    print(d," ...processado")
cursor.close()
conector.close()
print("\n\nBanco de dados atualizado com sucesso")
print("\n\nFim do programa")
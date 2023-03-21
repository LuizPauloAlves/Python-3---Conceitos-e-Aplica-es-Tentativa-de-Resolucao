alunos = {}
N = 1
while N != 0:
    Nome = input("Nome do aluno:")
    if not(Nome in alunos) and Nome != '0':
        for i in range(4):
            valor = int(input("nota da Prova:"))
            if i == 0:
                alunos[Nome] = [valor]
            else:
                alunos[Nome].append(valor)
    elif Nome == "0":
        N = 0
for i in alunos.items():
    Media = sum(i[1])/4
    if Media >= 6:
        print(i[0],i[1],Media,"Aprovado")
    else:
        print(i[0],i[1],Media,"Reprovado")

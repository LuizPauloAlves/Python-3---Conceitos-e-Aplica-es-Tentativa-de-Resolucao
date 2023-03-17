Nprodutos = int(input("quantos produtos tem:"))
Nlojas = int(input("quantas lojas tem:"))
custo, estoque = [], [[] for _ in range(Nlojas)]
for i in range(Nprodutos):
    custo.append(float(input("O custo unitario do produto {} é:".format(i+1))))
print(custo)
for i in range(Nlojas):
    for j in range(Nprodutos):
        estoque[i].append(int(input("Na loja {} tem quantos do produto {}:".format(i+1,j+1))))
print(estoque)
somaloja = []
for i in range(Nlojas):
    somaloja.append(0)
    for j in range(Nprodutos):
        somaloja[i] += custo[j]*estoque[i][j]
print(somaloja)
somarede = []
for i in range(Nprodutos):
    somarede.append(0)
    for j in range(Nlojas):
        somarede[i] += custo[i]*estoque[j][i]
print(somarede)
somatotal = 0
for i in range(Nprodutos):
    somatotal += somarede[i]
print(somatotal)
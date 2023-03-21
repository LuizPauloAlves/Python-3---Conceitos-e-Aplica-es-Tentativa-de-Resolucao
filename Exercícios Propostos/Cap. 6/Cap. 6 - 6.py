pessoas = {}
Nome = 0
while Nome != "":
    Nome = input("Digite seu nome:")
    if not(Nome in pessoas) and Nome != "":
        idade = int(input("Idade:"))
        numero = input("Numero de Telefone:")
        pessoas[Nome] = [idade]
        pessoas[Nome].append(numero)

menores18, maiores18 = {},{}

for i in pessoas.items():
    if i[1][0] >= 18:
        maiores18[i[0]] = i[1]
    else:
        menores18[i[0]] = i[1]
pessoas.clear()
print(pessoas)
print(maiores18)
print(menores18)

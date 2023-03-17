n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo numero:"))
if n1 > n2:   #if para verificar se n1 é maior que n2
    print("O numero ", n1, "é maior que ", n2)
elif n2 != n1:   #elif para verifiar se n2 é diferente n1
    print("O numero ", n2, "é maior que ", n1)
else:
    print("O numero ", n1, "é igual que ", n2)
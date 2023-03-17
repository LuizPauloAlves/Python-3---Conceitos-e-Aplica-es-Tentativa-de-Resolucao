TotalP, TotalN = 0, 0
N = 1
while N != 0:
    N = int(input("Digite um número:"))
    if N > 0:
        TotalP += N
    elif N < 0:
        TotalN += N
print("O valor total da soma de número positivos é {}.\nO valor total da soma de numeros negativos é {}.".format(TotalP, TotalN))
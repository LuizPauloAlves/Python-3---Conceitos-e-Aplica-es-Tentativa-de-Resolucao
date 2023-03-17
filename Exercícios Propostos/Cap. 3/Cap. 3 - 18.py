n = int(input("digite um valor:"))
maior = n
menor = n
quant = 0
soma = 0
media = n
while n != 0 and n > 0:
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    quant += 1
    soma += n
    media = soma/quant
    n = int(input("digite um valor:"))
print("O maior valor {}".format(maior))
print("O menor valor {}".format(menor))
print("O quantidade de valores digitados {}".format(quant))
print("O valor da soma {}".format(soma))
print("O valor da média {}".format(media))

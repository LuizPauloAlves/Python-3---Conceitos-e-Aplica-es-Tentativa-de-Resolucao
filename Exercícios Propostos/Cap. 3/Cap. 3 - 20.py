n = int(input('Entre com um valor:'))
i, soma = 1, 0
while n < 100:
    n = int(input('Entre com um valor:'))
while i <= n:
    if i % 2 == 0:
        soma += i
    i += 1
print(soma)
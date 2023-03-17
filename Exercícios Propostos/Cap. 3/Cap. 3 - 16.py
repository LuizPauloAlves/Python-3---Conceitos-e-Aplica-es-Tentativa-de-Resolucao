n = int(input("Digite um valor interio>"))
N = float(input("Digite um valor real>"))
if n > N:
    print("O valor de {} é maior que {}".format(n, N))
elif N > n:
    print("O valor de {} é maior que {}".format(N, n))
else:
    print("O valores são iguais")

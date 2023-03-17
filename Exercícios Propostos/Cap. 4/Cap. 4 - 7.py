i = 0
A, NEG, POS = [], [], []
while i == 0:
    N = int(input("Digite um valor entre 0 a 50: "))
    if 50 >= N >= 0:
        i = 1
while i <= N:
    A.append(float(input("Digite um valor para a posição {}: ".format(i))))
    if A[i-1] >= 0:
        POS.append(A[i-1])
    else:
        NEG.append(A[i-1])
    i += 1
print("Valores Positivos")
print(POS)
print("Valores Negativos")
print(NEG)
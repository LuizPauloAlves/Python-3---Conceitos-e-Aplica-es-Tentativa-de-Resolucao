def divisivel(A, B):
    div = A % B
    if div == 0:
        return 1
    else:
        return 0

numA = int(input("digite A:"))
numB = int(input("digite B:"))
resultado = divisivel(numA, numB)
print(resultado)
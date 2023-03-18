def code(X):
    DM = X // 10000
    RX = X % 10000
    M = RX // 1000
    RX = RX % 1000
    C = RX // 100
    RX = RX % 100
    D = RX // 10
    RX = RX % 10
    U = RX // 1
    MDM = DM*2
    MM = M*3
    MC = C*4
    MD = D*5
    MU = U*6
    soma = MDM+MM+MC+MD+MU
    divisao = soma % 7
    return divisao

Numero = 0
while Numero > 30000 or Numero < 10000:
    Numero = int(input("Digite um numero entre 10.000 e 30.000:"))

print(code(Numero))
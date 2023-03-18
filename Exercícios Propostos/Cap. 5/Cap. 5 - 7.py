def entre(Min, Max):
    Numero = int(input("Novo Valor:"))
    while Min > Numero or Max < Numero:
        Numero = int(input("Erro *** Novo Valor:"))
    if Min <= Numero and Numero <= Max:
        return 'ok'

Maximo = int(input("Digite o Maximo:"))
Minimo = int(input("Digite o Minimo:"))
print(entre(Minimo, Maximo))
import random
def multiplica(L):
    multi = 1
    for i in range(len(L)):
        antes = multi
        multi = multi * L[i]
        print(antes,'*',L[i],'=',multi)
    return multi

valor = []
for j in range(10):
    valor.append(random.randint(1,10))

print(valor)
print(multiplica(valor))
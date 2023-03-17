pt = int(input("Digite o primeiro termo:"))
razao = int(input("Digite a razao:"))
q = int(input("Digite a quantidade:"))
i , pa = 1, []
pa.append(pt)
while i < q:
    pa.append(pt+razao*i)
    i +=1
print(pa)
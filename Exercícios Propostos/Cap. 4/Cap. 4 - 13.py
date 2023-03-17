m1, m2, soma = [[],[]], [[],[]], [[],[]]
for i in range(2):
    for j in range(2):
        m1[i].append(int(input("{}x{}:".format(i+1,j+1))))
print(m1)
for i in range(2):
    for j in range(2):
        m2[i].append(int(input("{}x{}:".format(i+1,j+1))))
print(m2)
for i in range(2):
    for j in range(2):
        soma[i].append(m1[0][j]*m2[i][0]+m1[1][j]*m2[i][1])
print(soma)
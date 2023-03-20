N = int(input("Valor"))
d = {}
dic = []
if N >0 :
    d[N] = 1
    dic.append(N)

while N > 0:
    N = int(input("Valor"))
    if N > 0:
        x = 0
        for i in range(len(dic)):
            if N == dic[i]:
                d[N] += 1
                x = 1
        if x != 1:
            d[N] = 1
            dic.append(N)

print(d)
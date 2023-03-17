import math   #biblioteca math para usar a função sqrt
#atribui os valores as variaveis A, B, C, x1 e x2, y1 e y2
A = 4
B = 5
C = 1
x1 = 1
y1 = 1
x2 = 4
y2 = 5
#expressões
#a
equa = (A + B)/2
print(equa)
#b
equa = (-B + math.sqrt(B**2 - 4*A*C))/(2*A)   #math. é para usar a função da biblioteca math
print(equa)
#c
equa = (3*A+2*B)/(A+B)
print(equa)
#d
equa = 7.6*A - B**(1.7)
print(equa)
#e
equa = math.sqrt((x1-x2)**2+(y1-y2)**2)
print(equa)
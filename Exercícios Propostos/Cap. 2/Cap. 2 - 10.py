p1 = input("Nome do produto:")
quant1 = int(input("Quantidade vendida:"))
valor1 = float(input("Valor unitario:"))
valortot1 = quant1*valor1
p2 = input("Nome do produto:")
quant2 = int(input("Quantidade vendida:"))
valor2 = float(input("Valor unitario:"))
valortot2 = quant2*valor2
p3 = input("Nome do produto:")
quant3 = int(input("Quantidade vendida:"))
valor3 = float(input("Valor unitario:"))
valortot3 = quant3*valor3
print(p1, " vendeu ", valortot1, " reais.")
print(p2, " vendeu ", valortot2, " reais.")
print(p3, " vendeu ", valortot3, " reais.")
valortot = valortot1 + valortot2 + valortot3
print("Vendeu no total de", valortot," reais!")
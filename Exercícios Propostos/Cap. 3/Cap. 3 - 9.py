nome = input("Seu nome:")
valorhora = float(input("Valor que você ganha por hora:"))
hora = int(input("Horas trabalhadas:"))
extra = int(input("Horas extras:"))
salario = valorhora * hora + 2 * valorhora * extra
print("O funcionario", nome, "vai receber o valor de", salario, "reais.")
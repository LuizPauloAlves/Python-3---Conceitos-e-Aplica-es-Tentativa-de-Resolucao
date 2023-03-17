nome = input("Digite seu nome:")
peso = float(input("Digite seu peso:"))
if peso < 65:
    print("O lutador", nome,"pesa", peso, "KG", "é peso Pena")
elif 65 <= peso and peso < 72:
    print("O lutador", nome,"pesa", peso, "KG", "é peso Leve")
elif 72 <= peso and peso < 79:
    print("O lutador", nome,"pesa", peso, "KG", "é peso Ligeiro")
elif 79 <= peso and peso < 86:
    print("O lutador", nome,"pesa", peso, "KG", "é peso Meio - médio")
elif 86 <= peso and peso < 93:
    print("O lutador", nome,"pesa", peso, "KG", "é peso Médio")
elif 93 <= peso and peso < 100:
    print("O lutador", nome,"pesa", peso, "KG", "é peso Meio - pesado")
else:
    print("O lutador", nome,"pesa", peso, "KG", "é peso Pesado")

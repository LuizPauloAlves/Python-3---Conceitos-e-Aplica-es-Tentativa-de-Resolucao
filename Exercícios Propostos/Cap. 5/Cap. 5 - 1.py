def par(x):
    if (x%2)==0:
      y = 'é par'
      return y
    else:
        y = 'é impar'
        return y

tipo = int(input("digite:"))

valor = par(tipo)
print(tipo,valor)
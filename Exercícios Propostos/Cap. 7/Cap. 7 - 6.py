import string
import secrets

arq = open('RA.txt','r')
texto = arq.readlines()
arq.close()
print(texto)
textoNW = []
for texto in texto:
    textoNW.append(int(texto.rstrip('\n')))
alphabet = string.ascii_letters + string.digits
arq = open('RASENHA.txt', 'w')
for textoNW in textoNW:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    x = str(textoNW) + ';' + str(password) + '\n'
    arq.write(x)
arq.close()
'''
x = input("Digite algo:")
x = x+'.txt'
arq = open(x,'w') cria um
arq.write('Testes 01\n')

x = 'teste1.txt'
arq = open(x,'a') #sobre escreve o arquivo apartir do final
'''
'''
from tkinter import Tk, Label, RAISED

root = Tk() #objeto da classe Tk
labels = [['1','2','3'],
          ['4','5','6'],
          ['7','8','9'],
          ['*','0','#']]
for r in range(4):
    for c in range(3):
        label = Label(root, relief=RAISED, padx=10,text=labels[r][c])
        label.grid(row=r,column=c)
root.mainloop() #chamada de uma função para criação da janela
'''
'''     '''
from tkinter import Tk, Button, Label #https://docs.python.org/pt-br/3/library/tkinter.html?highlight=tkinter#module-tkinter
from tkinter.messagebox import showinfo #https://docs.python.org/pt-br/3/library/tkinter.messagebox.html
from time import strftime, localtime #https://docs.python.org/pt-br/3/library/time.html#time.localtime

def clicked():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S%p\n', localtime())
    showinfo(message=time)#mostrar as Tempo na tela

root = Tk()
#janela principal
button = Button(root, text='Clique', command=clicked) #command chama a função clicked
button.pack() #empacotar a janela junto com o botão
root.mainloop()

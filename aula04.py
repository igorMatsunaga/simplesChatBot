# coding=utf-8

from tkinter import *
import unicodedata

root = Tk()


def remove_accents(b):
    normalized = unicodedata.normalize('NFKD', b)
    print(type(normalized))
    return ''.join([c for c in normalized if not unicodedata.combining(c)])


def click(event=None):
    send = 'Você: ' + a.get()
    text.insert(END, '\n' + send)
    b = a.get().lower()
    b = remove_accents(b)
    print('2', b)

    if b == 'oi':
        text.insert(END, '\n' + 'Bot: Oi, tudo bem?')
    elif b == 'ola':
        text.insert(END, '\n' + 'Bot: Olá, tudo bem?')
    elif b == 'bom dia':
        text.insert(END, '\n' + 'Bot: Bom dia, tudo bem?')
    else:
        text.insert(END, '\n' + 'Bot: Desculpe, ainda não conheço essa palavra')
    a.delete(0, 'end')


text = Text(root, bg='white')
text.grid(row=0, column=0, columnspan=2)

a = Entry(root, width=40)

send = Button(root, text='Enviar', bg='white', width=20,
              command=click).grid(row=1, column=1)
a.grid(row=1, column=0)

root.title('Gracebot aula03')
root.bind('<Return>', click)
root.mainloop()

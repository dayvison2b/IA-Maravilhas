from tkinter import *
import tkinter.messagebox

pergunta = tkinter.messagebox.askquestion(title='GITHUB', message='Você está prestes a entrar no github do criador do script, deseja continuar?')
print(pergunta)
if pergunta == 'yes':
    print('Hello world')
else:
    print('Você não escolheu sim')
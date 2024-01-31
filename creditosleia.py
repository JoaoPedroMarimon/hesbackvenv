import tkinter as tk
from PIL import Image, ImageTk

def abrir_segunda_janela():
    janelacre = tk.Tk()
    janelacre.geometry("400x200")
    janelacre.title("Créditos")
    texto = '''Código - Marimon
    imagens - Marimon
    roteiro - Marimon
    interface - Marimon
    
    ou seja, o marimon é foda'''
    janelacre.resizable(width=False, height=False)
    labelcre = tk.Label(janelacre, text=texto,font=("Helvetica", 15))
    labelcre.pack()


def abrir_terceira_janela():
    janelaleia = tk.Tk()
    janelaleia.geometry("700x300")
    janelaleia.title("Leia")
    janelaleia.resizable(width=False, height=False)
    texto = '''Espero que goste, pois confesso que deu um pouco
    de trabalho pra fazer esse joguinho ruim. Antes de pensar 
    abobrinhas, lembre-se que foi feito pelo tkinter, pois é.
    
    No jogo anterior voce era apenas um cubinho azul, agora
    voce é o marimon fds'''

    labelleia = tk.Label(janelaleia,text=texto,font=("Helvetica", 15))
    labelleia.pack()


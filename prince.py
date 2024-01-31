import tkinter as tk
import time
from PIL import Image, ImageTk
import pygame
from time import sleep
from creditosleia import *
from teste import *
from prince2 import *


def iniciar_cronometro():
    pygame.mixer.init()
    pygame.mixer.music.load("360ytmp3.com_320kbps-sonic-exe-laugh-sound-effect.mp3")
    pygame.mixer.music.play()
    atualizar_cronometro()
    botao_iniciar.pack_forget()
    frase = "doces:"
    label_frase = tk.Label(janela, text=frase, font=("Helvetica", 25))
    label_frase.place(x=370, y=7)
    imagem_label.place_forget()
    imagem_labelborba1.place_forget()
    botao_abrir_terceira_janela.place_forget()
    botao_abrir_segunda_janela.place_forget()
    usar_textoforever('Vida: 100/100','green',600,10)
    label_dano = tk.Label(janela, text=f'Força: 25/∞', font=("Helvetica", 15), fg='red')
    label_dano.place(x=200, y=10)



def mudar_numero(x):
    var_numero.set(x)


def escrever_arquivo(numero):
    with open("saida.txt", "w") as arquivo:
        arquivo.write(str(numero))

def escrever_arquivodamage(numero):
    with open("danojogador.txt", "w") as arquivo:
        arquivo.write(str(numero))


def escrever_arquivodoce(numero):
    with open("veridoce.txt", "w") as arquivo:
        arquivo.write(str(numero))

def escrever_arquivovidacombate(numero):
    with open("vidacombate.txt", "w") as arquivo:
        arquivo.write(str(numero))


def escrever_arquivopedra(numero):
    with open("pedrapapel.txt", "w") as arquivo:
        arquivo.write(str(numero))

def verificar_arquivo():
    with open("saida.txt", "r") as arquivo:
        conteudo = arquivo.read().strip()
    return conteudo


def verificar_arquivopedra():
    with open("pedrapapel.txt", "r") as arquivo:
        conteudo2 = arquivo.read().strip()
    return conteudo2


def atualizar_cronometro():
    global numero
    numero = var_numero.get()
    veri2 = verificar_arquivopedra()
    veri = verificar_arquivo()
    if veri == '1':
        numero += 1
        var_numero.set(f'{numero}')
    if numero == 36 and veri == "":
        numero += 0
        # var_numero2.set(f'{numero}')
        var_numero.set(f'{numero}')
    elif veri == "":
        numero += 1
        # var_numero2.set(f'{numero}')
        var_numero.set(f'{numero}')
    # label_numero2.config(font=("Helvetica", 24))
    # label_numero2.pack(pady=10)
    label_numero.config(font=("Helvetica", 24))
    label_numero.pack(pady=10)
    global timer_id
    timer_id = janela.after( 1500,atualizar_cronometro)
    if numero == 5 and veri == "":
        texto = '''Bom dia belo rapaz, eu sou a taylor swift, eu estou dando um show agora
    e gostaria muito que voce estivesse la, bom, eu vo cantar um pouco agora pra tentar te convencer a ir'''
        imagemborba('taylor swiftoriginal.png', 300, 300, 240, 250,20800)
        usar_audio('taylorded.mp3',0)
        usar_texto(texto, 'purple', -10, 170,12000)
    if numero == 19 and veri == "":
        imagemborbaforever('taylor swiftoriginalmorta.png',300, 220, 100, 430)
        imagemborba('kanyegun.jfif' ,300, 300, 650, 270,4400)
    if numero == 22 and veri == "":
        imagemborba('kanyewest.jfif',304,300,650,270,4000)
    if numero == 25 and veri == "":
        texto = '''Você: Meudeus, oque acabou de acontecer aqui? O Kanye West acabou de matar a taylor swift?!
        MEUDEUS!'''
        usar_texto(texto,'blue', 100, 240,6000)
    if numero == 30 and veri == "":
        texto = '''Ei, que barulho foi esse?
         HÃ, voce acabou de
        matar a taylor swift! vou
         te prender agora vagabundo'''
        imagemborbaforever('policial.jfif',304,300,250,80)
        usar_texto(texto,'black',580,80,4000000)
    if numero == 35 and veri == "":

        usar_audio('pampampam.mp3', -1)
        usar_botao('Subornar o policial: 34 doces',opcao1,16,650,230)
        usar_botao2('Enfrentar o policial', opcao2, 16, 650, 315)

    if veri2 == 'vitoria':
        escrever_arquivo(2)
    if veri2 == 'derrota':
        escrever_arquivo(3)



def opcao1():
    escrever_arquivovidacombate(7)
    pygame.mixer.music.stop()
    botao_iniciar5.place_forget()
    botao_iniciar6.place_forget()
    label.place_forget()
    escrever_arquivo(5)
    janela.destroy()
    escrever_arquivodoce(1)
    escrever_arquivopedra('vitoria')
    criar_janela()
    var_numero.set(2)



def opcao2():
    pygame.mixer.music.stop()
    escrever_arquivodamage(25)
    escrever_arquivovidacombate(7)
    escrever_arquivo(4)
    botao_iniciar5.place_forget()
    botao_iniciar6.place_forget()
    label.place_forget()
    janela.destroy()  # Fecha a janela atual
    executar_jogo('mari.jpg','policial.jfif')



def abrir_janela_jogo():
    print('vsf')


def imagemborba(image, L, A, X, Y,l):
    imagem_originalborba = Image.open(image)
    novo_tamanho = (L, A)
    imagem_redimensionadaborba = imagem_originalborba.resize(novo_tamanho)
    imagem_tkborba = ImageTk.PhotoImage(imagem_redimensionadaborba)
    global imagem_labelborba
    imagem_labelborba = tk.Label(janela, image=imagem_tkborba)
    imagem_labelborba.image = imagem_tkborba
    imagem_labelborba.place(x=X, y=Y)
    janela.after(l, lambda: imagem_labelborba.place_forget())

def imagemborbaforever(image, L, A, X, Y):
    imagem_originalborba2 = Image.open(image)
    novo_tamanho2 = (L, A)
    imagem_redimensionadaborba2 = imagem_originalborba2.resize(novo_tamanho2)
    imagem_tkborba2 = ImageTk.PhotoImage(imagem_redimensionadaborba2)
    global imagem_labelborba2
    imagem_labelborba2 = tk.Label(janela, image=imagem_tkborba2)
    imagem_labelborba2.image = imagem_tkborba2
    imagem_labelborba2.place(x=X, y=Y)


# 380,220
# 200,300
def usar_audio(file_audio,inf):
    pygame.mixer.init()
    pygame.mixer.music.load(file_audio)
    pygame.mixer.music.play(inf)


def usar_texto(text, color, x, y,l):
    global label
    label = tk.Label(janela, text=text, font=("Helvetica", 15), fg=color)
    label.place(x=x, y=y)
    janela.after(l, lambda: label.place_forget())


def usar_textoforever(text, color, x, y):
    global label2
    label2 = tk.Label(janela, text=text, font=("Helvetica", 15), fg=color)
    label2.place(x=x, y=y)

def usar_botao2(text, command, font, x, y):
    global botao_iniciar6
    botao_iniciar6 = tk.Button(janela, text=text, command=command, font=("Helvetica", font),bd=1, relief="solid")
    botao_iniciar6.place(x=x, y=y)



def usar_botao(text, command, font, x, y):
    global botao_iniciar5
    botao_iniciar5 = tk.Button(janela, text=text, command=command, font=("Helvetica", font),bd=1, relief="solid")
    botao_iniciar5.place(x=x, y=y)




janela = tk.Tk()
janela.geometry("1000x600")
janela.title("The attack of the Rocket-Borba 2")
janela.resizable(width=False, height=False)
global var_numero,botao_abrir_segunda_janela,botao_abrir_terceira_janela
var_numero = tk.IntVar(value=-1)
label_numero = tk.Label(janela, textvariable=var_numero, font=("Helvetica", 40))
botao_iniciar = tk.Button(janela, text="Jogar", command=iniciar_cronometro, font=("Helvetica", 20),bd=1, relief="solid")
botao_iniciar.pack(pady=10)



imagem_original = Image.open("hesbackimagem.png")
novo_tamanho = (500, 100)
imagem_redimensionada = imagem_original.resize(novo_tamanho)
imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)
imagem_label = tk.Label(janela, image=imagem_tk)
imagem_label.image = imagem_tk
imagem_label.place(x=250, y=120)

pygame.mixer.init()
pygame.mixer.music.load("Sonic.exe-Green-Hill-Zone-Song.mp3")
pygame.mixer.music.play(-1)

imagem_originalborba1 = Image.open('borbadevil.png')
novo_tamanho1 = (1000, 700)
imagem_redimensionadaborba1 = imagem_originalborba1.resize(novo_tamanho1)
imagem_tkborba1 = ImageTk.PhotoImage(imagem_redimensionadaborba1)
imagem_labelborba1 = tk.Label(janela, image=imagem_tkborba1)
imagem_labelborba1.image = imagem_tkborba1
imagem_labelborba1.place(x=-10, y=220)

botao_abrir_segunda_janela = tk.Button(janela, text="Créditos", command=abrir_segunda_janela, font=("Helvetica", 15))
botao_abrir_segunda_janela.place(x=10, y=10)
botao_abrir_terceira_janela = tk.Button(janela, text="Leia", command=abrir_terceira_janela, font=("Helvetica", 15))
botao_abrir_terceira_janela.place(x=945, y=10)


janela.mainloop()


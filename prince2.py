import tkinter as tk
from tkinter import messagebox
import time
from PIL import Image, ImageTk
import pygame
from time import sleep
from runbro import *
from teste3 import *

def iniciar_cronometro():
    atualizar_cronometro()

    frase = "doces:"
    label_frase = tk.Label(janela, text=frase, font=("Helvetica", 25))
    label_frase.place(x=370, y=7)



def escrever_arquivojogo(numero):
    with open("verijogo.txt", "w") as arquivo:
        arquivo.write(str(numero))



def escrever_arquivo(numero):
    with open("saida.txt", "w") as arquivo:
        arquivo.write(str(numero))

def verificar_arquivo():
    with open("saida.txt", "r") as arquivo:
        conteudo = arquivo.read().strip()
    return conteudo

def escrever_arquivopedra(numero):
    with open("pedrapapel.txt", "w") as arquivo:
        arquivo.write(str(numero))
def verificar_arquivopedra():
    with open("pedrapapel.txt", "r") as arquivo:
        conteudo2 = arquivo.read().strip()
    return conteudo2

def verificar_arquivodoce():
    with open("veridoce.txt", "r") as arquivo:
        conteudo3 = arquivo.read().strip()
    return conteudo3

def escrever_arquivodoce(numero):
    with open("veridoce.txt", "w") as arquivo:
        arquivo.write(str(numero))

def verificar_arquivoquatro():
    with open("veri4.txt", "r") as arquivo:
        conteudo4 = arquivo.read().strip()
    return conteudo4

def escrever_arquivoquatro(numero):
    with open("veri4.txt", "w") as arquivo:
        arquivo.write(str(numero))

def escrever_arquivovida(numero):
    with open("compravida.txt", "w") as arquivo:
        arquivo.write(str(numero))


def verificar_arquivovida():
    with open("compravida.txt", "r") as arquivo:
        conteudo5 = arquivo.read().strip()
    return conteudo5

def escrever_arquivodano(numero):
    with open("compradano.txt", "w") as arquivo:
        arquivo.write(str(numero))


def verificar_arquivodano():
    with open("compradano.txt", "r") as arquivo:
        conteudo6 = arquivo.read().strip()
    return conteudo6

def mudar_dano(numero):
    with open("danojogador.txt", "w") as arquivo:
        arquivo.write(str(numero))

def mudar_numero(x):
    var_numero.set(x)

def mudar_numero2(x):
    var_numero2.set(x)

def alterar_cor_fundo():
    if veri4 == "":
        if janela.cget('bg') == cor_padrao:
            janela.configure(bg=cor_vermelha)
        else:
            janela.configure(bg=cor_padrao)
        # Agendar a próxima mudança de cor após 2000 milissegundos (2 segundos)
        janela.after(50, alterar_cor_fundo)
    else:
        janela.configure(bg=cor_padrao)



def atualizar_cronometro():
    global numero, veri, cor_padrao,cor_vermelha,veri4,numero2,verivida,veridano
    numero = var_numero.get()
    numero2 = var_numero2.get()
    veri2 = verificar_arquivopedra()
    veri = verificar_arquivo()
    veri4 = verificar_arquivoquatro()
    veri3 = verificar_arquivodoce()
    verivida = verificar_arquivovida()
    veridano = verificar_arquivodano()
    label = tk.Label(janela, text=numero2, font=("Helvetica", 15), fg='black')
    label.place(x=800, y=10)
    if veri2 == "vitoria":
        numero2 += 1
        numero += 1
        mudar_numero(numero)
        mudar_numero2(numero2)
    if veri4 == 2:
        numero += 0
        mudar_numero(numero)
        numero2 += 0
        mudar_numero(numero2)


    if veri3 == '1' and numero == 2:
        usar_audio('comediaa.mp3',0)
        texto = '''Ta beleza, eu vou aceitar, mas
se tu contar pra alguem eu
te mato hein, comédia'''
        usar_texto(texto,'black',580,80,6000)
        imagemborbaforever('policial.jfif',304,300,250,80,8400)
        imagemborba('taylor swiftoriginalmorta.png',300, 220, 100, 430,8400)
    if veri4 == "9":
        janela.destroy()
    label_numero.config(font=("Helvetica", 24))
    label_numero.pack(pady=10)
    cor_padrao = "SystemButtonFace"
    cor_vermelha = "red"
    if veri3 == "" and numero == 51 or veri3 == "1" and numero == 16:
        usar_audio('terror.mp3',0)
        alterar_cor_fundo()

    if veri3 == "1" and numero == 20 or veri3 == "" and numero == 55:
        escrever_arquivoquatro(1)
    if veri3 == "1" and numero == 26 or veri3 == "" and numero == 61:
        imagemborbaforever('kanyemorto.png',300, 220, 600, 250,900000)
        imagemborba2('hesbackimagem.png',290,190,600,70,900000)
    if veri3== "" and numero == 74 or veri3 == "1" and numero == 39:
        janela.after(1,usar_texto('Voce: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA','blue',10,250,2500))
    if veri3 == "" and numero== 77 or veri3 == "1" and numero == 42:
        janela.after(500,imagemborba('borbadevil.png',290,290,190,140,900000))
    if veri3 == "" and numero == 78 or veri3 == "1" and numero == 43:
        texto = '''Ola amigo HAHA, gostou do presentinho
        que deixei pra voce ai?'''
        janela.after(500,usar_texto(texto,'red',150,450,8500))
    if veri3 == "" and numero == 84 or veri3 == "1" and numero == 49:
        texto = '''Ah não! voce denovo não, eu devia
         imaginar que voce voltaria'''
        janela.after(1,usar_texto(texto,'blue',150,450,4900))
    if veri3 == "" and numero == 88 or veri3 == "1" and numero == 53:
            messagebox.showerror("RUN", "CORRA, VOCE NAO VAI QUERER ENFRENTAR ELE")
            jogar_o_jogo()
    if veri3 == "" and numero == 89 or veri3 == "1" and numero == 54:
        texto = '''Voce escapou do Rocket-Borba
        Muito bem! fique sempre atento a ele.'''
        usar_audio('Victory - Sound Effect_EQtGmxuIPFY.mp3',0)
        usar_texto(texto,'green',190,140,7000)
        imagem_labelborba.place_forget()
    if veri3 == "" and numero == 92 or veri3 == "1" and numero == 57:
        imagem_labelborba3.place_forget()
        imagem_labelborba2.place_forget()

    if veri3 == "" and numero == 99 or veri3 == "1" and numero == 64:

        texto = '''Olá, eu sou o Matheus, e eu estou aqui
        para te vender alguns itens, eu recomendo que
        voce compre algumas coisas porque futuramente
        pode aparecer alguns inimigos um pouco mais
        fortes, e voce tem que ta preparado pra isso'''
        usar_audio('audioloja.mp3',0)
        imagemborba('matheus.jfif',300, 300,190,140,900000)
        usar_texto(texto,'pink',510,200,14000)

    if veri3 == "" and numero == 110 or veri3 == "1" and numero == 75:
        usar_botao('Poção de curar a vida: 40 doces',curar_vida,16,520,200)
        usar_botao2('espada/+25 de dano: 25 doces',aumentar_dano,16,520,295)
        usar_botao3('Continuar jornada',continuar_jornada,16,590,400)

    if veri3 == "" and numero == 111  or veri3 == "1" and numero == 76:
        escrever_arquivodoce(3)
        escrever_arquivopedra('derrota')

    if verivida == '1':
        numero -= 40
        mudar_numero(numero)
        escrever_arquivovida(2)
    if veridano == '1':
        numero -= 25
        mudar_numero(numero)
        escrever_arquivodano(2)
    if veri3 == "3" and numero2 == 77:
        texto = '''Ótima escolha de compra amigo, espero
        te ver denovo em alguma outra hora'''
        usar_audio('belaescolha.mp3',0)
        usar_texto(texto,'pink',510,200,7000)
    if veri3 == "3" and numero2 == 82:
        imagem_labelborba.place_forget()

    if veri3 == "3" and numero2 == 90:
        texto = '''SOCORRO SOCORRO, ALGUEM ME AJUDEEEE'''
        usar_audio('socorro.mp3',0)
        usar_texto(texto,'purple',190,140,6000)
    if veri3 == "3" and numero2 == 93:
        messagebox.showinfo('??????','Tenho que ajudar essa pessoa em perigo')
    if veri3 == "3" and numero2 == 95:
        texto = '''Fica quieta ai sua desgraçada, eu juro pra ti que se alguem escuta
        isso, eu vou matar voce.'''
        imagemborba('daneliya.jfif',280, 300,170,140,9000000)
        imagemborba2('bluesaoarmado.jfif',280, 300,470,140,9000000)
        usar_audio('tretablue.mp3',0)
        usar_texto(texto,'green',170,500,7800)

    if veri3 == "3" and numero2 == 101:
        texto = '''Fica parado ai seu bangueludo, eu juro pra ti que se
        tu encosta mais um dedo nela, eu arranco todos esses teus dentes que faltam.'''
        usar_texto(texto,'blue',170,500,8000)
    if veri3 == "3" and numero2 == 107:
        texto = '''Pode vir pra cima seu fracote, ja vou te adiantando que eu
        vou acabar contigo'''
        usar_textoforever(texto,'green',170,500)

    if veri3 == "3" and numero2 == 111:
        janela.destroy()  # Fecha a janela atual
        executar_jogo2('mari.jpg', 'bluesao.jfif')


    global timer_id
    timer_id = janela.after( 1500,atualizar_cronometro)



def curar_vida():
    escrever_arquivoquatro(2)
    if veri == 5:
        messagebox.showwarning('TUA VIDA TA CHEIA MONGOL')
    else:
        label_vida.config(text=f'Vida: 100/100',fg='green')
    escrever_arquivo(5)
    escrever_arquivovida(1)
    botao_iniciar5.place_forget()

def aumentar_dano():
    label_dano.config(text=f'Força: 50/∞')
    escrever_arquivodano(1)
    mudar_dano(50)
    botao_iniciar6.place_forget()


def continuar_jornada():
    escrever_arquivopedra('vitoria')
    escrever_arquivoquatro(5)
    botao_iniciar7.place_forget()
    if verivida == "":
        botao_iniciar5.place_forget()
    if veridano == "":
        botao_iniciar6.place_forget()





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

def imagemborbaforever(image, L, A, X, Y,l):
    imagem_originalborba2 = Image.open(image)
    novo_tamanho2 = (L, A)
    imagem_redimensionadaborba2 = imagem_originalborba2.resize(novo_tamanho2)
    imagem_tkborba2 = ImageTk.PhotoImage(imagem_redimensionadaborba2)
    global imagem_labelborba2
    imagem_labelborba2 = tk.Label(janela, image=imagem_tkborba2)
    imagem_labelborba2.image = imagem_tkborba2
    imagem_labelborba2.place(x=X, y=Y)
    janela.after(l, lambda: imagem_labelborba2.place_forget())


def imagemborba2(image, L, A, X, Y,l):
    imagem_originalborba3 = Image.open(image)
    novo_tamanho3 = (L, A)
    imagem_redimensionadaborba3 = imagem_originalborba3.resize(novo_tamanho3)
    imagem_tkborba3 = ImageTk.PhotoImage(imagem_redimensionadaborba3)
    global imagem_labelborba3
    imagem_labelborba3 = tk.Label(janela, image=imagem_tkborba3)
    imagem_labelborba3.image = imagem_tkborba3
    imagem_labelborba3.place(x=X, y=Y)
    janela.after(l, lambda: imagem_labelborba3.place_forget())


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


def usar_botao3(text, command, font, x, y):
    global botao_iniciar7
    botao_iniciar7 = tk.Button(janela, text=text, command=command, font=("Helvetica", font),bd=1, relief="solid")
    botao_iniciar7.place(x=x, y=y)

def criar_janela():
    global var_numero, janela, label_numero,label_vida, veri3,var_numero2,label_dano
    janela = tk.Tk()
    janela.geometry("1000x600")
    veri3 = verificar_arquivodoce()
    label_dano = tk.Label(janela, text=f'Força: 25/∞', font=("Helvetica", 15), fg='red')
    label_dano.place(x=200, y=10)
    label_vida = tk.Label(janela, text=f'Vida: 100/100', font=("Helvetica", 15), fg='green')
    label_vida.place(x=600, y=10)
    var_numero2 = tk.IntVar(value=0)
    if veri3 == "":
        var_numero = tk.IntVar(value=36)#94
        # var_numero2 = tk.IntVar(value=58)
    if veri3 == "1":
        var_numero = tk.IntVar(value=1)
    label_numero = tk.Label(janela, textvariable=var_numero, font=("Helvetica", 40))
    iniciar_cronometro()
    janela.title("The attack of the Rocket-Borba 2")
    if veri == '5':
        label_vida.config(text=f'Vida: 100/100',fg='green')
    if veri == '6':
        label_vida.config(text=f'Vida: 75/100',fg='yellow')
    if veri == '7':
        label_vida.config(text=f'Vida: 50/100',fg='orange')
    if veri == '8':
        label_vida.config(text=f'Vida: 25/100',fg='red')



    janela.mainloop()


import tkinter as tk
import random
from PIL import Image, ImageTk
import pygame
from prince2 import *


def verificar_arquivocombate():
    with open("vidacombate.txt", "r") as arquivo:
        conteudo = arquivo.read().strip()
    return conteudo


def verificar_arquivodamage():
    with open("danojogador.txt", "r") as arquivo:
        conteudo = arquivo.read().strip()
    return conteudo


veridamage = verificar_arquivodamage()
verivida = verificar_arquivocombate()
if verivida == "5":
    vida_usuario = 100
if verivida == "6":
    vida_usuario = 75
if verivida == "7":
    vida_usuario = 50
if verivida == "8":
    vida_usuario = 25

dano = veridamage

print(vida_usuario)
pontuacao_usuario = 0
pontuacao_computador = 0

vida_computador = 50


# Global variables

def jogar_pedra_papel_tesoura(escolha_usuario):
    global pontuacao_usuario, pontuacao_computador, vida_usuario, vida_computador

    esconder_botoes()

    opcoes = ["sorrateiro", "ataque", "defesa"]  # pedra papel e tesoura
    escolha_computador = random.choice(opcoes)
    resultado = ""
    if escolha_usuario == escolha_computador:
        resultado = "Empate!"
    elif (
            (escolha_usuario == "sorrateiro" and escolha_computador == "defesa") or
            (escolha_usuario == "ataque" and escolha_computador == "sorrateiro") or
            (escolha_usuario == "defesa" and escolha_computador == "ataque")
    ):
        resultado = "Você ganhou!"
        pontuacao_usuario += 2
        vida_computador -= int(dano)

    else:
        resultado = "Você perdeu!"
        pontuacao_computador += 1
        vida_usuario -= int(dano)

    label_resultado.config(text=f"Escolha do oponente: {escolha_computador}\nResultado: {resultado}")
    label_vida_usuario.config(text=f"Vida: {vida_usuario}/100")
    label_vida_computador.config(text=f"Vida: {vida_computador}/50")

    if vida_usuario == 100:
        escrever_arquivo(5)
    if vida_usuario == 75:
        escrever_arquivo(6)
    if vida_usuario == 50:
        escrever_arquivo(7)
    if vida_usuario == 25:
        escrever_arquivo(8)

    if vida_usuario == 0 or vida_computador == 0:
        mostrar_vencedor()
    else:
        janela_batalha.after(4000, mostrar_botoes)


def mostrar_botoes():
    for botao in botoes_opcao:
        botao.pack(side=tk.LEFT if botao["text"].lower() != "papel" else tk.RIGHT, padx=10)


def escrever_arquivo(numero):
    with open("saida.txt", "w") as arquivo:
        arquivo.write(str(numero))


def verificar_arquivocombate():
    with open("vidacombate.txt", "r") as arquivo:
        conteudo = arquivo.read().strip()
    return conteudo


def esconder_botoes():
    for botao in botoes_opcao:
        botao.pack_forget()


def mostrar_vencedor():
    global pontuacao_usuario, pontuacao_computador
    vencedor = "Você" if pontuacao_usuario == 4 else "Policial"
    mensagem = f"{vencedor} venceu o jogo!"
    if vencedor == "Você":
        pygame.mixer.init()
        pygame.mixer.music.load("Victory - Sound Effect_EQtGmxuIPFY.mp3")
        pygame.mixer.music.play()
    elif vencedor == "Policial":
        pygame.mixer.init()
        pygame.mixer.music.load("Factorio Defeat Sound Effect_r35qcOHUuZs.mp3")
        pygame.mixer.music.play()
    label_resultado.config(text=mensagem)
    esconder_botoes()
    registrar_resultado("vitoria" if pontuacao_usuario == 4 else "derrota")
    reiniciar_jogo()


def registrar_resultado(resultado):
    with open("pedrapapel.txt", "w") as arquivo:
        arquivo.write(f"{resultado}\n")
    veri2 = verificar_arquivopedra()
    if veri2 == "derrota":
        print("Burro")
    if verivida == 0:
        janela_batalha.destroy()
    if vida_computador == 0:
        janela_batalha.after(4000, janela_batalha.destroy())
    if veri2 == "vitoria":
        criar_janela()


def reiniciar_jogo():
    global pontuacao_usuario, pontuacao_computador
    pontuacao_usuario = 0
    pontuacao_computador = 0
    mostrar_botoes()

    # Função para iniciar o jogo
    # ... (código anterior)

    # Função para iniciar o jogo


def abrir_dica():
    janela_dica = tk.Toplevel()
    janela_dica.title("LEIALEIALEIA")
    janela_dica.geometry("300x230")
    texto = '''SEGUINTE.
    -ATAQUE GANHA DE SORRATEIRO
    -SORRATEIRO GANHA DE DEFESA
    -DEFESA GANHA DE ATAQUE

    JOGUE COM CUIDADO! POIS SUA VIDA
    SALVARÁ APOS A BATALHA

    BOA SORTE'''
    label = tk.Label(janela_dica, text=texto, font=("Helvetica", 10), fg='red')
    label.pack(pady=20)


def executar_jogo(n1, n2):
    global janela_batalha, label_resultado, label_vida_usuario, label_vida_computador, botoes_opcao, imagem_tk3, imagem_tk4
    janela_batalha = tk.Tk()
    janela_batalha.geometry("400x500")
    janela_batalha.title("Batalha")

    botao_abrir_dica = tk.Button(janela_batalha, text="LEIA", command=abrir_dica, font=("Helvetica", 10))
    botao_abrir_dica.place(x=10, y=10)

    pygame.mixer.init()
    pygame.mixer.music.load(
        "The Decisive Battle - Música de Suspense e Ação para usar em fundo de vídeos do YouTube__QNlsHrbkYE.mp3")
    pygame.mixer.music.play(-1)

    label_resultado = tk.Label(janela_batalha, text="", font=("Helvetica", 14))
    label_resultado.pack(pady=140)

    label_vida_computador = tk.Label(janela_batalha, text=f"Vida: {vida_computador}/50", font=("Helvetica", 12))
    label_vida_computador.place(x=150, y=200)

    label_vida_usuario = tk.Label(janela_batalha, text=f"Vida: {vida_usuario}/100", font=("Helvetica", 12))
    label_vida_usuario.place(x=150, y=250)

    imagem_original3 = Image.open(n1)
    novo_tamanho3 = (150, 150)
    imagem_redimensionada3 = imagem_original3.resize(novo_tamanho3)
    imagem_tk3 = ImageTk.PhotoImage(imagem_redimensionada3)
    imagem_label3 = tk.Label(janela_batalha, image=imagem_tk3)
    imagem_label3.image = imagem_tk3
    imagem_label3.place(x=220, y=320)

    imagem_original4 = Image.open(n2)
    novo_tamanho4 = (180, 110)
    imagem_redimensionada4 = imagem_original4.resize(novo_tamanho4)
    imagem_tk4 = ImageTk.PhotoImage(imagem_redimensionada4)
    imagem_label4 = tk.Label(janela_batalha, image=imagem_tk4)
    imagem_label4.image = imagem_tk4
    imagem_label4.place(x=100, y=20)

    opcoes = ["defesa", "ataque", "sorrateiro"]
    botoes_opcao = []

    for opcao in opcoes:
        botao = tk.Button(janela_batalha, text=opcao.capitalize(),
                          command=lambda opcao=opcao: jogar_pedra_papel_tesoura(opcao))
        botoes_opcao.append(botao)
        botao.pack(side=tk.LEFT if opcao.lower() != "papel" else tk.RIGHT, padx=4)

    janela_batalha.mainloop()


# Se este script for executado diretamente, chama a função jogar_jogo()
if __name__ == "__main__":
    executar_jogo()


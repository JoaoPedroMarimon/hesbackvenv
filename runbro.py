import pygame
import random
import math
import time
from time import sleep

# Função principal do jogo
def jogar_o_jogo():
    pygame.init()

    # Configurações da tela do jogo
    WIDTH, HEIGHT = 800, 600
    FPS = 60

    # Cores
    WHITE = (255,0, 0)
    RED = (255, 0, 0)

    # Classe para representar o jogador
    class Player(pygame.sprite.Sprite):
        def __init__(self, x, y, image_path):
            super().__init__()
            self.original_image = pygame.image.load(image_path)
            self.image = pygame.transform.smoothscale(self.original_image, (50, 50))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

        def move(self, keys):
            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
            if keys[pygame.K_RIGHT]:
                self.rect.x += 5
            if keys[pygame.K_UP]:
                self.rect.y -= 5
            if keys[pygame.K_DOWN]:
                self.rect.y += 5

            # Limita o movimento do jogador dentro da tela
            self.rect.x = max(self.rect.x, 0)
            self.rect.y = max(self.rect.y, 0)
            self.rect.x = min(self.rect.x, WIDTH - self.rect.width)
            self.rect.y = min(self.rect.y, HEIGHT - self.rect.height)

    # Classe para representar o computador (que tenta perseguir o jogador)
    class Computer(pygame.sprite.Sprite):
        def __init__(self, x, y, image_path):
            super().__init__()
            self.original_image = pygame.image.load(image_path)
            self.image = pygame.transform.smoothscale(self.original_image, (55, 55))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.speed = 0#4.9
            self.start_chase_time = None

        def start_chase(self):
            self.start_chase_time = time.time()

        def update(self, target_x, target_y):
            if self.start_chase_time is None:
                return

            # Movimento do computador para perseguir o jogador
            dx = target_x - self.rect.centerx
            dy = target_y - self.rect.centery
            distance = math.sqrt(dx ** 2 + dy ** 2)
            if distance > 0:
                self.rect.x += dx / distance * self.speed
                self.rect.y += dy / distance * self.speed

            # Limita o movimento do computador dentro da tela
            self.rect.x = max(self.rect.x, 0)
            self.rect.y = max(self.rect.y, 0)
            self.rect.x = min(self.rect.x, WIDTH - self.rect.width)
            self.rect.y = min(self.rect.y, HEIGHT - self.rect.height)

    def escrever_arquivoquatro(numero):
        with open("veri4.txt", "w") as arquivo:
            arquivo.write(str(numero))

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("RUN")

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    # Carrega as imagens do jogador e do computador
    player_image_path = "marivermei.jpg"
    player = Player(WIDTH // 4, HEIGHT // 2, player_image_path)

    computer_image_path = "borbadevilvermeioriginal.png"
    computer = Computer(WIDTH * 3 // 4, HEIGHT // 2, computer_image_path)

    all_sprites.add(player, computer)

    # Inicia o tempo
    start_time = time.time()

    # Loop principal do jogo
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        # Se o computador ainda não começou a perseguir, verifica se já se passaram 4 segundos
        if computer.start_chase_time is None:
            elapsed_time = time.time() - start_time
            if elapsed_time >= 4:
                pygame.mixer.init()
                pygame.mixer.music.load("sonic exe chase_816nYpit5zU.mp3")
                pygame.mixer.music.play()
                computer.start_chase()

        # Atualiza o computador com a posição atual do jogador
        computer.update(player.rect.centerx, player.rect.centery)

        # Verifica se o jogador alcançou o computador
        if pygame.sprite.collide_rect(player, computer):
            escrever_arquivoquatro(9)
            pygame.mixer.init()
            pygame.mixer.music.load("scream.mp3")
            pygame.mixer.music.play()
            print("Você morreu! Game Over.")
            sleep(5)
            running = False

        # Verifica se o tempo passou de 20 segundos
        elapsed_time = time.time() - start_time
        if elapsed_time >= 16:
            print("Parabéns! Você ganhou!")
            running = False

        # Limpa a tela
        screen.fill(WHITE)

        # Desenha os sprites na tela
        all_sprites.draw(screen)

        # Atualiza a tela
        pygame.display.flip()

        # Controla a taxa de quadros por segundo
        clock.tick(FPS)

    pygame.quit()

# Chama a função para jogar o jogo se este arquivo for executado diretamente
if __name__ == "__main__":
    jogar_o_jogo()

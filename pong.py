import pygame
import random
import os

# Inicializando o pygame
pygame.init()

# Definindo as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Largura e altura da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Configuração da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Definindo as classes de objetos do jogo
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([15, 100])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= 10

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = [random.choice([-4, 4]), random.choice([-4, 4])]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Verificando colisão com as bordas
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.velocity[1] = -self.velocity[1]
        
        # Verificando colisão com as paddles
        if self.rect.colliderect(left_paddle.rect) or self.rect.colliderect(right_paddle.rect):
            self.velocity[0] = -self.velocity[0]

        # Se a bola sair pela direita ou pela esquerda, reiniciar
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            self.velocity = [random.choice([-4, 4]), random.choice([-4, 4])]

# Inicializando as paddles e a bola
left_paddle = Paddle(WHITE, 50, SCREEN_HEIGHT // 2 - 50)
right_paddle = Paddle(WHITE, SCREEN_WIDTH - 65, SCREEN_HEIGHT // 2 - 50)
ball = Ball(WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Criando os grupos de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(left_paddle)
all_sprites.add(right_paddle)
all_sprites.add(ball)

# Definindo o relógio do jogo
clock = pygame.time.Clock()

# Inicializando o placar
left_score = 0
right_score = 0

# Função para desenhar o placar
def draw_score():
    font = pygame.font.SysFont("Arial", 36)
    score_text = font.render(f"{left_score}   {right_score}", True, WHITE)
    screen.blit(score_text, [SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20])

# Função para salvar a pontuação em um arquivo de texto
def save_score():
    if not os.path.exists("pontuacoes.txt"):
        with open("pontuacoes.txt", "w") as file:
            file.write("Pontuações:\n")
    
    with open("pontuacoes.txt", "a") as file:
        file.write(f"Esquerda: {left_score} | Direita: {right_score}\n")

# Loop principal do jogo
running = True
while running:
    screen.fill(BLACK)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimento das paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle.move_up()
    if keys[pygame.K_s]:
        left_paddle.move_down()
    if keys[pygame.K_UP]:
        right_paddle.move_up()
    if keys[pygame.K_DOWN]:
        right_paddle.move_down()

    # Atualizando a bola
    ball.update()

    # Atualizando o placar
    if ball.rect.left <= 0:
        right_score += 1
        ball.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    if ball.rect.right >= SCREEN_WIDTH:
        left_score += 1
        ball.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # Desenhando os sprites
    all_sprites.update()
    all_sprites.draw(screen)

    # Desenhando o placar
    draw_score()

    # Salvando o placar no arquivo
    if left_score == 5 or right_score == 5:  # Limite para terminar o jogo
        save_score()
        running = False

    # Atualizando a tela
    pygame.display.flip()

    # Definindo a taxa de atualização do jogo
    clock.tick(60)

pygame.quit()
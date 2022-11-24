import pygame 
import random
import sys

largura = 1200
altura = 720

fundo = 'imagens/ousadia_e_alegria.png'
fonte ='fonts/Tescaro Bold.ttf'
TRAVE = 'imagens/trave.webp'
BOLA = 'imagens/bola.jpg'
jogador = 'imagens/neymar.png'
FAZ = 'sons/faz.mp3'

pontos = 0
recorde = 0

velo = 600

pausa = False
fim_do_game = False

class Trave(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(TRAVE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

class Bola(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(BOLA).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound(FAZ)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shoot(self):
        global pontos
        self.sound.play()

        gol = pygame.sprite.spritecollide(bola, memoria_traves, False)
        for gol in gol:
            pontos += 1
            gol.kill()
            trave= Trave(random.randrange(0, largura), random.randrange(0,altura))
            memoria_traves.add(trave)

pygame.init()

screen = pygame.display.set_mode((largura,altura))

fundo = pygame.image.load(fundo).convert()
fundo = pygame.transform.scale(fundo, (largura, altura))

tempo = pygame.time.Clock()

fonte = pygame.font.Font(fonte, 50)

pygame.display.set_caption('RUMO AO HEXA - O GAME')

memoria_traves = pygame.sprite.Group()

for i in range(20):
    trave = Trave(random.randrange(0,largura),random.randrange(0,altura))
    memoria_traves.add(trave)


bola = Bola()
memoria_bolas = pygame.sprite.Group()
memoria_bolas.add(bola)

while not fim_do_game:

    if not pausa:
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausa = not pausa
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                bola.shoot()

        screen.blit(fundo, (0,0))
        memoria_traves.draw(screen)
        memoria_bolas.draw(screen)
        memoria_bolas.update()

        placar = fonte.render(f'GOLS DO NEY: {int(pontos)}', True,(0, 255, 0))
        screen.blit(placar, (50,50))

        velocidade_recorde = fonte.render(f'VELOCIDADE DO NEY: {velo/60:.1f}', True,(0, 255, 0))
        screen.blit(velocidade_recorde, (50,100))

        velo -= 1
        if velo < 0:
            velo = 600

            if pontos > recorde:
                recorde = pontos
                pontos = 0
            pausa = not pausa

    else:
        screen.fill((0, 255, 0))
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausa = not pausa

                
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pause = fonte.render(f" APERTE A TECLA ESC PARA INICIAR" ,True, (0,0,139))
        pontos_marcacao = fonte.render(f"RECORDE: {recorde} ", True, (0,0,139))

        pause_acao = pause.get_rect(center = (largura/2, altura/2))
        pontos_marcacao_acao = pontos_marcacao.get_rect(center = (largura/2, altura/2-50))

        screen.blit(pause, pause_acao)
        screen.blit(pontos_marcacao, pontos_marcacao_acao)

    pygame.display.flip()
    tempo.tick(60)
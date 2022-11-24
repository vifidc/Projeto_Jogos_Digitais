import pygame 
import random
import sys

largura = 1200
altura = 720

fundo = 'imagens/ousadia_e_alegria.png'
fonte ='fonts/Tescaro Bold.ttf'
alvo = 'imagens/trave'
mira = 'imagens/mira_alvo'
chute = 'imagens/pe_de_ouro'

pontos = 0
recorde = 0

timer = 1800

pausa = False
fim_do_game = False

pygame.init()

screen = pygame.display.set_mode((largura,altura))

fundo = pygame.image.load(fundo).convert()
fundo = pygame.transform.scale(fundo, (largura, altura))

tempo = pygame.time.Clock()

fonte = pygame.font.Font(fonte, 30)

pygame.display.set_caption('RUMO AO HEXA - O GAME')

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
            
            screen.blit(fundo, (0,0))

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
        pontos_marcacao_acao = pontos_marcacao.get_rect(center = (largura/2, altura/2-40))

        screen.blit(pause, pause_acao)
        screen.blit(pontos_marcacao, pontos_marcacao_acao)

    pygame.display.flip()
    tempo.tick(60)
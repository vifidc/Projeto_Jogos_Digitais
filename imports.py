import pygame 
import random
import sys

largura = 1200
altura = 720

fundo = 'imagens/ousadia_e_alegria.png'
fonte ='imagens/'
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

pygame.display.set_caption('RUMO AO HEXA - O GAME')

while not fim_do_game:
    if not pausa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            screen.blit(fundo, (0,0))

    pygame.display.flip()
    tempo.tick(60)
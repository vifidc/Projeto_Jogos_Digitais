import pygame, random, os, sys
from pygame.locals import *

pygame.init()

def run_main():
    import main.py

volume = 1
size = (900, 506)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('RUMO AO HEXA')

font = pygame.font.SysFont('Tescaro Bold.ttf', 50)
fonte_principal = pygame.font.SysFont("Tescaro Bold.ttf", 100)

folder = "imagens"

cenarios = ('imagens/hexa.webp')
cenario = pygame.image.load(cenarios)

preto = [0, 0, 0]

texto_principal = fonte_principal.render(("RUMO AO HEXA"), True, (0, 255, 0))
screen.blit(texto_principal, [255, 125])


bg = (204, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)


clicked = False
counter = 0

musica = {}
musica["despause"] = pygame.mixer.music.load('sons/copa.mp3')
pygame.mixer.music.play(-1)

som = {}
som["despause"] = pygame.mixer.Sound('sons/copa.mp3')

class menu():
    
    button_col = (white)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = black
    width = 180
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):

        global clicked
        action = False

       
        pos = pygame.mouse.get_pos()

        
        button_rect = Rect(self.x, self.y, self.width, self.height)

        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)


        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action

def como_jogar():
    import sys, pygame, os, random

    pygame.init()

    size = (900, 506)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("RUMO AO HEXA")

    folder = "imagens"

    cenarios = ('imagens/hexa.webp')
    cenario = pygame.image.load(cenarios)

    branco = [0, 0, 0]

    fonte_texto = pygame.font.SysFont("Tescaro Bold.ttf", 50)
    titulo = pygame.font.SysFont("Tescaro Bold.ttf", 50)

    msg_titulo = titulo.render(("Como jogar:"), True, (0,0,139))
    texto = fonte_texto.render(("Utilize o mouse para fazer o Gol! É só clicar!"), True, (0, 255, 0))
    texto2 = fonte_texto.render(("Tente vencer seus amigos!"), True, (0, 255, 0))

    msg_dificuldade1 = fonte_texto.render(("Voce tem 10 segundos para fazer os Gols"), True, (0, 255, 0))

    while True:

        screen.blit(cenario, (0, 0))

        if jogar.draw_button():
            run_main()
            pygame.display.update()
        if voltar.draw_button():
            menu(240, 240, 'Jogar')
            menu(470, 240, 'Instruções')
            menu(470, 240, 'Voltar')
            menu(240, 340, 'Tirar som')
            menu(500, 340, 'Colocar som')
            pygame.display.update()
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if (x > 190 and x < 270) and (y > 380 and y < 500):
                    if (volume == 1):
                        som["despause"].play()
                    menu()

        screen.blit(msg_titulo, [3, 3])
        screen.blit(texto, [3, 70])
        screen.blit(texto2, [3,100])
        screen.blit(msg_dificuldade1, [3, 150])

        pygame.display.flip()


jogar = menu(240, 240, 'Jogar')
instrucao = menu(470, 240, 'Instruções')
voltar = menu(470, 240, 'Voltar')
tirar_som = menu(240, 340, 'Tirar som')
colocar_som = menu(500, 340, 'Colocar som')


while True:

    screen.blit(cenario, (0, 0))
    screen.blit(texto_principal, [255, 125])

    if jogar.draw_button():
        run_main()
    if instrucao.draw_button():
        como_jogar()
    if tirar_som.draw_button():
        if(volume == 1):
            pygame.mixer.music.pause()
    if colocar_som.draw_button():
        pygame.mixer.music.unpause()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

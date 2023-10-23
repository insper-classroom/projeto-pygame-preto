import pygame

def inicializa():
    pygame.init()
    window = pygame.display.set_mode((800,700))
    pygame.display.set_caption('JOGO DA COBRINHA')

    dicionario = {}
    dicionario['game over'] = pygame.image.load('imagens/game over.png')

    return window,dicionario

def recebe_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def desenha(window,dicionario):
    window.fill((0,149,0))
    
    window.blit(dicionario['game over'],(120,190))

    pygame.display.update()

def game_loop(window,dicionario):
    while recebe_eventos():
        desenha(window,dicionario)
    
w,d = inicializa()
game_loop(w,d)
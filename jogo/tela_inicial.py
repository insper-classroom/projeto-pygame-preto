import pygame
def inicializa():
    pygame.init()
    window = pygame.display.set_mode((800,800))
    pygame.display.set_caption('JOGO DA COBRINHA')
    return window

def recebe_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def desenha(window):
    window.fill((0,0,0))
    
    window.blit(pygame.image.load())
    pygame.display.update()

def game_loop(window):
    while recebe_eventos():
        desenha(window)
    
w = inicializa()
game_loop(w)
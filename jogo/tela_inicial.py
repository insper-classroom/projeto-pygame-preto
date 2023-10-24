import pygame
def inicializa():
    #janela
    pygame.init()
    window = pygame.display.set_mode((800,700))
    pygame.display.set_caption('JOGO DA COBRINHA')

    dicionario = {}

    #desenho da cobra
    dicionario['cobra'] = pygame.image.load('imagens/cobra.png')
    dicionario['cobra'] = pygame.transform.scale(dicionario['cobra'],(200,200))

    #imagem bem vindos
    dicionario['bem vindo'] = pygame.image.load('imagens/bem vindos.png')

    return window,dicionario
    
   

def recebe_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def desenha(window,dicionario):
    window.fill((0,149,0))
    
    window.blit(dicionario['cobra'],(170,180))
    window.blit(dicionario['bem vindo'],(0,0))
    
    pygame.display.update()

def game_loop(window,dicionario):
    while recebe_eventos():
        desenha(window,dicionario)
    
w,d= inicializa()
game_loop(w,d)


    

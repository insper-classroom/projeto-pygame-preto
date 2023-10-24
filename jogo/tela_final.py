import pygame

def inicializa():
    pygame.init()
    window = pygame.display.set_mode((800,700))
    pygame.display.set_caption('JOGO DA COBRINHA')

    dicionario = {}
    dicionario['game over'] = pygame.image.load('imagens/game over.png')

    dicionario['caveira'] = pygame.image.load('imagens/caveira.png')
    dicionario['caveira'] = pygame.transform.scale(dicionario['caveira'],(130,130))

    dicionario['fonte'] = pygame.font.Font('fonte/retro_computer_personal_use.ttf',15)

    return window,dicionario

def recebe_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def desenha(window,dicionario):
    window.fill((0,149,0))
    
    window.blit(dicionario['game over'],(120,50))

    window.blit(dicionario['caveira'],(300,220))

    texto = dicionario['fonte'].render('Pressione ENTER para recomecar',False,(0,0,0))
    window.blit(texto,(200,480))

    pygame.display.update()

def game_loop(window,dicionario):
    while recebe_eventos():
        desenha(window,dicionario)
    
w,d = inicializa()
game_loop(w,d)
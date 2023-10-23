import pygame
def inicializa():
    pygame.init()
    window = pygame.display.set_mode((800,800))
    pygame.display.set_caption('JOGO DA COBRINHA')
    assets = {'fonte16':pygame.font.Font(pygame.font.get_default_font(),16)
    }
    return window, assets

def recebe_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def desenha(window, assets):
    window.fill((0,0,0))
    fonte16 = assets['fonte16'].render("Bem Vindos ao jogo da Cobrinha", True, (255, 255, 255))
    window.blit(fonte16,(280, 80))
    fonte16_2 = assets['fonte16'].render("Instuções do jogo:", True, (255, 255, 255))
    window.blit(fonte16_2,(100,500))
    fonte16_3 = assets['fonte16'].render("Regras do jogo bla bla e bla", True, (255, 255, 255))
    window.blit(fonte16_3,(100,530))
    fonte16_4 = assets['fonte16'].render("clique para iniciar", True, (255, 255, 255))
    window.blit(fonte16_4,(500,530))
    
    pygame.display.update()

def game_loop(window,assets):
    while recebe_eventos():
        desenha(window, assets)
    
w,a = inicializa()
game_loop(w,a)
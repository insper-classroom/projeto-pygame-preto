import pygame

def inicializa():
    #janela
    pygame.init()
    window = pygame.display.set_mode((800,700))
    pygame.display.set_caption('JOGO DA COBRINHA')

    dicionario = {}
    #INSTRUCOES FONTE
    dicionario['fonte'] = pygame.font.Font('fonte/retro_computer_personal_use.ttf',15)

    #desenho da cobra
    dicionario['cobra'] = pygame.image.load('imagens/cobra.png')
    dicionario['cobra'] = pygame.transform.scale(dicionario['cobra'],(200,200))

    #imagem bem vindos
    dicionario['bem vindo'] = pygame.image.load('imagens/bem vindos.png')

    #IMAGEM START
    dicionario['start'] = pygame.image.load('imagens/start.png')

    return window,dicionario
    
   

def recebe_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def desenha(window,dicionario):
    window.fill((0,149,0))
#DESENHAR A COBRA
    window.blit(dicionario['cobra'],(270,180))
    window.blit(dicionario['bem vindo'],(170,0))
#DESENHAR AS INSTRUÇOES
    texto = dicionario['fonte'].render('Clique para iniciar',False,(0,0,0))
    window.blit(texto,(270, 550))
#DESENHAR O START
    window.blit(dicionario['start'],(260,500))
    
    pygame.display.update()

def game_loop(window,dicionario):
    while recebe_eventos():
        desenha(window,dicionario)
    
w,d= inicializa()
game_loop(w,d)
# tela_jogo.game_loop(w,d) #IMPORTANTE PARA TROCAR DE TELAS


    

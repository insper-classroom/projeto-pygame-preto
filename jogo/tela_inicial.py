import pygame
import tela_jogo

window = None
vaijogo = False

def inicializa():
    #janela
    global window

    pygame.init()
    window = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('JOGO DA COBRINHA')

    dicionario = {}
    #INSTRUCOES FONTE
    dicionario['fonte'] = pygame.font.Font('fonte/retro_computer_personal_use.ttf',15)

    #desenho da cobra
    dicionario['cobra'] = pygame.image.load('imagens/cobra_logo.png')
    dicionario['cobra'] = pygame.transform.scale(dicionario['cobra'],(300,300))

    #imagem bem vindos
    dicionario['bem vindo'] = pygame.image.load('imagens/bem vindos.png')

    #IMAGEM START
    dicionario['start'] = pygame.image.load('imagens/botao_start-16.png.png')
    

    return window,dicionario
    
   

def recebe_eventos():
    global vaijogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key  == pygame.K_RETURN:
                vaijogo = True
        if event.type == pygame.KEYDOWN:        
            if event.key == pygame.K_y:
                vaijogo = True
                


    return True


def desenha(window,dicionario):
    window.fill((0,149,0))
#DESENHAR A COBRA
    window.blit(dicionario['cobra'],(420,220))
    window.blit(dicionario['bem vindo'],(360,0))
#DESENHAR AS INSTRUÇOES
    texto = dicionario['fonte'].render('Clique ENTER para iniciar',False,(0,0,0))
    window.blit(texto,(430, 590))
#DESENHAR O START
    window.blit(dicionario['start'],(490,590))
    
    pygame.display.update()

def game_loop_inicial(window,dicionario):
    while recebe_eventos():
        if vaijogo:
            tela_jogo.rodar_jogo(window,dicionario)#IMPORTANTE PARA TROCAR DE TELAS
        else:
            desenha(window,dicionario)


    
w,d= inicializa()
game_loop_inicial(w,d)



    

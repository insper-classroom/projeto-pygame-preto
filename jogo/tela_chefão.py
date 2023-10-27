import pygame
from random import randint

def inicializa():
    pygame.init()
    widht = 1200
    height = 800

    window = pygame.display.set_mode((widht,height))
    pygame.display.set_caption('JOGO DA COBRINHA')

    estado={
        'pos_cobra': [(widht/2),(height/2)],
        'pos_parede' : [[0,0]],
        'pos_rabo' : [(widht/2)+12,(height/2) - 59]
        }
    #posicao aleatoria do coelho
    lista= []
    for i in range(3):
        x = randint(0,1150)
        y = randint(0,750)
        dici = {'x': x,'y':y}
        lista.append(dici)

    #posicao aleatoria da maçã
    l = []
    for i in range(1):
        x = randint(0,1150)
        y = randint(0,750)
        d = {'x': x,'y':y}
        l.append(d)
    
    #parede
    for y1 in range(0,height,50):
        pos = [0,y1]
        estado['pos_parede'].append(pos)
    
    for x1 in range(0,widht,40):
        pos = [x1,0]
        estado['pos_parede'].append(pos)

    for y2 in range(0,height,50):
        pos = [(1200-50),y2]
        estado['pos_parede'].append(pos)
    
    for x2 in range(0,widht,40):
        pos = [x2,(800-50)]
        estado['pos_parede'].append(pos)

    dicionario = {}

    dicionario['coelho_bom'] = lista
    dicionario['maca_vermelha'] = l

    dicionario['parede'] = pygame.image.load('imagens/parede2.png')

    dicionario['img_cobra'] = pygame.image.load('imagens/cobra_cabeca.png')
    dicionario['cobra'] = pygame.transform.scale(dicionario['img_cobra'],(50,50))

    dicionario['img_cobra_rabo'] = pygame.image.load('imagens/cobra_rabo.png')
    dicionario['cobra_rabo'] = pygame.transform.scale(dicionario['img_cobra_rabo'],(30,60))

    dicionario['img_coelho'] = pygame.image.load('imagens/coelho.png')
    dicionario['coelho'] = pygame.transform.scale(dicionario['img_coelho'],(40,50))

    dicionario['img_maca'] = pygame.image.load('imagens/maca.png')
    dicionario['maca'] = pygame.transform.scale(dicionario['img_maca'],(30,40))

    dicionario['img_cobra_corpo'] = pygame.image.load('imagens/cobra_corpo.png')
    dicionario['cobra_corpo'] = pygame.transform.scale(dicionario['img_cobra_corpo'],(30,60))

    return window,dicionario,estado 

def recebe_eventos(estado,dicionario,window):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        if event.type == pygame.KEYDOWN :
            ultima_tecla = event.key

            if event.key == pygame.K_RIGHT:
                estado['pos_cobra'][0] += 50
                estado['pos_rabo'][0] += 50

            elif event.key == pygame.K_LEFT:
                estado['pos_cobra'][0] -= 50
                estado['pos_rabo'][0] -= 50
                
            elif event.key == pygame.K_DOWN:
                estado['pos_cobra'][1] += 50
                estado['pos_rabo'][1] += 50
            
            elif event.key == pygame.K_UP:
                estado['pos_cobra'][1] -= 50
                estado['pos_rabo'][1] -= 50
    
        #colisão da cobra c/ parede
        retan_cobra = pygame.Rect((estado['pos_cobra'][0],estado['pos_cobra'][1]),(50,50))
        # retan_rabo = pygame.Rect((estado['pos_cobra'][0],estado['pos_cobra'][1]),(30,60))
        retan_parede = []

        for p in estado['pos_parede']:
            retangulo = pygame.Rect((p[0],p[1]),(50,50))
            retan_parede.append(retangulo)

        
        for retangulo in retan_parede:
            if retan_cobra.colliderect(retangulo):

                if ultima_tecla == pygame.K_RIGHT:
                    estado['pos_cobra'][0] -= 50
                    estado['pos_rabo'][0] -= 50

                elif ultima_tecla == pygame.K_LEFT:
                    estado['pos_cobra'][0] += 50
                    estado['pos_rabo'][0] += 50
                    
                elif ultima_tecla == pygame.K_DOWN:
                    estado['pos_cobra'][1] -= 25
                    estado['pos_rabo'][1] -= 25
                
                elif  ultima_tecla== pygame.K_UP:
                    estado['pos_rabo'][1] += 25
                    estado['pos_cobra'][1] += 25

        #colisao da cobra com a maçã
        retan_cobra = retan_cobra = pygame.Rect((estado['pos_cobra'][0],estado['pos_cobra'][1]),(50,50))
        retan_maca = []

        for mv in dicionario['maca_vermelha']:
            retangulo1 = pygame.Rect((mv['x'],mv['y']),(30,40))
            retan_maca.append(retangulo1)
        
        for retangulo1 in retan_maca:
            if retan_cobra.colliderect(retangulo1):
                if ultima_tecla == pygame.K_RIGHT:
                    estado['pos_cobra'][0] -= 50
                    estado['pos_rabo'][0] -= 50
                    dicionario['maca_vermelha'].remove({'x':retangulo1.x,'y':retangulo1.y})
                    # window.blit(dicionario['cobra_corpo'])

                elif ultima_tecla == pygame.K_LEFT:
                    estado['pos_cobra'][0] += 50
                    estado['pos_rabo'][0] += 50
                    dicionario['maca_vermelha'].remove({'x':retangulo1.x,'y':retangulo1.y})
                    
                elif ultima_tecla == pygame.K_DOWN:
                    estado['pos_cobra'][1] -= 25
                    estado['pos_rabo'][1] -= 25
                    dicionario['maca_vermelha'].remove({'x':retangulo1.x,'y':retangulo1.y})
                
                elif  ultima_tecla== pygame.K_UP:
                    estado['pos_cobra'][1] += 25
                    estado['pos_rabo'][1] += 25
                    dicionario['maca_vermelha'].remove({'x':retangulo1.x,'y':retangulo1.y})

    return True

def desenha(window,dicionario,estado):

    window.fill((0,149,0))

    window.blit(dicionario['cobra'],(estado['pos_cobra'][0],estado['pos_cobra'][1]))
    window.blit(dicionario['cobra_rabo'],(estado['pos_rabo'][0],estado['pos_rabo'][1]))

    for parede in estado['pos_parede']:
        window.blit(dicionario['parede'],parede)

    for coelho in dicionario['coelho_bom']:
        window.blit(dicionario['coelho'],(coelho['x'],coelho['y']))

    for maca in dicionario['maca_vermelha']:
        window.blit(dicionario['maca'],(maca['x'],maca['y']))

    pygame.display.update()

def game_loop(window,dicionario,estado):
    while recebe_eventos(estado,dicionario,window):
        desenha(window,dicionario,estado)
    
w,d,e= inicializa()
game_loop(w,d,e)

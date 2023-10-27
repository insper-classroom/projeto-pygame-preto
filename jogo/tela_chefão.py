import pygame

def inicializa():
    pygame.init()
    widht = 900
    height = 800

    window = pygame.display.set_mode((widht,height))
    pygame.display.set_caption('JOGO DA COBRINHA')

    estado={
        'pos_cobra': [(widht/2),(height/2)],
        'pos_parede' : [[0,0]],
        'pos_rabo' : [(widht/2),(height/2) - 15]
        }
    
    for y1 in range(0,height,13):
        pos = [0,y1]
        estado['pos_parede'].append(pos)
    
    for x1 in range(0,widht,10):
        pos = [x1,0]
        estado['pos_parede'].append(pos)

    for y2 in range(0,height,13):
        pos = [(900-10),y2]
        estado['pos_parede'].append(pos)
    
    for x2 in range(0,widht,10):
        pos = [x2,(800-13)]
        estado['pos_parede'].append(pos)

    dicionario = {}
    dicionario['img_parede'] = pygame.image.load('imagens/parede.png')
    dicionario['parede'] = pygame.transform.scale(dicionario['img_parede'],(10,13))

    dicionario['cobra'] = pygame.image.load('imagens/cobra_cabeca.png')
    dicionario['cobra_rabo'] = pygame.image.load('imagens/cobra_rabo.png')

    return window,dicionario,estado 

def recebe_eventos(estado,dicionario):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT:
                estado['pos_cobra'][0] += 50

            elif event.key == pygame.K_LEFT:
                estado['pos_cobra'][0] -= 50
                
            elif event.key == pygame.K_DOWN:
                estado['pos_cobra'][1] += 50
            
            elif event.key == pygame.K_UP:
                estado['pos_cobra'][1] -= 50
    
        #colisão da cobra c/ parede
        # retan_cobra = pygame.Rect((estado['pos_cobra'][0],estado['pos_cobra'][1],50,50))
        # retan_parede = []

        # for p in dicionario['parede']:
        #     retangulo = pygame.Rect((p['x'],p['y']),(dicionario['pos_parede'][0],dicionario['pos_parede'][1]),(10,13))
        #     retan_parede.append(retangulo)
        
        # for retangulo in retan_parede:
        #     if retan_cobra.colliderect(retangulo):
        #         dicionario['pos_cobra'] -=1
    return True

def desenha(window,dicionario,estado):

    window.fill((0,149,0))

    window.blit(dicionario['cobra'],(estado['pos_cobra'][0],estado['pos_cobra'][1]))
    window.blit(dicionario['cobra_rabo'],(estado['pos_cobra'][0],estado['pos_cobra'][1]))
    
    for parede in estado['pos_parede']:
        window.blit(dicionario['parede'],parede)

    pygame.display.update()

def game_loop(window,dicionario,estado):
    while recebe_eventos(estado,dicionario):
        desenha(window,dicionario,estado)
    
w,d,e= inicializa()
game_loop(w,d,e)

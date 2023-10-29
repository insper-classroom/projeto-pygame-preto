import pygame
from random import randint

VELOCIDADE_X = 1
VELOCIDADE_Y = 0.75
TILE_FRAME = 50

def inicializa():
    pygame.init()
    widht = 1200
    height = 800
    QUANT_COELHOS = 3

    window = pygame.display.set_mode((widht,height))
    pygame.display.set_caption('JOGO DA COBRINHA')

    estado = {
        'pos_cobra': [(widht/2),(height/2)],
        'pos_rabo' : [(widht/2) + 12,(height/2) - 59],
        'velocidade' : [0, VELOCIDADE_Y],
        'pontuacao' : 0,
        'xp' : 0
        }
    #posicao aleatoria do coelho
    pos_coelho = []
    for _ in range(QUANT_COELHOS):
        x = randint(100,1100)
        y = randint(100,700)
        pos= {'x':x ,'y':y}
        # pos_coelho = pygame.Rect((x, y), (40, 50))
        pos_coelho.append(pos)

    #posicao aleatoria da maçã
    x = randint(100,1100)
    y = randint(100,700)
    pos_maca = pygame.Rect((x, y), (30, 40))

    #posicao aleatoria da maca especial
    x = randint(100,1100)
    y = randint(100,700)
    pos_maca_especial = pygame.Rect((x, y), (30, 40))
            
    #parede    
    parede = pygame.Rect((0,0), (TILE_FRAME, TILE_FRAME))
    estado['pos_parede'] = [parede]
    
    for y1 in range(0,height,TILE_FRAME):
        parede = pygame.Rect((0, y1), (TILE_FRAME, TILE_FRAME))
        estado['pos_parede'].append(parede)
    
    for x1 in range(0,widht,TILE_FRAME):
        parede = pygame.Rect((x1, 0), (TILE_FRAME, TILE_FRAME))
        estado['pos_parede'].append(parede)

    for y2 in range(0,height,TILE_FRAME):
        parede = pygame.Rect((widht-50, y2), (TILE_FRAME,TILE_FRAME))
        estado['pos_parede'].append(parede)
    
    for x2 in range(0,widht,TILE_FRAME):
        parede = pygame.Rect((x2, height-TILE_FRAME), (TILE_FRAME, TILE_FRAME))
        estado['pos_parede'].append(parede)

    dicionario = {}

    dicionario['fonte'] = pygame.font.Font('fonte/perfect_dos_vga_437/Perfect DOS VGA 437 Win.ttf',20)

    dicionario['pos_coelho'] = pos_coelho
    dicionario['pos_maca'] = pos_maca
    dicionario['pos_maca_especial'] = pos_maca_especial

    dicionario['parede'] = pygame.image.load('imagens/parede2.png')

    dicionario['img_cobra'] = pygame.image.load('imagens/cobra_cabeca.png')
    dicionario['cobra'] = pygame.transform.scale(dicionario['img_cobra'],(50,50))

    dicionario['img_cobra_rabo'] = pygame.image.load('imagens/cobra_rabo.png')
    dicionario['cobra_rabo'] = pygame.transform.scale(dicionario['img_cobra_rabo'],(30,60))

    dicionario['img_coelho'] = pygame.image.load('imagens/coelho.png')
    dicionario['coelho_bom'] = pygame.transform.scale(dicionario['img_coelho'],(40,50))

    dicionario['img_coelho_mal'] = pygame.image.load('imagens/coelho_malvado.png')
    dicionario['coelho_mal'] = pygame.transform.scale(dicionario['img_coelho_mal'],(40,50))

    dicionario['img_maca'] = pygame.image.load('imagens/maca.png')
    dicionario['maca'] = pygame.transform.scale(dicionario['img_maca'],(30,40))

    dicionario['img_maca_especial'] = pygame.image.load('imagens/maca_especial.png')
    dicionario['maca_especial'] = pygame.transform.scale(dicionario['img_maca_especial'],(30,40))

    dicionario['img_cobra_corpo'] = pygame.image.load('imagens/cobra_corpo.png')
    dicionario['cobra_corpo'] = pygame.transform.scale(dicionario['img_cobra_corpo'],(30,60))

    dicionario['int'] = 'sons/8bit-music-for-game-68698.mp3'
    pygame.mixer.music.load(dicionario['int'])
    pygame.mixer.music.play()

    dicionario['game_over'] = pygame.mixer.Sound('sons/game-over-arcade-6435.mp3')

    dicionario['comida'] = pygame.mixer.Sound('sons/eating-sound-effect-36186.mp3')

    return window,dicionario,estado 

def recebe_eventos(estado,dicionario,window):
    # movimentação da cobra
    estado['pos_cobra'][0] += estado['velocidade'][0]
    estado['pos_cobra'][1] += estado['velocidade'][1]
    estado['pos_rabo'][0] += estado['velocidade'][0]
    estado['pos_rabo'][1] += estado['velocidade'][1]
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT:
                estado['velocidade'][0] = VELOCIDADE_X
                estado['velocidade'][1] = 0

            elif event.key == pygame.K_LEFT:
                estado['velocidade'][0] = -VELOCIDADE_X
                estado['velocidade'][1] = 0
                
            elif event.key == pygame.K_DOWN:
                estado['velocidade'][0] = 0
                estado['velocidade'][1] = VELOCIDADE_Y
            
            elif event.key == pygame.K_UP:
                estado['velocidade'][0] = 0
                estado['velocidade'][1] = - VELOCIDADE_Y
    
    #colisão da cobra c/ parede
    retan_cobra = pygame.Rect((estado['pos_cobra'][0],estado['pos_cobra'][1]),(TILE_FRAME,TILE_FRAME))  
    for parede in estado['pos_parede']:
        if retan_cobra.colliderect(parede):
            print("Colidiu")
            dicionario['game_over'].play()
            return False
        
    #colisao da cobra com a maçã
    retan_maca = pygame.Rect((dicionario['pos_maca'][0], dicionario['pos_maca'][1]),(30,40))

    if retan_cobra.colliderect(retan_maca):
        dicionario['comida'].play()
        estado["pontuacao"] += 1
        x = randint(100,1100)
        y = randint(100,700)
        nova_maca = pygame.Rect((x, y), (30, 40))
        dicionario['pos_maca'] = nova_maca

    #colisao da cobra com a maçã especial
    retan_maca_especial = pygame.Rect((dicionario['pos_maca_especial'][0], dicionario['pos_maca_especial'][1]),(30,40))

    if retan_cobra.colliderect(retan_maca_especial):
        dicionario['comida'].play()
        estado['xp'] += 5
        x = randint(50,500)
        y = randint(50,100)
        nova_maca_especial = pygame.Rect((x, y), (30, 40))
        dicionario['pos_maca_especial'] = nova_maca_especial
    
    #colisao da cobra com o coelho
    # for coelho in dicionario['pos_coelho']:
    #     if retan_cobra.collidedict(coelho):
    #         print("colidiu")
    #         return False

    return True

def desenha(window,dicionario,estado):
    window.fill((0,149,0))

    window.blit(dicionario['cobra'],(estado['pos_cobra'][0],estado['pos_cobra'][1]))
    window.blit(dicionario['cobra_rabo'],(estado['pos_rabo'][0],estado['pos_rabo'][1]))

    for parede in estado['pos_parede']:
        window.blit(dicionario['parede'],parede)

    for coelho in dicionario['pos_coelho']:
        window.blit(dicionario['coelho_bom'],(coelho['x'],coelho['y']))

    window.blit(dicionario['maca'],(dicionario['pos_maca'][0],dicionario['pos_maca'][1]))

    window.blit(dicionario['maca_especial'],(dicionario['pos_maca_especial'][0],dicionario['pos_maca_especial'][1]))

    texto = dicionario['fonte'].render(f'POINTS: {estado["pontuacao"]}',False,(0,0,0))
    window.blit(texto,(10,10))

    texto = dicionario['fonte'].render(f'XP: {estado["xp"]}',False,(0,0,0))
    window.blit(texto,(10,30))
    pygame.display.update()

def game_loop(window,dicionario,estado):
    while recebe_eventos(estado,dicionario,window):
        desenha(window,dicionario,estado)
    
w,d,e = inicializa()
game_loop(w,d,e)

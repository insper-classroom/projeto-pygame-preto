import pygame
import tela_final
from random import randint

VELOCIDADE_X = 50
VELOCIDADE_Y = 50
TILE_FRAME = 50

def inicializa():
    pygame.init()
    widht = 1200
    height = 800
    QUANT_COELHOS = 3

    window = pygame.display.set_mode((widht,height))
    pygame.display.set_caption('RETRO SNAKE')

    clock = pygame.time.Clock()

    estado = {
        'pos_cobra': [(widht/2),(height/2)],
        'pos_rabo' : [(widht/2) + 12,(height/2) - 59],
        'velocidade' : [50,50],
        'pontuacao' : 0,
        'xp' : 0,
        'direcao': 'baixo',
        'corpo': 1,
        'cobra' : [{
            'pos' : [(widht/2),(height/2)],
            'imag' : '',
            'cabeca': True,
        }],
        'clock' : clock,
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

    #fontes
    dicionario['fonte'] = pygame.font.Font('fonte/perfect_dos_vga_437/Perfect DOS VGA 437 Win.ttf',20)

    #posicao
    dicionario['pos_coelho'] = pos_coelho
    dicionario['pos_maca'] = pos_maca
    dicionario['pos_maca_especial'] = pos_maca_especial

    #imagem da parede
    dicionario['parede'] = pygame.image.load('imagens/parede2.png')

    #imagens da cobra
    dicionario['img_cobra'] = pygame.image.load('imagens/cobra_cabeca.png')
    dicionario['cobra'] = pygame.transform.scale(dicionario['img_cobra'],(50,50))

    dicionario['cobra_direita']= pygame.transform.rotate(dicionario['cobra'],90)
    dicionario['cobra_cima']= pygame.transform.rotate(dicionario['cobra'],180)
    dicionario['cobra_esquerda']= pygame.transform.rotate(dicionario['cobra'],270)
    dicionario['cobra_baixo'] = dicionario['cobra']
    estado['cobra'][0]['imag'] = dicionario['cobra'] 

    dicionario['img_cobra_rabo'] = pygame.image.load('imagens/cobra_rabo.png')
    dicionario['cobra_rabo'] = pygame.transform.scale(dicionario['img_cobra_rabo'],(50,50))
    dicionario['cobra_rabo_direita'] = pygame.transform.rotate(dicionario['cobra_rabo'],90)
    dicionario['cobra_rabo_cima'] = pygame.transform.rotate(dicionario['cobra_rabo'],180)
    dicionario['cobra_rabo_esquerda'] = pygame.transform.rotate(dicionario['cobra_rabo'],270)
    dicionario['cobra_rabo_baixo'] = dicionario['cobra_rabo']
    
    dicionario['img_cobra_corpo'] = pygame.image.load('imagens/cobra_corpo.png')
    dicionario['cobra_corpo'] = pygame.transform.scale(dicionario['img_cobra_corpo'],(50,50))
    dicionario['cobra_corpo_direita'] = pygame.transform.rotate(dicionario['cobra_corpo'],90)
    dicionario['cobra_corpo_cima'] = pygame.transform.rotate(dicionario['cobra_corpo'],180)
    dicionario['cobra_corpo_esquerda'] = pygame.transform.rotate(dicionario['cobra_corpo'],270)
    dicionario['cobra_corpo_baixo'] = dicionario['cobra_corpo']

    dicionario['img_cobra_mov1'] = pygame.image.load('imagens/cobra_mov1.png')
    dicionario['cobra_mov1'] = pygame.transform.scale(dicionario['img_cobra_mov1'],(50,50))

    dicionario['img_cobra_mov2'] = pygame.image.load('imagens/cobra_mov2.png')
    dicionario['cobra_mov2'] = pygame.transform.scale(dicionario['img_cobra_mov2'],(50,50))

    dicionario['img_cobra_mov3'] = pygame.image.load('imagens/cobra_mov3.png')
    dicionario['cobra_mov3'] = pygame.transform.scale(dicionario['img_cobra_mov3'],(50,50))

    dicionario['img_cobra_mov4'] = pygame.image.load('imagens/cobra_mov4.png')
    dicionario['cobra_mov4'] = pygame.transform.scale(dicionario['img_cobra_mov4'],(50,50))

    #imagens dos coelhos
    dicionario['img_coelho'] = pygame.image.load('imagens/coelho.png')
    dicionario['coelho_bom'] = pygame.transform.scale(dicionario['img_coelho'],(40,50))

    dicionario['img_coelho_mal'] = pygame.image.load('imagens/coelho_malvado.png')
    dicionario['coelho_mal'] = pygame.transform.scale(dicionario['img_coelho_mal'],(40,50))

    #imagens das maçãs
    dicionario['img_maca'] = pygame.image.load('imagens/maca.png')
    dicionario['maca'] = pygame.transform.scale(dicionario['img_maca'],(30,40))

    dicionario['img_maca_especial'] = pygame.image.load('imagens/maca_especial.png')
    dicionario['maca_especial'] = pygame.transform.scale(dicionario['img_maca_especial'],(30,40))

    #sons
    dicionario['int'] = 'sons/8bit-music-for-game-68698.mp3'
    pygame.mixer.music.load(dicionario['int'])
    pygame.mixer.music.play()

    dicionario['game_over'] = pygame.mixer.Sound('sons/game-over-arcade-6435.mp3')

    dicionario['comida'] = pygame.mixer.Sound('sons/eating-sound-effect-36186.mp3')

    return window,dicionario,estado 

def recebe_eventos(estado,dicionario,window):
    # movimentação da cobra
    y = estado['cobra'][0]['pos'][1] 
    x = estado['cobra'][0]['pos'][0] 

    if estado['direcao'] == 'baixo':
        y += estado['velocidade'][1]
    if estado['direcao'] == 'cima':
        y-= estado['velocidade'][1]
    if estado['direcao'] == 'direita':
        x += estado['velocidade'][0]
    if estado['direcao'] == 'esquerda':
        x -= estado['velocidade'][0]

    pedaco ={
        'pos' : [x,y],
        'imag' : dicionario['cobra'],
    }
    

    estado['cobra'].insert(0,pedaco)
    del estado['cobra'][-1]

    if len(estado['cobra']) == 2:
        rabo = estado['cobra'][1]
        if estado['direcao'] == 'baixo':
            rabo['imag'] = dicionario['cobra_rabo_baixo']
        if estado['direcao'] == 'cima':
            rabo['imag'] = dicionario['cobra_rabo_cima']
        if estado['direcao'] == 'esquerda':
            rabo['imag'] = dicionario['cobra_rabo_esquerda']
        if estado['direcao'] == 'direita':
            rabo['imag'] = dicionario['cobra_rabo_direita']

    if len(estado['cobra']) > 2:
        cabeca = estado['cobra'][0]
        pescoco = estado['cobra'][1]
        pescoco['imag']= dicionario['cobra_corpo']
        corpo1 = estado['cobra'][2]

        if estado['direcao'] == 'baixo':
            if cabeca['pos'][1] > pescoco['pos'][1] and pescoco['pos'][1] > corpo1['pos'][1]: #cenario 1
                pescoco['imag']= dicionario['cobra_corpo']
            if cabeca['pos'][1] > pescoco['pos'][1] and pescoco['pos'][0] < corpo1['pos'][0]: # cenario 3
                pescoco['imag']= dicionario['cobra_mov1']
            if cabeca['pos'][1] > pescoco['pos'][1] and pescoco['pos'][0] > corpo1['pos'][0]: # cenario 4
                pescoco['imag']= dicionario['cobra_mov2']

        if estado['direcao'] == 'cima':
            if cabeca['pos'][1] < pescoco['pos'][1] and pescoco['pos'][1] < corpo1['pos'][1]: #cenario 2
                pescoco['imag']= dicionario['cobra_corpo']
            if cabeca['pos'][1] < pescoco['pos'][1] and pescoco['pos'][0] > corpo1['pos'][0]: 
                pescoco['imag']= dicionario['cobra_mov4']
            if cabeca['pos'][1] < pescoco['pos'][1] and pescoco['pos'][0] < corpo1['pos'][0]: 
                pescoco['imag']= dicionario['cobra_mov3']

        if estado['direcao'] == 'esquerda':
            if cabeca['pos'][0] < pescoco['pos'][0] and pescoco['pos'][0] < corpo1['pos'][0]:
                pescoco['imag']= dicionario['cobra_corpo_esquerda']
            if cabeca['pos'][0] < pescoco['pos'][0] and pescoco['pos'][1] > corpo1['pos'][1]: # cenario 3
                pescoco['imag']= dicionario['cobra_mov1']
            if cabeca['pos'][0] < pescoco['pos'][0] and pescoco['pos'][1] < corpo1['pos'][1]: # cenario 4
                pescoco['imag']= dicionario['cobra_mov2']

        if estado['direcao'] == 'direita':
            if cabeca['pos'][0] > pescoco['pos'][0] and pescoco['pos'][0] > corpo1['pos'][0]:
                pescoco['imag']= dicionario['cobra_corpo_direita']
            if cabeca['pos'][0] > pescoco['pos'][0] and pescoco['pos'][1] < corpo1['pos'][1]: 
                pescoco['imag']= dicionario['cobra_mov4']
            if cabeca['pos'][0] > pescoco['pos'][0] and pescoco['pos'][1] > corpo1['pos'][1]: 
                pescoco['imag']= dicionario['cobra_mov3']
            

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT:
                if estado['direcao'] != 'esquerda': 
                    dicionario['cobra'] = dicionario['cobra_direita']
                    estado['direcao'] = 'direita'

            elif event.key == pygame.K_LEFT:
                if estado['direcao'] != 'direita':
                    dicionario['cobra'] = dicionario['cobra_esquerda']
                    estado['direcao'] = 'esquerda'
                
            elif event.key == pygame.K_DOWN:
                if estado['direcao'] != 'cima':
                    dicionario['cobra'] = dicionario['cobra_baixo']
                    estado['direcao'] = 'baixo'
            
            elif event.key == pygame.K_UP:
                if estado['direcao'] != 'baixo':
                    dicionario['cobra'] = dicionario['cobra_cima']
                    estado['direcao'] = 'cima'

    #colisão da cobra c/ parede
    cabeca = estado['cobra'][0]
    retan_cobra = pygame.Rect((cabeca['pos'][0],cabeca['pos'][1]),(TILE_FRAME,TILE_FRAME))  
    for parede in estado['pos_parede']:
        if retan_cobra.colliderect(parede):
            dicionario['game_over'].play()
            return False
        
    #colisao da cobra com a maçã
    retan_maca = pygame.Rect((dicionario['pos_maca'][0], dicionario['pos_maca'][1]),(30,40))

    if retan_cobra.colliderect(retan_maca):
        y = estado['cobra'][0]['pos'][1] 
        x = estado['cobra'][0]['pos'][0] 

        if estado['direcao'] == 'baixo':
            y += estado['velocidade'][1]
        if estado['direcao'] == 'cima':
            y-= estado['velocidade'][1]
        if estado['direcao'] == 'direita':
            x += estado['velocidade'][0]
        if estado['direcao'] == 'esquerda':
            x -= estado['velocidade'][0]

        nova_cabeca={
            'pos' : [x,y],
            'imag' : dicionario['cobra']
        }

        estado['cobra'].insert(0,nova_cabeca)

        estado['cobra'][1]['imag'] = dicionario['cobra_corpo']

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
    # retan_coelho = pygame.Rect((dicionario['pos_coelho'][0], dicionario['pos_coelho'][1]),(40,50))
    # if retan_cobra.collidedict(retan_coelho):
    #         dicionario['coelho_bom'] = dicionario['coelho_mal']

    return True

def desenha(window,dicionario,estado):
    window.fill((0,149,0))

    for cobra in estado['cobra']:
        window.blit(cobra['imag'],(cobra['pos'][0], cobra['pos'][1]))

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
        estado['clock'].tick(4)
        desenha(window,dicionario,estado)
    
w,d,e = inicializa()
game_loop(w,d,e)

w,d = tela_final.inicializa()
fecha_jogo = tela_final.game_loop(w,d)

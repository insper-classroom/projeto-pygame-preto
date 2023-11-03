import pygame
import tela_final
from random import randint

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
        'cobra' : [{
            'pos' : [(widht/2),(height/2)],
            'imag' : '',
            'cabeca': True,
        }],
        'clock' : clock,
        'status': True
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
    img_cabeca = pygame.image.load('imagens/cobra_cabeca.png')
    dicionario['img_cabeca'] = pygame.transform.scale(img_cabeca,(50,50))

    dicionario['cobra_direita']= pygame.transform.rotate(dicionario['img_cabeca'],90)
    dicionario['cobra_cima']= pygame.transform.rotate(dicionario['img_cabeca'],180)
    dicionario['cobra_esquerda']= pygame.transform.rotate(dicionario['img_cabeca'],270)
    dicionario['cobra_baixo'] = dicionario['img_cabeca']
    estado['cobra'][0]['imag'] = dicionario['img_cabeca'] 

    img_cobra_rabo = pygame.transform.scale(pygame.image.load('imagens/cobra_rabo.png'),(50,50))
    dicionario['cobra_rabo_direita'] = pygame.transform.rotate(img_cobra_rabo,90)
    dicionario['cobra_rabo_cima'] = pygame.transform.rotate(img_cobra_rabo,180)
    dicionario['cobra_rabo_esquerda'] = pygame.transform.rotate(img_cobra_rabo,270)
    dicionario['cobra_rabo_baixo'] = img_cobra_rabo
    
    dicionario['img_cobra_corpo'] = pygame.image.load('imagens/cobra_corpo.png')
    dicionario['cobra_corpo'] = pygame.transform.scale(dicionario['img_cobra_corpo'],(50,50))
    dicionario['cobra_corpo_horizontal'] = pygame.transform.rotate(dicionario['cobra_corpo'],90)
    dicionario['cobra_corpo_vertical'] = dicionario['cobra_corpo']

    img_cobra_quina = pygame.transform.scale(pygame.image.load('imagens/cobra_mov1.png'), (50,50))
    dicionario['cobra_quina_direita_baixo'] = img_cobra_quina
    dicionario['cobra_quina_esquerda_baixo'] = pygame.transform.rotate(img_cobra_quina, -90)
    dicionario['cobra_quina_esquerda_cima'] = pygame.transform.rotate(img_cobra_quina, -180)
    dicionario['cobra_quina_direita_cima'] = pygame.transform.rotate(img_cobra_quina, -270)
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

def movimenta(estado, x, y):
    if estado['direcao'] == 'baixo':
        y += estado['velocidade'][1]
    if estado['direcao'] == 'cima':
        y-= estado['velocidade'][1]
    if estado['direcao'] == 'direita':
        x += estado['velocidade'][0]
    if estado['direcao'] == 'esquerda':
        x -= estado['velocidade'][0]
    
    return estado, x, y

def muda_movimento(estado, dicionario):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT:
                if estado['direcao'] != 'esquerda': 
                    dicionario['img_cabeca'] = dicionario['cobra_direita']
                    estado['direcao'] = 'direita'

            elif event.key == pygame.K_LEFT:
                if estado['direcao'] != 'direita':
                    dicionario['img_cabeca'] = dicionario['cobra_esquerda']
                    estado['direcao'] = 'esquerda'
                
            elif event.key == pygame.K_DOWN:
                if estado['direcao'] != 'cima':
                    dicionario['img_cabeca'] = dicionario['cobra_baixo']
                    estado['direcao'] = 'baixo'
            
            elif event.key == pygame.K_UP:
                if estado['direcao'] != 'baixo':
                    dicionario['img_cabeca'] = dicionario['cobra_cima']
                    estado['direcao'] = 'cima'
    return estado, dicionario

def atualiza_cobra(estado, dicionario, x, y):
    pedaco = {
        'pos' : [x,y],
        'imag' : dicionario['img_cabeca'],
    }
    
    estado['cobra'].insert(0, pedaco)
    del estado['cobra'][-1]

    if len(estado['cobra']) == 2:
        rabo = estado['cobra'][-1]
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
        rabo = estado['cobra'][-1]
        corpo1 = estado['cobra'][2]
                    
        if estado['direcao'] == 'baixo':
            # acompanha onde tá indo
            rabo['imag'] = dicionario['cobra_rabo_baixo']
            if cabeca['pos'][1] > pescoco['pos'][1] and pescoco['pos'][1] > corpo1['pos'][1]:
                pescoco['imag']= dicionario['cobra_corpo_vertical']
            # estava vindo da direita
            if cabeca['pos'][1] > pescoco['pos'][1] and pescoco['pos'][0] < corpo1['pos'][0]:
                pescoco['imag']= dicionario['cobra_quina_direita_baixo']
            # estava vindo da esquerda
            if cabeca['pos'][1] > pescoco['pos'][1] and pescoco['pos'][0] > corpo1['pos'][0]: 
                pescoco['imag']= dicionario['cobra_quina_esquerda_baixo']

        if estado['direcao'] == 'cima':
            # acompanha onde tá indo
            rabo['imag'] = dicionario['cobra_rabo_cima']
            if cabeca['pos'][1] < pescoco['pos'][1] and pescoco['pos'][1] < corpo1['pos'][1]: #cenario 2
                pescoco['imag']= dicionario['cobra_corpo_vertical']
            # 
            if cabeca['pos'][1] < pescoco['pos'][1] and pescoco['pos'][0] > corpo1['pos'][0]: 
                pescoco['imag']= dicionario['cobra_quina_esquerda_cima']
            if cabeca['pos'][1] < pescoco['pos'][1] and pescoco['pos'][0] < corpo1['pos'][0]: 
                pescoco['imag']= dicionario['cobra_quina_direita_cima']

        if estado['direcao'] == 'esquerda':
            rabo['imag'] = dicionario['cobra_rabo_esquerda']
            
            if cabeca['pos'][0] < pescoco['pos'][0] and pescoco['pos'][0] < corpo1['pos'][0]:
                pescoco['imag'] = dicionario['cobra_corpo_horizontal']
            if cabeca['pos'][0] < pescoco['pos'][0] and pescoco['pos'][1] > corpo1['pos'][1]: # cenario 3
                pescoco['imag'] = dicionario['cobra_quina_esquerda_cima']
            if cabeca['pos'][0] < pescoco['pos'][0] and pescoco['pos'][1] < corpo1['pos'][1]: # cenario 4
                pescoco['imag'] = dicionario['cobra_quina_esquerda_baixo']

        if estado['direcao'] == 'direita':
            rabo['imag'] = dicionario['cobra_rabo_direita']
            
            if cabeca['pos'][0] > pescoco['pos'][0] and pescoco['pos'][0] > corpo1['pos'][0]:
                pescoco['imag']= dicionario['cobra_corpo_horizontal']
            if cabeca['pos'][0] > pescoco['pos'][0] and pescoco['pos'][1] < corpo1['pos'][1]: 
                pescoco['imag']= dicionario['cobra_quina_direita_baixo']
            if cabeca['pos'][0] > pescoco['pos'][0] and pescoco['pos'][1] > corpo1['pos'][1]: 
                pescoco['imag']= dicionario['cobra_quina_direita_cima']
    return estado, dicionario

def colisao_parede(estado, dicionario, retan_cobra):
    for parede in estado['pos_parede']:
        if retan_cobra.colliderect(parede):
            dicionario['game_over'].play()
            estado['status'] = False
    return estado, dicionario

def colisao_maca(estado, dicionario, retan_cobra):
    retan_maca = pygame.Rect((dicionario['pos_maca'][0], dicionario['pos_maca'][1]),(30,40))
    if retan_cobra.colliderect(retan_maca):
        y = estado['cobra'][0]['pos'][1] 
        x = estado['cobra'][0]['pos'][0] 
        estado, x, y = movimenta(estado, x, y)  

        nova_cabeca = {
            'pos' : [x,y],
            'imag' : dicionario['img_cabeca']
        }

        estado['cobra'].insert(0,nova_cabeca)

        estado['cobra'][1]['imag'] = dicionario['cobra_corpo']

        dicionario['comida'].play()
        estado["pontuacao"] += 1
        x = randint(100,1100)
        y = randint(100,700)
        nova_maca = pygame.Rect((x, y), (30, 40))
        dicionario['pos_maca'] = nova_maca
    return estado, dicionario
        
def colisao_maca_especial(estado, dicionario, retan_cobra):
    retan_maca_especial = pygame.Rect((dicionario['pos_maca_especial'][0], dicionario['pos_maca_especial'][1]),(30,40))
    if retan_cobra.colliderect(retan_maca_especial):
        dicionario['comida'].play()
        estado['xp'] += 5
        x = randint(50,500)
        y = randint(50,100)
        nova_maca_especial = pygame.Rect((x, y), (30, 40))
        dicionario['pos_maca_especial'] = nova_maca_especial
    return estado, dicionario
    

def recebe_eventos(estado,dicionario,window):
    y = estado['cobra'][0]['pos'][1] 
    x = estado['cobra'][0]['pos'][0] 
    # movimentação da cobra
    estado, x, y = movimenta(estado, x, y)

    estado, dicionario = atualiza_cobra(estado, dicionario, x, y)
            
    estado, dicionario = muda_movimento(estado, dicionario)

    cabeca = estado['cobra'][0]
    retan_cobra = pygame.Rect((cabeca['pos'][0],cabeca['pos'][1]),(TILE_FRAME,TILE_FRAME))  

    #colisão da cobra c/ parede
    estado, dicionario = colisao_parede(estado, dicionario, retan_cobra)
        
    #colisao da cobra com a maçã
    estado, dicionario = colisao_maca(estado, dicionario, retan_cobra)

    #colisao da cobra com a maçã especial
    estado, dicionario = colisao_maca_especial(estado, dicionario, retan_cobra)
    
    #colisao da cobra com o coelho
    # retan_coelho = pygame.Rect((dicionario['pos_coelho'][0], dicionario['pos_coelho'][1]),(40,50))
    # if retan_cobra.collidedict(retan_coelho):
    #         dicionario['coelho_bom'] = dicionario['coelho_mal']

    return estado['status']

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
    # jogo começa
    while recebe_eventos(estado,dicionario,window):
        estado['clock'].tick(5)
        desenha(window,dicionario,estado)
    
    # jogo acaba e troca pra tela final
    w,d = tela_final.inicializa()
    while (tela_final.game_loop(w,d)):
        pass
    # jogo recomeça
    w,d,e = inicializa()
    game_loop(w,d,e)

#inicializa o jogo
w,d,e = inicializa()
game_loop(w,d,e)
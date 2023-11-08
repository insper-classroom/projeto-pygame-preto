import pygame
from random import randint
from tela_chefão import *

TILE_FRAME = 50

def game_over(estado, dicionario):
    dicionario['game_over'].play()
    estado['status'] = False
    return estado, dicionario

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
            
            elif event.key == pygame.K_w:
                if estado['direcao'] != 'baixo':
                    dicionario['img_cabeca'] = dicionario['cobra_cima']
                    estado['direcao'] = 'cima'

            if event.key == pygame.K_d:
                if estado['direcao'] != 'esquerda': 
                    dicionario['img_cabeca'] = dicionario['cobra_direita']
                    estado['direcao'] = 'direita'

            elif event.key == pygame.K_a:
                if estado['direcao'] != 'direita':
                    dicionario['img_cabeca'] = dicionario['cobra_esquerda']
                    estado['direcao'] = 'esquerda'
                
            elif event.key == pygame.K_s:
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
        #TENTNDO ARRUMAR IMAGEM DO RABINHO
        penultimo = estado['cobra'][-2]
        if penultimo['pos'][1] == rabo['pos'][1]:
            if penultimo['pos'][0] < rabo['pos'][0]:
                rabo['imag'] = dicionario['cobra_rabo_esquerda']
            if penultimo['pos'][0] > rabo['pos'][0]:
                rabo['imag'] = dicionario['cobra_rabo_direita']
        if penultimo['pos'][0] == rabo['pos'][0]:
            if penultimo['pos'][1] < rabo['pos'][1]:
                rabo['imag'] = dicionario['cobra_rabo_cima']
            if penultimo['pos'][1] > rabo['pos'][1]:
                rabo['imag'] = dicionario['cobra_rabo_baixo']
        
    return estado, dicionario

def colisao_parede(estado, dicionario, retan_cobra):
    for parede in estado['pos_parede']:
        if retan_cobra.colliderect(parede):
            estado, dicionario = game_over(estado, dicionario)
            dicionario['morte'] = "ter batido na parede"
    return estado, dicionario

def colisao_cobra(estado, dicionario, retan_cobra):
    for i, pedaco in enumerate(estado['cobra']):
        if i == 0:
            pass
        else:
            retan_pedaco = pygame.Rect((pedaco['pos'][0], pedaco['pos'][1]), (TILE_FRAME, TILE_FRAME))
            if retan_cobra.colliderect(retan_pedaco):
                estado, dicionario = game_over(estado, dicionario)
                dicionario['morte'] = "comer o próprio corpo"
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
        pescoco = estado['cobra'][1]
        pescoco['imag'] = dicionario['cobra_corpo']
        if nova_cabeca['pos'][1] == pescoco['pos'][1]:
           pescoco['imag'] = dicionario['cobra_corpo_horizontal']

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


def colisao_pedra(estado, dicionario,retan_cobra):
    for pedra in estado['lista_pedra']:
        if retan_cobra.colliderect(pedra):
            estado, dicionario = game_over(estado, dicionario)
            dicionario['morte'] = "ter batido na pedra"
    return estado, dicionario

# import pygame
# import random
# def inicializa():
#     #Janela
#     pygame.init()
#     window = pygame.display.set_mode((800,700))
#     pygame.display.set_caption('JOGO DA COBRINHA')
#     dicionario = {}
#     #Add parede em dic
#     dicionario['parede'] = pygame.image.load('imagens/parede.png')
#     dicionario['parede'] = pygame.transform.scale(dicionario['parede'],(30,770))
#     dicionario['parede1'] = pygame.image.load('imagens/parede.png')
#     dicionario['parede1'] = pygame.transform.scale(dicionario['parede1'],(900,30))
#     #Add cobra
#     tamanho_quadrado = 10
#     velocidade_cobra = 15
#     tamanho_cobra = 1
#     cobrax = 1
#     cobray = 1
#     pixels = []
#     dicionario['tamanho_quadrado'] = tamanho_quadrado
#     dicionario['tamanho_cobra'] = tamanho_cobra
#     dicionario['velocidade_cobra'] = velocidade_cobra
#     dicionario['cobrax'] = cobrax
#     dicionario['cobray'] = cobray
#     dicionario['pixels'] = pixels
#     #COBRINHA ANDANDO
#     dicionario['velocidadex'] = 0 
#     dicionario['velocidadex'] = 0 
#     #Relogio
#     relogio = pygame.time.Clock()
#     dicionario['relogio'] = relogio
    
#     return window,dicionario

#     #COMIDA
# def gerar_comida(dicionario):
#     comidax = round(random.randrange(0, 750-10)/10.0)*10.0
#     comiday = round(random.randrange(0, 650-10)/10.0)*10.0
#     dicionario['comidax'] = comidax
#     dicionario['comiday'] = comiday
#     return dicionario 

# def recebe_eventos():
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             return False
#     return True

# def desenha(window,dicionario):

#     window.fill((0,149,0))
    
#     #Desenha borda
#     window.blit(dicionario['parede'],(0,0))
#     window.blit(dicionario['parede'],(770,0))
#     window.blit(dicionario['parede1'],(0,0))
#     window.blit(dicionario['parede1'],(0,670))
#     #Desenhar comida
#     pygame.draw.rect(window,(255,0,0),(dicionario['comidax'],dicionario['comiday'],dicionario['tamanho_quadrado'],dicionario['tamanho_quadrado']))
#     #DESENHA COBRA
#     for pixel in dicionario['pixels']:
#         pygame.draw.rect(window, (255,255,255), [pixel[0], pixel[1], dicionario['tamanho_cobra'], dicionario['tamanho_cobra']])


#     pygame.display.update()

# def game_loop(window,dicionario):
#     while recebe_eventos():
#         gerar_comida(dicionario)
#         desenha(window,dicionario)
    
# w,d= inicializa()
# game_loop(w,d)


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import pygame
# import random
# pygame.mixer.init()
# # pygame.init()
# # pygame.display.set_caption("JOGO DA COBRINHA")
# # window = pygame.display.set_mode((1200, 800))
# relogio = pygame.time.Clock()

# # cores 
# preta = (0, 0, 0)
# branca = (255, 255, 255)
# vermelha = (255, 0, 0)
# verde = (0, 255, 0)
# verde_2 = (0, 149,0)

# # parametros da cobrinha
# tamanho_quadrado = 50
# velocidade_jogo = 15
# imagem = {}
# imagem['parede'] = pygame.image.load('imagens/parede2.png')
# imagem['comida'] = pygame.image.load('imagens/maca.png')

# #imagens das maçãs
# imagem['img_maca'] = pygame.image.load('imagens/maca.png')
# imagem['maca'] = pygame.transform.scale(imagem['img_maca'],(30,40))

# #IMAGNES DA COBRA
# imagem['img_cobra'] = pygame.image.load('imagens/cobra_cabeca.png')
# imagem['cobra'] = pygame.transform.scale(imagem['img_cobra'],(50,50))

# imagem['cobra_direita']= pygame.transform.rotate(imagem['cobra'],90)
# imagem['cobra_cima']= pygame.transform.rotate(imagem['cobra'],180)
# imagem['cobra_esquerda']= pygame.transform.rotate(imagem['cobra'],270)
# imagem['cobra_baixo'] = imagem['cobra'] 

# imagem['img_cobra_rabo'] = pygame.image.load('imagens/cobra_rabo.png')
# imagem['cobra_rabo'] = pygame.transform.scale(imagem['img_cobra_rabo'],(50,50))
# imagem['cobra_rabo_direita'] = pygame.transform.rotate(imagem['cobra_rabo'],90)
# imagem['cobra_rabo_cima'] = pygame.transform.rotate(imagem['cobra_rabo'],180)
# imagem['cobra_rabo_esquerda'] = pygame.transform.rotate(imagem['cobra_rabo'],270)
# imagem['cobra_rabo_baixo'] = imagem['cobra_rabo']
    
# imagem['img_cobra_corpo'] = pygame.image.load('imagens/cobra_corpo.png')
# imagem['cobra_corpo'] = pygame.transform.scale(imagem['img_cobra_corpo'],(50,50))
# imagem['cobra_corpo_direita'] = pygame.transform.rotate(imagem['cobra_corpo'],90)
# imagem['cobra_corpo_cima'] = pygame.transform.rotate(imagem['cobra_corpo'],180)
# imagem['cobra_corpo_esquerda'] = pygame.transform.rotate(imagem['cobra_corpo'],270)
# imagem['cobra_corpo_baixo'] = imagem['cobra_corpo']

# imagem['img_cobra_mov1'] = pygame.image.load('imagens/cobra_mov1.png')
# imagem['cobra_mov1'] = pygame.transform.scale(imagem['img_cobra_mov1'],(50,50))

# imagem['img_cobra_mov2'] = pygame.image.load('imagens/cobra_mov2.png')
# imagem['cobra_mov2'] = pygame.transform.scale(imagem['img_cobra_mov2'],(50,50))

# imagem['img_cobra_mov3'] = pygame.image.load('imagens/cobra_mov3.png')
# imagem['cobra_mov3'] = pygame.transform.scale(imagem['img_cobra_mov3'],(50,50))

# imagem['img_cobra_mov4'] = pygame.image.load('imagens/cobra_mov4.png')
# imagem['cobra_mov4'] = pygame.transform.scale(imagem['img_cobra_mov4'],(50,50))


# imagem['game_over'] = pygame.mixer.Sound('sons/game-over-arcade-6435.mp3')


# def gerar_comida(dicionario_comida):
#     comida_x = round(random.randrange(50, 1150 - tamanho_quadrado) / (tamanho_quadrado)) * (tamanho_quadrado)
#     comida_y = round(random.randrange(50, 750 - tamanho_quadrado) / (tamanho_quadrado)) * (tamanho_quadrado)
#     dicionario_comida['comida_x'] = comida_x
#     dicionario_comida['comida_y'] = comida_y

#     return dicionario_comida


# def gerar_parede(dicionario):
#     parede = pygame.Rect((0,0),(tamanho_quadrado,tamanho_quadrado))
#     dicionario['pos_parede'] = [parede]

#     for y1 in range(0,800,tamanho_quadrado):
#         parede = pygame.Rect((0, y1), (tamanho_quadrado, tamanho_quadrado))
#         dicionario['pos_parede'].append(parede)
    
#     for x1 in range(0,1200,tamanho_quadrado):
#         parede = pygame.Rect((x1, 0), (tamanho_quadrado, tamanho_quadrado))
#         dicionario['pos_parede'].append(parede)

#     for y2 in range(0,800,tamanho_quadrado):
#         parede = pygame.Rect((1200-50, y2), (tamanho_quadrado,tamanho_quadrado))
#         dicionario['pos_parede'].append(parede)
    
#     for x2 in range(0,1200,tamanho_quadrado):
#         parede = pygame.Rect((x2, 800-tamanho_quadrado), (tamanho_quadrado, tamanho_quadrado))
#         dicionario['pos_parede'].append(parede)
#     return dicionario

# # def gerar_pedra(dicionario):
# #     pedra_x = round(random.randrange(50, 1200 - tamanho_quadrado) / (tamanho_quadrado)) * (tamanho_quadrado)
# #     pedra_y = round(random.randrange(50, 800 - tamanho_quadrado) / (tamanho_quadrado)) * (tamanho_quadrado)
# #     dicionario['pedra_x'] = pedra_x
# #     dicionario['pedra_y'] = pedra_y

#     return dicionario

# def desenhar_comida(window, tamanho, dicionario_comida):
#     pygame.draw.rect(window, verde_2, pygame.Rect(dicionario_comida['comida_x'], dicionario_comida['comida_y'], tamanho, tamanho))
#     window.blit(imagem['maca'],(dicionario_comida['comida_x'], dicionario_comida['comida_y']))
# # def desenhar_pedra(window, tamanho, dicionario):
# #     pygame.draw.rect(window, preta, pygame.Rect(dicionario['pedra_x'], dicionario['pedra_y'], tamanho, tamanho))

# def desenhar_cobra(window, tamanho, pixels):
#     for pixel in pixels:
#         pygame.draw.rect(window, verde, [pixel[0], pixel[1], tamanho, tamanho])
#         # window.blit(imagem['cobra']),((pixel[0],pixel[1],tamanho,tamanho))

# def desenhar_parede(window, dicionario):
#     for parede in dicionario['pos_parede']:
#         window.blit(imagem['parede'],parede)

# def desenhar_pontuacao(window, pontuacao):
#     fonte = pygame.font.SysFont("Helvetica", 25)
#     texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
#     window.blit(texto, [1, 1])

# def selecionar_velocidade(tecla):
#     velocidade_x = 0
#     velocidade_y = 0
#     if tecla == pygame.K_DOWN:
#         velocidade_x = 0
#         velocidade_y = tamanho_quadrado
#     elif tecla == pygame.K_UP:
#         velocidade_x = 0
#         velocidade_y = -tamanho_quadrado
#     elif tecla == pygame.K_RIGHT:
#         velocidade_x = tamanho_quadrado
#         velocidade_y = 0
#     elif tecla == pygame.K_LEFT:
#         velocidade_x = -tamanho_quadrado
#         velocidade_y = 0
#     if tecla == pygame.K_s:
#         velocidade_x = 0
#         velocidade_y = tamanho_quadrado
#     elif tecla == pygame.K_w:
#         velocidade_x = 0
#         velocidade_y = -tamanho_quadrado
#     elif tecla == pygame.K_d:
#         velocidade_x = tamanho_quadrado
#         velocidade_y = 0
#     elif tecla == pygame.K_a:
#         velocidade_x = -tamanho_quadrado
#         velocidade_y = 0
#     return velocidade_x, velocidade_y

# def rodar_jogo(window, dicionario, dicionario_comida):
#     fim_jogo = False

#     x = 1200 / 2
#     y = 800 / 2

#     velocidade_x = 0
#     velocidade_y = 0

#     tamanho_cobra = 1
#     pixels = []

#     comida = gerar_comida(dicionario_comida)
#     # pedra = gerar_pedra(dicionario)
#     dicionario = gerar_parede(dicionario)
    

#     while not fim_jogo:
#         window.fill(verde_2)

#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 fim_jogo = True
#                 return False
#             elif evento.type == pygame.KEYDOWN:
#                 if evento.type == pygame.KEYDOWN:
#                     if evento.key == pygame.K_ESCAPE:
#                         return False
#                 velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

    

#         # desenhar_comida
#         desenhar_comida(window,tamanho_quadrado,comida)
#         # desenhar pedra
#         # desenhar_pedra(window,tamanho_quadrado,pedra)

#         # atualizar a posicao da cobra
#         if x < 0 or x >= 1200 or y < 0 or y >= 800:
#             fim_jogo = True

#         x += velocidade_x
#         y += velocidade_y

#         # desenhar_cobra
#         pixels.append([x, y])
#         if len(pixels) > tamanho_cobra:
            
#             del pixels[0]

#         # se a cobrinha bateu no proprio corpo
#         for pixel in pixels[:-1]:
#             if pixel == [x, y]:
#                 fim_jogo = True

#         desenhar_cobra(window, tamanho_quadrado, pixels)
#         #desenhar parede
#         desenhar_parede(window,dicionario)

#         # desenhar_pontos
#         desenhar_pontuacao(window,tamanho_cobra - 1)

#         # atualizacao da tela
#         pygame.display.update()

#         # criar nova comida
#         if x == dicionario_comida['comida_x'] and y == dicionario_comida['comida_y']:
#             tamanho_cobra += 1
#             dicionario_comida = gerar_comida(dicionario_comida)
            

#         relogio.tick(velocidade_jogo)
        
#         #colisão da cobra com a parede
#         for pixel in pixels:
#             retan_cobra = pygame.Rect(pixel[0], pixel[1], tamanho_quadrado, tamanho_quadrado)  
#             for parede in dicionario['pos_parede']:
#                 if retan_cobra.colliderect(parede):
#                     imagem['game_over'].play()
#                     fim_jogo = True



# # rodar_jogo()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


import pygame
import tela_final
from random import randint
import funcoes_chefão as jogo
import tela_chefão

TILE_FRAME = 50

def inicializa():
    pygame.init()
    widht = 1200
    height = 800
    # QUANT_COELHOS = 5

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
        }],
        'clock' : clock,
        'status': True
    }


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
        parede = pygame.Rect((widht-TILE_FRAME, y2), (TILE_FRAME,TILE_FRAME))
        estado['pos_parede'].append(parede)
    
    for x2 in range(0,widht,TILE_FRAME):
        parede = pygame.Rect((x2, height-TILE_FRAME), (TILE_FRAME, TILE_FRAME))
        estado['pos_parede'].append(parede)

    dicionario = {}

    #fontes
    dicionario['fonte'] = pygame.font.Font('fonte/perfect_dos_vga_437/Perfect DOS VGA 437 Win.ttf',20)

    #posicao
    dicionario['pos_maca'] = pos_maca
    dicionario['pos_maca_especial'] = pos_maca_especial

    #imagem da parede
    dicionario['parede'] = pygame.image.load('imagens/parede2.png')

    #imagens dos coelhos
    # img_coelho = pygame.image.load('imagens/coelho.png')
    # dicionario['coelho_bom'] = pygame.transform.scale(img_coelho,(40,50))

    # img_coelho_mal = pygame.image.load('imagens/coelho_malvado.png')
    # dicionario['coelho_mal'] = pygame.transform.scale(img_coelho_mal,(40,50))

    #posicao aleatoria do coelho
    # dicionario['coelhos'] = []
    # for _ in range(QUANT_COELHOS):
    #     x = randint(100,1100)
    #     y = randint(100,700)        
    #     coelho = {
    #         'pos': pygame.Rect((x,y), (40, 50)),
    #         'img': dicionario['coelho_bom'],
    #         'malvado': False
    #         }
    #     dicionario['coelhos'].append(coelho)

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
    
    img_cobra_corpo = pygame.image.load('imagens/cobra_corpo.png')
    dicionario['cobra_corpo'] = pygame.transform.scale(img_cobra_corpo,(50,50))
    dicionario['cobra_corpo_horizontal'] = pygame.transform.rotate(dicionario['cobra_corpo'],90)
    dicionario['cobra_corpo_vertical'] = dicionario['cobra_corpo']

    img_cobra_quina = pygame.transform.scale(pygame.image.load('imagens/cobra_mov1.png'), (50,50))
    dicionario['cobra_quina_direita_baixo'] = img_cobra_quina
    dicionario['cobra_quina_esquerda_baixo'] = pygame.transform.rotate(img_cobra_quina, -90)
    dicionario['cobra_quina_esquerda_cima'] = pygame.transform.rotate(img_cobra_quina, -180)
    dicionario['cobra_quina_direita_cima'] = pygame.transform.rotate(img_cobra_quina, -270)

    #imagens das maçãs
    img_maca = pygame.image.load('imagens/maca.png')
    dicionario['maca'] = pygame.transform.scale(img_maca,(30,40))

    img_maca_especial = pygame.image.load('imagens/maca_especial.png')
    dicionario['maca_especial'] = pygame.transform.scale(img_maca_especial,(30,40))

    #sons
    musica = 'sons/8bit-music-for-game-68698.mp3'
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()

    dicionario['game_over'] = pygame.mixer.Sound('sons/game-over-arcade-6435.mp3')

    dicionario['comida'] = pygame.mixer.Sound('sons/eating-sound-effect-36186.mp3')

    return window,dicionario,estado 

def recebe_eventos(estado,dicionario,window):
    estado, dicionario = jogo.muda_movimento(estado, dicionario)

    y = estado['cobra'][0]['pos'][1] 
    x = estado['cobra'][0]['pos'][0] 
    # movimentação da cobra
    estado, x, y = jogo.movimenta(estado, x, y)
    
    # estado,dicionario = jogo.movimenta_coelho(estado,dicionario)

    estado, dicionario = jogo.atualiza_cobra(estado, dicionario, x, y)
            

    cabeca = estado['cobra'][0]
    retan_cobra = pygame.Rect((cabeca['pos'][0],cabeca['pos'][1]),(TILE_FRAME,TILE_FRAME))  

    #colisão da cobra c/ ela mesma
    estado, dicionario = jogo.colisao_cobra(estado, dicionario, retan_cobra)

    #colisão da cobra c/ parede
    estado, dicionario = jogo.colisao_parede(estado, dicionario, retan_cobra)
        
    #colisao da cobra com a maçã
    estado, dicionario = jogo.colisao_maca(estado, dicionario, retan_cobra)

    #colisao da cobra com a maçã especial
    estado, dicionario = jogo.colisao_maca_especial(estado, dicionario, retan_cobra)
    
    #colisao da cobra com o coelho
    # estado, dicionario = jogo.colisao_coelho(estado, dicionario, retan_cobra)

    return estado['status']

def desenha(window,dicionario,estado):
    window.fill((0,149,0))

    for cobra in estado['cobra']:
        window.blit(cobra['imag'],(cobra['pos'][0], cobra['pos'][1]))

    for parede in estado['pos_parede']:
        window.blit(dicionario['parede'],parede)

    # for coelho in dicionario['coelhos']:
    #     window.blit(coelho['img'],(coelho['pos'][0],coelho['pos'][1]))

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
        estado['clock'].tick(4)
        if estado['xp'] <= 5:
            desenha(window,dicionario,estado)
        else:
            break
    window,dicionario,estado = tela_chefão.inicializa()
    tela_chefão.game_loop(window,dicionario,estado)
    
    # jogo acaba e troca pra tela final
    w,d = tela_final.inicializa()
    d['morte'] = dicionario['morte']
    while (tela_final.game_loop(w,d)):
        pass
    # jogo recomeça
    w,d,e = inicializa()
    game_loop(w,d,e)

#inicializa o jogo
# w,d,e = inicializa()
# game_loop(w,d,e)
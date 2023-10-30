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

import pygame
import random

# pygame.init()
# pygame.display.set_caption("JOGO DA COBRINHA")
# window = pygame.display.set_mode((1200, 800))
relogio = pygame.time.Clock()

# cores 
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

# parametros da cobrinha
tamanho_quadrado = 20
velocidade_jogo = 15

def gerar_comida(dicionario):
    comida_x = round(random.randrange(0, 1200 - tamanho_quadrado) / (tamanho_quadrado)) * (tamanho_quadrado)
    comida_y = round(random.randrange(0, 800 - tamanho_quadrado) / (tamanho_quadrado)) * (tamanho_quadrado)
    dicionario['comida_x'] = comida_x
    dicionario['comida_y'] = comida_y

    return dicionario

def desenhar_comida(window, tamanho, dicionario):
    pygame.draw.rect(window, verde, pygame.Rect(dicionario['comida_x'], dicionario['comida_y'], tamanho, tamanho))

def desenhar_cobra(window, tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(window, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(window, pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
    window.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    velocidade_x = 0
    velocidade_y = 0
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo(window, dicionario):
    fim_jogo = False

    x = 1200 / 2
    y = 800 / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida = gerar_comida(dicionario)

    while not fim_jogo:
        window.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
                return False
            elif evento.type == pygame.KEYDOWN:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        return False
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # desenhar_comida
        desenhar_comida(window,tamanho_quadrado,comida)

        # atualizar a posicao da cobra
        if x < 0 or x >= 1200 or y < 0 or y >= 800:
            fim_jogo = True

        x += velocidade_x
        y += velocidade_y

        # desenhar_cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        # se a cobrinha bateu no proprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        desenhar_cobra(window, tamanho_quadrado, pixels)

        # desenhar_pontos
        desenhar_pontuacao(window,tamanho_cobra - 1)

        # atualizacao da tela
        pygame.display.update()

        # criar nova comida
        if x == dicionario['comida_x'] and y == dicionario['comida_y']:
            tamanho_cobra += 1
            dicionario = gerar_comida(dicionario)

        relogio.tick(velocidade_jogo)


# rodar_jogo()


import pygame
import time
import random


def game():
    pygame.init()
    tela = pygame.display.set_mode((800, 600))
    x_init = 400
    y_init = 300
    eixo_x = 0
    eixo_y = 0
    snake_lst = []
    tam = 1
    pygame.display.set_caption('Jogo da Cobrinha por Thiago Rto.Stk')
    mov(tela,x_init,y_init,eixo_x,eixo_y, snake_lst, tam)

def over(tela,pont):
    red = (255,0,0)
    white = (255,255,255)
    fonte = pygame.font.SysFont(None, 40)
    msg = fonte.render("Voce Perdeu",True,red)
    value = fonte.render(f'Seu Score: {pont}', True, white)
    tela.blit(msg, [250,300])
    tela.blit(value, [250,200])
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    quit()

def snake(snake_lst,tela,Cobra):
    for x in snake_lst:
        pygame.draw.rect(tela,Cobra, [x[0],x[1],10,10])

def score(score,tela):
    white = (255,255,255)
    fonte = pygame.font.SysFont(None, 30)
    value = fonte.render(f'Score: {str(score)}', True, white)
    tela.blit(value,[0,0])

def Fruta():
    rng = random.choice([0,9])
    if rng > 1:
        return 0 
    return 1

def mov(tela, y_init, x_init, eixo_x, eixo_y, snake_lst, tam):
    Blk = (0,0,0)
    Cobra = (0,255,0)
    Comida = (255,0,0)
    Comida2 = (0,0,255)
    comidax = round(random.randrange(0, 800) / 10) * 10
    comiday = round(random.randrange(0, 600) / 10) * 10
    spd = pygame.time.Clock()
    F_Point = Fruta()
    if F_Point == 0:
        pygame.draw.rect(tela,Comida,[comidax,comiday, 10, 10])
    else:
        pygame.draw.rect(tela,Comida2,[comidax,comiday, 10, 10])
    pygame.display.update()
    pontos = 0
    while not False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and eixo_x != 5:
                    eixo_x = -5
                    eixo_y = 0
                elif event.key == pygame.K_RIGHT and eixo_x != -5:
                    eixo_x = 5
                    eixo_y = 0
                elif event.key == pygame.K_UP and eixo_y != 5:
                    eixo_x = 0
                    eixo_y = -5
                elif event.key == pygame.K_DOWN and eixo_y != -5:
                    eixo_x = 0
                    eixo_y = 5
        if y_init < 5 or y_init > 595 or x_init < 5 or x_init > 795:
            over(tela,pontos)
        x_init += eixo_x
        y_init += eixo_y
        if x_init in range(comidax - 10, comidax + 10)  and y_init in range(comiday-10, comiday+10):
            #print("+1")
            comidax = round(random.randrange(0, 800) / 5) * 5
            comiday = round(random.randrange(0, 600) / 5) * 5
            if F_Point == 1:
                pontos += 10
            else:
                pontos += 20
            F_Point == Fruta() 
            tam += 1
            
        tela.fill(Blk)
        cabeça = []
        cabeça.append(x_init)
        cabeça.append(y_init)
        snake_lst.append(cabeça)
        score(pontos,tela)
        if len(snake_lst) > tam:
            del snake_lst[0]
        for x in snake_lst [:-1]:
            if x == cabeça:
                over(tela,pontos)
        snake(snake_lst,tela,Cobra)
        if F_Point == 1:
            pygame.draw.rect(tela,Comida,[comidax,comiday, 10, 10])
        else:
            pygame.draw.rect(tela,Comida2,[comidax,comiday, 10, 10])
        pygame.display.update()
        spd.tick(60)

game()
quit()

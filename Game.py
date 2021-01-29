import Foods
import pygame
import GameOver

def mov(tela, y_init, x_init, eixo_x, eixo_y, snake_lst, tam):
    Blk = (0,0,0)
    Cobra = (0,255,0)
    comida,cx,cy,cor = Foods.Food(tela)
    spd = pygame.time.Clock()
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
        if y_init < 0 or y_init > 590 or x_init < 0 or x_init > 790:
            GameOver.over(tela,pontos)
        x_init += eixo_x
        y_init += eixo_y
        if x_init in range(cx - 10, cx + 10)  and y_init in range(cy-10, cy+10):
            if comida > 2:
                pontos += 1
            elif comida >=1 and comida <= 2:
                pontos += 5
            else:
                pontos += 10
            comida,cx,cy,cor = Foods.Food(tela)
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
                GameOver.over(tela,pontos)
        pygame.draw.rect(tela,cor,[cx,cy, 10, 10])
        snake(snake_lst,tela,Cobra)
        pygame.display.update()
        spd.tick(60)


def score(score,tela):
    white = (255,255,255)
    fonte = pygame.font.SysFont(None, 30)
    value = fonte.render(f'Score: {str(score)}', True, white)
    tela.blit(value,[0,0])


def snake(snake_lst,tela,Cobra):
    for x in snake_lst:
        pygame.draw.rect(tela,Cobra, [x[0],x[1],10,10])

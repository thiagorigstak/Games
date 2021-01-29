import pygame
import Game

def over(tela,pont):
    blk = (0,0,0)
    red = (255,0,0)
    white = (255,255,255)
    fonte = pygame.font.SysFont(None, 30)
    fonte2 = pygame.font.SysFont(None, 40)
    msg = fonte.render("Voce Perdeu, para continuar pressione K, ou ESC para sair",True,red)
    value = fonte2.render(f'Seu Score: {pont}', True, white)
    tela.blit(msg, [100,300])
    tela.blit(value, [250,200])
    while 1:
        tela.blit(msg, [100,300])
        tela.blit(value, [250,200])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    Game.mov(tela,400,300,0,0,[],1)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        pygame.display.update()

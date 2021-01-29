import pygame
import Menu

def over(tela,pont):
    blk = (0,0,0)
    red = (255,0,0)
    white = (255,255,255)
    fonte = pygame.font.SysFont(None, 30)
    fonte2 = pygame.font.SysFont(None, 40)
    msg = fonte.render("Voce Perdeu, para voltar ao menu pressione ESC",True,red)
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
                if event.key == pygame.K_ESCAPE:
                    Menu.menu(tela)
        pygame.display.update()

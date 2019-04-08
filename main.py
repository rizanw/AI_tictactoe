import sys
import pygame
from game import Games as ui

def main():

    #setup pygame
    pygame.init()
    pygame.display.set_caption('TicTacToe with ABP')
    screen = pygame.display.set_mode(ui.screenSize)
    clock = pygame.time.Clock()
    screen.fill(ui.BGColor)
    #font
    bigFont = pygame.font.SysFont('Helvatica', 90)
    regFont = pygame.font.SysFont('Helvatica', 24)

    done = False

    XMouse = 0
    YMouse = 0

    mainBoard = ui.usedBoxChecked(False)
    chekedBox = ui.usedBoxChecked(False)

    pScore = 0
    cScore = 0
    dScore = 0

    ui.drawLines(screen)

    while not done:
        ui.drawScore(screen, font=regFont, dScore=dScore, pScore=pScore, cScore=cScore)
        mouseClicked = False
        pTurn = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.K_UP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEMOTION:
                XMouse, YMouse = event.pos

            elif event.type == pygame.MOUSEBUTTONUP:
                XMouse, YMouse = event.pos
                mouseClicked = True

        boxx, boxy = ui.getCoordinate(XMouse, YMouse)

        print(boxx, boxy)

        if boxx != None and boxy != None:
            if not chekedBox[boxx][boxy] and mouseClicked and pTurn is True:
                ui.XMarker(screen, boxx, boxy, font=bigFont)
                chekedBox[boxx][boxy] = True
                mainBoard[boxx][boxy] = 'X'
                pTurn = False
                pygame.display.update()

        pygame.display.flip()
        clock.tick(ui.FPS)


if __name__ == '__main__':
    main()


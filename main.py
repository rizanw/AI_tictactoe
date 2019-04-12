import sys
import pygame
from game import Games as ui
from AI import *

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

    ai = alphabeta()
    apb = abp()
    mm = minimax()

    mainBoard = ai.usedBoxChecked(0)
    chekedBox = ai.usedBoxChecked(False)

    pScore = 0
    cScore = 0
    dScore = 0

    ui.drawLines(screen)

    pTurn = True

    while not done:
        mouseClicked = False

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

        # print(boxx, boxy)

        if boxx != None and boxy != None and pTurn is True:
            ui.drawState(screen, regFont, "Your Turn")
            if mouseClicked:
                ui.XMarker(screen, boxx, boxy, font=bigFont)
                chekedBox[boxx][boxy] = -1
                mainBoard[boxx][boxy] = 'X'
                pTurn = False
                pygame.display.update()

        elif pTurn is False:
            ui.drawState(screen, regFont, "AI Turn     ")
            pygame.time.wait(500)

            # cMove = apb.alphabetapruning(mainBoard)

            depth = 0
            for i in range(0, 3):
                for j in range(0, 3):
                    # print(mainBoard[i][j])
                    if chekedBox[i][j] == 0:
                        depth += 1

            cMove = mm.minimax(chekedBox, depth, +1)

            # comp = ai.findBestMove(checkedBox=chekedBox, board=mainBoard)
            cX = cMove[0]
            cY = cMove[1]
            ui.OMarker(screen, cX, cY, font=bigFont)
            chekedBox[cX][cY] = +1
            mainBoard[cX][cY] = 'O'
            pygame.display.update()
            pTurn = True

        pWins = mm.wins(mainBoard, -1)
        cWins = mm.wins(mainBoard, +1)
        noWins = mm.endGame(mainBoard)

        print(pWins, cWins, noWins)
        if pWins:
            ui.drawState(screen, regFont, "Player Wins   ")
            pygame.time.wait(500)
            pygame.display.update()
        elif cWins == True and pWins == False:
            ui.drawState(screen, regFont, "Computer Wins   ")
            pygame.time.wait(500)
            pygame.display.update()
        if cWins == False and pWins == False and noWins == True:
            ui.drawState(screen, regFont, "Draw game. No Winner ")
            pygame.time.wait(500)
            pygame.display.update()


if __name__ == '__main__':
    main()


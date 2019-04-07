import pygame
import sys

#constanta
WindowWidth = 840
WindowHeight = 540
screenSize = [WindowWidth, WindowHeight]
FPS = 30
BoxSize = 100
GapSize = 10
BoardHeight = 3
BoardWidth = 3

XMargin = int(BoxSize/2)
YMargin = int(BoxSize)

#           R    G    B
White   = (255, 255, 255)
Black   = (0,   0,   0)
Grey    = (100, 100, 100)
BGrey   = (45,  46,  48)
GWhite  = (206, 207, 209)

BGColor = BGrey
BoxColor = BGColor
LineColor = Black

#setup pygame
pygame.init()
pygame.display.set_caption('TicTacToe with ABP')
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
screen.fill(BGColor)

#font
bigFont = pygame.font.SysFont('Helvatica', 90)
regFont = pygame.font.SysFont('Helvatica', 24)

def drawLines():
    LinesColor = GWhite

    #Draw Vertical Lines
    verLen = XMargin + BoxSize
    horLen = YMargin
    width = GapSize
    height = (BoxSize + GapSize) * BoardHeight

    pygame.draw.rect(screen, LinesColor, pygame.Rect(verLen, horLen, width, height))
    pygame.draw.rect(screen, LinesColor, pygame.Rect(verLen + BoxSize + GapSize, horLen, width, height))
    pygame.draw.rect(screen, LinesColor, pygame.Rect(verLen - BoxSize - GapSize, horLen, width, height))
    pygame.draw.rect(screen, LinesColor, pygame.Rect(verLen + (BoxSize + GapSize) * 2, horLen, width, height))

    #Draw Horizontal Lines
    verLen = XMargin
    horLen = YMargin + BoxSize
    width = (BoxSize + GapSize) * BoardWidth
    height = GapSize

    pygame.draw.rect(screen, LinesColor, pygame.Rect(verLen, horLen, width, height))
    pygame.draw.rect(screen, LinesColor, pygame.Rect(verLen, horLen + BoxSize + GapSize, width, height))
    pygame.draw.rect(screen, LinesColor, pygame.Rect(verLen, horLen + (BoxSize + GapSize) * 2, width, height))
    pygame.draw.rect(screen, LinesColor, pygame.Rect(verLen, horLen - BoxSize - GapSize, width, height))

def usedBoxChecked(pos):
    # Marking used boxes
    Boxes = []
    for i in range(BoardWidth):
        Boxes.append([pos] * BoardHeight)
    return Boxes

def drawScore(font, dScore, pScore, cScore):
    # draw score board
    scoreBoard = font.render(
        'Draw: ' + str(dScore) + '  ' + 'Player: ' + str(pScore) + '    ' + 'Computer: ' + str(cScore),
        True,
        Black,
        BGColor
    )
    scoreBoardRect = scoreBoard.get_rect()
    scoreBoardRect.x = WindowWidth - 300
    scoreBoardRect.y = WindowHeight - 300
    screen.blit(scoreBoard, scoreBoardRect)

def getCornerBox(boxx, boxy):
    left = boxx * (BoxSize + GapSize) + XMargin
    top = boxy * (BoxSize + GapSize) + YMargin
    return left, top

def getCoordinate(x, y):
    for boxx in range(BoardWidth):
        for boxy in range(BoardHeight):
            left, top = getCornerBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BoxSize, BoxSize)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)

def getCenterBox(Xpt, Ypt):
    centerx = Xpt * (BoxSize + GapSize) + XMargin + (BoxSize / 2)
    centery = Ypt * (BoxSize + GapSize) + YMargin + (BoxSize / 2) + 5
    return centerx, centery

def XMarker(XX, XY, font):
    Xpt, Ypt = getCenterBox(XX, XY)
    mark = font.render('X', True, Grey)
    markRect = mark.get_rect()
    markRect.centerx = Xpt
    markRect.centery = Ypt
    screen.blit(mark, markRect)

def OMarker(XX, XY, font):
    Xpt, Ypt = getCenterBox(XX, XY)
    mark = font.render('O', True, Grey)
    markRect = mark.get_rect()
    markRect.centerx = Xpt
    markRect.centery = Ypt
    screen.blit(mark, markRect)

def main():
    done = False

    XMouse = 0
    YMouse = 0

    mainBoard = usedBoxChecked(False)
    chekedBox = usedBoxChecked(False)

    pScore = 0
    cScore = 0
    dScore = 0

    drawLines()

    while not done:
        drawScore(font=regFont, dScore=dScore, pScore=pScore, cScore=cScore)
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

        boxx, boxy = getCoordinate(XMouse, YMouse)

        print(boxx, boxy)

        if boxx != None and boxy != None:
            if not chekedBox[boxx][boxy] and mouseClicked and pTurn == True:
                XMarker(boxx, boxy, font=bigFont)
                chekedBox[boxx][boxy] = True
                mainBoard[boxx][boxy] = 'X'
                pTurn = False
                pygame.display.update()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()


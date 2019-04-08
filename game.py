import pygame
import sys

class Games:
    # constanta
    WindowWidth = 840
    WindowHeight = 540
    screenSize = [WindowWidth, WindowHeight]
    FPS = 30
    BoxSize = 100
    GapSize = 10
    BoardHeight = 3
    BoardWidth = 3

    XMargin = int(BoxSize / 2)
    YMargin = int(BoxSize)

    #           R    G    B
    White = (255, 255, 255)
    Black = (0, 0, 0)
    Grey = (100, 100, 100)
    BGrey = (45, 46, 48)
    GWhite = (206, 207, 209)

    BGColor = BGrey
    BoxColor = BGColor
    LineColor = Black



    def drawLines(screen):
        LinesColor = Games.GWhite

        #Draw Vertical Lines
        verLen = Games.XMargin + Games.BoxSize
        horLen = Games.YMargin
        width = Games.GapSize
        height = (Games.BoxSize + Games.GapSize) * Games.BoardHeight

        pygame.draw.rect(screen, LinesColor, pygame.Rect(verLen, horLen, width, height))
        pygame.draw.rect(screen, LinesColor, pygame.Rect(verLen + Games.BoxSize + Games.GapSize, horLen, width, height))
        pygame.draw.rect(screen, LinesColor, pygame.Rect(verLen - Games.BoxSize - Games.GapSize, horLen, width, height))
        pygame.draw.rect(screen, LinesColor, pygame.Rect(verLen + (Games.BoxSize + Games.GapSize) * 2, horLen, width, height))

        #Draw Horizontal Lines
        verLen = Games.XMargin
        horLen = Games.YMargin + Games.BoxSize
        width = (Games.BoxSize + Games.GapSize) * Games.BoardWidth
        height = Games.GapSize

        pygame.draw.rect(screen, LinesColor, pygame.Rect(verLen, horLen, width, height))
        pygame.draw.rect(screen, LinesColor, pygame.Rect(verLen, horLen + Games.BoxSize + Games.GapSize, width, height))
        pygame.draw.rect(screen, LinesColor, pygame.Rect(verLen, horLen + (Games.BoxSize + Games.GapSize) * 2, width, height))
        pygame.draw.rect(screen, LinesColor, pygame.Rect(verLen, horLen - Games.BoxSize - Games.GapSize, width, height))

    def usedBoxChecked(pos):
        # Marking used boxes
        Boxes = []
        for i in range(Games.BoardWidth):
            Boxes.append([pos] * Games.BoardHeight)
        return Boxes

    def drawScore(screen, font, dScore, pScore, cScore):
        # draw score board
        scoreBoard = font.render(
            'Draw: ' + str(dScore) + '  ' + 'Player: ' + str(pScore) + '    ' + 'Computer: ' + str(cScore),
            True,
            Games.GWhite,
            Games.BGColor
        )
        scoreBoardRect = scoreBoard.get_rect()
        scoreBoardRect.x = Games.WindowWidth - 300
        scoreBoardRect.y = Games.WindowHeight - 300
        screen.blit(scoreBoard, scoreBoardRect)

    def getCornerBox(boxx, boxy):
        left = boxx * (Games.BoxSize + Games.GapSize) + Games.XMargin
        top = boxy * (Games.BoxSize + Games.GapSize) + Games.YMargin
        return left, top

    def getCoordinate(x, y):
        for boxx in range(Games.BoardWidth):
            for boxy in range(Games.BoardHeight):
                left, top = Games.getCornerBox(boxx, boxy)
                boxRect = pygame.Rect(left, top, Games.BoxSize, Games.BoxSize)
                if boxRect.collidepoint(x, y):
                    return (boxx, boxy)
        return (None, None)

    def getCenterBox(Xpt, Ypt):
        centerx = Xpt * (Games.BoxSize + Games.GapSize) + Games.XMargin + (Games.BoxSize / 2)
        centery = Ypt * (Games.BoxSize + Games.GapSize) + Games.YMargin + (Games.BoxSize / 2) + 5
        return centerx, centery

    def XMarker(screen, XX, XY, font):
        Xpt, Ypt = Games.getCenterBox(XX, XY)
        mark = font.render('X', True, Games.Grey)
        markRect = mark.get_rect()
        markRect.centerx = Xpt
        markRect.centery = Ypt
        screen.blit(mark, markRect)

    def OMarker(screen, XX, XY, font):
        Xpt, Ypt = Games.getCenterBox(XX, XY)
        mark = font.render('O', True, Games.Grey)
        markRect = mark.get_rect()
        markRect.centerx = Xpt
        markRect.centery = Ypt
        screen.blit(mark, markRect)

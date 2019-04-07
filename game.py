import pygame
import sys

#constanta
WindowWidth = 640
WindowHeight = 480
screenSize = [WindowWidth, WindowHeight]
FPS = 30
BoxSize = 100
GapSize = 10
BoardHeight = 3
BoardWidth = 3
PlayerMark = 'X'
CompMark = 'O'
XMargin = int((WindowWidth - (BoardWidth * (BoxSize + GapSize))) / 2)
YMargin = int((WindowHeight - (BoardWidth * (BoxSize + GapSize))) / 2)

#           R     G       B
White   = (255, 255,    255)
Black   = (0,     0,      0)
Grey    = (100, 100,    100)

BGColor = White
BoxColor = BGColor
LineColor = Black

#setup pygame
pygame.init()
pygame.display.set_caption('TicTacToe with ABP')
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
screen.fill(White)

def drawLines():
    #Draw Vertical Lines
    left = XMargin + BoxSize
    top = YMargin
    width = GapSize
    height = (BoxSize + GapSize) * BoardHeight

    verRect1 = pygame.Rect(left, top, width, height)
    pygame.draw.rect(screen, Grey, verRect1)

    verRect2 = pygame.Rect(left + BoxSize + GapSize, top, width, height)
    pygame.draw.rect(screen, Grey, verRect2)

    #Draw Horizontal Lines
    left = XMargin
    top = YMargin + BoxSize
    width = (BoxSize + GapSize) * BoardWidth
    height = GapSize

    horRect1 = pygame.Rect(left, top, width, height)
    pygame.draw.rect(screen, Grey, horRect1)
    horRect2 = pygame.Rect(left, top + BoxSize + GapSize, width, height)
    pygame.draw.rect(screen, Grey, horRect2)

def usedBoxChecked(pos):
    Boxes = []
    for i in range(BoardWidth):
        Boxes.append([pos] * BoardHeight)
    return Boxes

def drawScore(font, dScore, pScore, cScore):
    scoreBoard = font.render(
        'Draw: ' + str(dScore) + '  ' + 'Player: ' + str(pScore) + '    ' + 'Computer: ' + str(cScore),
        True,
        Black,
        BGColor
    )
    scoreBoardRect = scoreBoard.get_rect()
    scoreBoardRect.x = 0
    scoreBoardRect.y = 0
    screen.blit(scoreBoard, scoreBoardRect)

def main():
    done = False
    is_blue = True

    x = 30
    y = 30

    smallFont = pygame.font.SysFont('Helvatica', 40)

    pScore = 0
    cScore = 0
    dScore = 0

    drawLines()
    while not done:
        drawScore(font=smallFont, dScore=dScore, pScore=pScore, cScore=cScore)
        mouseClicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.K_UP  and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_blue = not is_blue

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3

        # screen.fill((255, 255, 255))
        if is_blue:
            color = (0, 128, 255)
        else:
            color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()


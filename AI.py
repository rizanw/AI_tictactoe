import math
import copy
from game import Games as ui

class abp:
    def check_state(self, board):
        #check vertical
        for i in range(len(board)):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2] :
                if board[i][0] == 'X':
                    return -10
                if board[i][0] == "O":
                    return +10

        # Check horizon
        for i in range(len(board)):
            if board[0][i] == board[1][i] and board[1][i] == board[2][i] :
                if board[0][i] == 'X':
                    return -10
                if board[0][i] == "O":
                    return +10

        #check diagonal
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[0][0] == 'X':
                return -10
            elif board[0][0] == 'O':
                return +10
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[0][2] == 'X':
                return -10
            elif board[0][2] == 'O':
                return +10

        # check noMoreMove
        # for i in range(len(board)):
        #     for j in range(len(board[i])):
        #         if board[i][j] != False:
        #             return 0

    def minimax(self, board, alpha, beta, ismax):
        # val = self.check_state(board)
        boardBak = copy.copy(board)
        bestB = 10000
        bestA = -10000

        # if val == +10:
        #     return val
        # if val == -10:
        #     return val
        # if val == 0:
        #     return val

        if ismax:
            print("ismax")
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == False:
                        board[i][j] = 'O'
                        maxval = self.minimax(boardBak, alpha, beta, not ismax)
                        board[i][j] = False
                        bestA = max(bestA, maxval)
                        alpha = max(alpha, bestA)

                        print("bta: ", beta, bestA)
                        if bestA >= beta:
                            return bestA
            return bestA
        else:
            print("nomax")
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == False:
                        board[i][j] = 'X'
                        maxval = self.minimax(boardBak, alpha, beta, not ismax)
                        board[i][j] = False
                        bestB = min(bestB, maxval)
                        beta = min(beta, bestB)
                        print("apa: ", alpha, bestB)

                        if bestB <= alpha:
                            return bestB
            return bestB

    def alphabetapruning(self, board):
        best = -10000
        move = [-1, -1]
        boardBak = copy.deepcopy(board)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == False:
                    board[i][j] = 'O'
                    moveval = self.minimax(board=boardBak, alpha=-10000, beta=10000, ismax=False)
                    board[i][j] = False
                    print("main: ", moveval, best)
                    if moveval > best:
                        best = moveval
                        move[0] = i
                        move[1] = j

        print(move, best)
        return move

class alphabeta:
    def __init__(self):
        pass

    def usedBoxChecked(self, pos):
        # Marking used boxes
        Boxes = []
        for i in range(ui.BoardWidth):
            Boxes.append([pos] * ui.BoardHeight)

        return Boxes

    def evaluate(self, board):
        #check vertical
        for i in range(len(board)):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2] :
                if board[i][0] == 'X':
                    # print("+10")
                    return -10
                if board[i][0] == "O":
                    # print("-10")
                    return +10

        for i in range(len(board)):
            if board[0][i] == board[1][i] and board[1][i] == board[2][i] :
                if board[0][i] == 'X':
                    # print("+10")
                    return -10
                if board[0][i] == "O":
                    # print("-10")
                    return +10

        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[0][0] == 'X':
                # print("+10")
                return -10
            elif board[0][0] == 'O':
                return +10

        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[0][2] == 'X':
                return -10
            elif board[0][2] == 'O':
                return +10

    def isMovesLeft(self, board):

        for col in range(len(board)):
            for row in range(len(board[col])):
                if board[col][row] == False:
                    return True

        return False

    def minimax(self, board, depth, isMax):
        score = self.evaluate(board)

        if score is 10:
            return score

        if score is -10:
            return score

        if self.isMovesLeft(board) == False:
            return 0

        if isMax:
            best = -1000
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == False:
                        board[i][j] = 'O'
                        best = max(best, self.minimax(board, depth+1, not isMax))
                        board[i][j] = False
            return best
        else:
            best = 1000
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == False:
                        board[i][j] = 'X'
                        best = min(best, self.minimax(board, depth+1, not isMax))
                        board[i][j] = False
            return  best

    def findBestMove(self, board, checkedBox):
        bestMove = [-1, -1]
        bestVal = -1000

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] is False:
                    board[i][j] = 'O'

                    moveVal = self.minimax(board, 0, False)

                    board[i][j] = False

                    if moveVal > bestVal:
                        bestMove[0] = i
                        bestMove[1] = j
                        bestVal = moveVal


        print(bestVal)
        print(bestMove)
        return  bestMove
from math import inf as infinity

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
        val = self.check_state(board)
        boardBak = copy.copy(board)

        if val == +10:
            return val
        if val == -10:
            return val
        if val == 0:
            return val

        if ismax:
            print("ismax")
            best = -10000
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == False:
                        board[i][j] = 'O'
                        maxval = self.minimax(boardBak, alpha, beta, not ismax)
                        board[i][j]= False
                        best = max(best, maxval)
                        alpha = max(alpha, best)

                        print("main: ", beta, best)
                        if best >= beta:
                            return best
            return best
        else:
            print("nomax")
            best = 10000
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == False:
                        board[i][j] = 'X'
                        maxval = self.minimax(boardBak, alpha, beta, not ismax)
                        board[i][j] = False
                        best = min(best, maxval)
                        beta = min(beta, best)
                        print("main: ", alpha, best)

                        if best <= alpha:
                            return best
            return best

    def alphabetapruning(self, board):
        best = -10000
        move = [-1, -1]
        boardBak = copy.deepcopy(board)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == False:
                    board[i][j] = 'O'
                    moveval = self.minimax(board=boardBak, alpha=-1000, beta=1000, ismax=False)
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

class minimax:
    def __init__(self):
        self.player = 'X'
        self.computer = 'O'

    def wins(self, state, player):
        win_state = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]
        if [player, player, player] in win_state:
            # print("true")
            return True
        else:
            # print("false")
            return False

    def game_over(self, state):
        return self.wins(state, -1) or self.wins(state, +1)

    def empty_cells(self, state):
        cells = []

        for x, row in enumerate(state):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        # print(cells)
        return cells

    def evaluate(self, state):
        if self.wins(state, +1):
            score = +1
        elif self.wins(state, -1):
            score = -1
        else:
            score = 0

        return score

    def minimax(self, state, depth, player):
        print(state)
        if player == +1:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        if depth == 0 or self.game_over(state):
            score = self.evaluate(state)
            return [-1, -1, score]

        for cell in self.empty_cells(state):
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = self.minimax(state, depth - 1, -player)
            state[x][y] = 0
            score[0], score[1] = x, y

            print(best[2], score[2])

            if player == +1:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value
        return best
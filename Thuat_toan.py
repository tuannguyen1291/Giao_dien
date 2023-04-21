class KnightsTour:
    moveX = [2, 1, -1, -2, -2, -1, 1, 2]
    moveY = [1, 2, 2, 1, -1, -2, -2, -1]


    def __init__(self, n):
        self.n = n
        self.board = [[-1 for i in range(n)] for j in range(n)]
        self.stack = []

    def s(self, x, y, stepsTaken):
        if stepsTaken == self.n * self.n:
            for r in self.board :
                print(r)
            return True

        possible_moves = []
        for i in range(len(self.moveX)):
            nextX = x + self.moveX[i]
            nextY = y + self.moveY[i]
            p = (nextX, nextY)
            if self.in_bounds(nextX, nextY) and self.board[nextX][nextY] == -1:
                possible_moves.append((nextX, nextY, self.onward_moves(p)))
        possible_moves.sort(key=self.onward_moves)


        for move in possible_moves:
            nextX = move[0]
            nextY = move[1]
            self.board[nextX][nextY] = stepsTaken
            if self.s(nextX,nextY,stepsTaken+1):
                self.stack.append([nextX,nextY])
                return True

            self.board[nextX][nextY] = -1

        return False

    def in_bounds(self, x, y):
        return (x >= 0) and (x < self.n) and (y >= 0) and (y < self.n)

    def onward_moves(self,pos):
        num_onward_moves = 0
        for i in range(len(self.moveX)):
            nextX = pos[0] + self.moveX[i]
            nextY = pos[1] + self.moveY[i]
            if self.in_bounds(nextX, nextY) and self.board[nextX][nextY] == -1:
                num_onward_moves += 1
        return num_onward_moves

    def solve(self, startX, startY):
        self.board[startX][startY] = 0
        self.s(startX, startY, 1)
        print("finished")
        return (self.board , self.stack)



if __name__ == '__main__':
    k = KnightsTour(8)
    print(k.solve(1, 3))




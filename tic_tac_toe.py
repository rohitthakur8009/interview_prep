

class TicTacToe:
    def __init__(self):
        self.board = [[' ',' ', ' '],[' ',' ', ' '],[' ',' ',' ']]
        self.next = 'X'
        self.moves = 0

    def draw_board(self):
        for row in self.board:
            print(" | ".join(row))

    def play(self, i, j):
        print(f"{self.next} plays {i},{j}")
        if self.board[i][j] == ' ':
            self.board[i][j] = self.next
            self.next = 'O' if self.next == 'X' else 'X'
            self.moves += 1
            result = self.is_win()

            if result:
                print(f'{result} wins')
            elif self.moves == 9:
                print('Game tied')

        else:
            print("Invalid move")

    def is_win(self):
        for row in self.board:
            if row[0] == row[1] == row[2]:
                return row[0]

        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]

        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        return None


board = TicTacToe()

board.play(0,0)
board.play(0,1)
board.play(1,1)
board.play(2,1)
board.play(2,2)
board.draw_board()

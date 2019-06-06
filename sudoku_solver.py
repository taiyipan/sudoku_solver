class Solution:
    def __init__(self):
        self.place_count = 0
        self.time_elapsed = 0

    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import time
        start = time.time()
        self.place_cell(board)
        self.time_elapsed = time.time() - start

    def print_board(self, board):
        print('Cell placement: {}'.format(self.place_count))
        for row in board:
            for cell in row:
                print(cell, end = ' ')
            print()
        print()

    # check current row
    def check_row(self, board, row, val):
        for cell in board[row]:
            if cell == val:
                return False
        return True

    # check current column
    def check_column(self, board, col, val):
        for row in range(len(board)):
            if board[row][col] == val:
                return False
        return True

    # check current subgrid
    def check_subgrid(self, board, row, col, val):
        r = row - row % 3
        c = col - col % 3
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                if board[i][j] == val:
                    return False
        return True

    # check if cell placement is valid
    def valid_cell(self, board, row, col, val):
        valid_row = self.check_row(board, row, val)
        valid_column = self.check_column(board, col, val)
        valid_subgrid = self.check_subgrid(board, row, col, val)
        if valid_row and valid_column and valid_subgrid:
            return True
        else:
            return False

    # recursive backtracking algorithm
    def place_cell(self, board):
        # define cell choices
        choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        if self.place_count != 0 and self.place_count % 1000 == 0:
            self.print_board(board)
        # loop through the board to find unfilled cell
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    # go through choices
                    for choice in choices:
                        # see if choice is valid
                        if self.valid_cell(board, row, col, choice):
                            # place cell
                            board[row][col] = choice
                            self.place_count += 1
                            # if solved, return
                            if self.place_cell(board):
                                return True
                            # if unsolved, revert to empty cell
                            else:
                                board[row][col] = '.'
                    # if all choices are tried and still unsolved, return
                    return False
        # if all cells are filled, return
        return True



sol = Solution()
board = [['9', '.', '8', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '1', '.', '.', '.', '5', '4', '.'],
         ['4', '.', '.', '3', '.', '.', '.', '.', '.'],
         ['.', '.', '2', '.', '5', '.', '1', '3', '.'],
         ['.', '.', '.', '2', '.', '.', '.', '.', '7'],
         ['.', '6', '.', '.', '3', '.', '.', '9', '.'],
         ['2', '.', '.', '.', '4', '3', '.', '.', '.'],
         ['.', '7', '.', '.', '.', '.', '.', '1', '.'],
         ['6', '.', '.', '.', '.', '.', '9', '7', '4']]
sol.print_board(board)
sol.solveSudoku(board)
sol.print_board(board)
print('Cell placements tried: {}'.format(sol.place_count))
print('Seconds elapsed: {:.5f}'.format(sol.time_elapsed))

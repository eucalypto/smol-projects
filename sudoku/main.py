from sudoku.sudoku import Sudoku

def printslice(slice):
    string = ""
    for row in slice:
        for field in row:
            string += str(field)
        string += "\n"
    print(string)


if __name__ == '__main__':
    sudoku_raw = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        #
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        #
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]
    sudoku = Sudoku.from_list(sudoku_raw)
    print(sudoku)
    print([field.number for field in sudoku.get_row(8)])
    print([field.number for field in sudoku.get_column(8)])
    printslice(sudoku.get_quadrant(2, 2))
    print([field.number for field in sudoku.get_quadrant(2, 2).reshape(1, 9)[0]])
    print(sudoku.check_quadrant(0, 0))
    print(sudoku.check_quadrant(2, 2))
    print(sudoku.check_column(0))
    print(sudoku.check_row(0))




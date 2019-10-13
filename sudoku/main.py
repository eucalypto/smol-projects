from sudoku.sudoku import Sudoku


def printslice(slice):
    string = ""
    for row in slice:
        for field in row:
            string += str(field)
        string += "\n"
    print(string)


if __name__ == '__main__':
    sudoku_raw_0 = [
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
    sudoku_raw = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 5, 6, 7, 0, 0, 0, 0, 0],
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
    # printslice(sudoku.get_quadrant(2, 2))
    print([field.number for field in sudoku.get_quadrant(2, 2)])
    print(sudoku.check_quadrant(0, 0))
    print(sudoku.check_quadrant(2, 2))
    print(sudoku.check_column(0))
    print(sudoku.check_row(0))
    print(sudoku.get_state())
    sudoku.solve()
    print(sudoku)

    # sudoku2_raw = [
    #     [3, 9, 0, 6, 0, 0, 0, 4, 7],
    #     [0, 2, 6, 9, 7, 0, 0, 0, 0],
    #     [0, 0, 1, 0, 0, 4, 2, 0, 0],
    #     #
    #     [6, 0, 0, 0, 5, 0, 8, 2, 0],
    #     [0, 0, 0, 1, 0, 6, 0, 0, 0],
    #     [0, 7, 4, 0, 2, 0, 0, 0, 1],
    #     #
    #     [0, 0, 2, 5, 0, 0, 4, 0, 0],
    #     [0, 0, 0, 0, 4, 1, 3, 8, 0],
    #     [5, 4, 0, 0, 0, 8, 0, 1, 2]
    # ]

    sudoku2_raw = [
        [7, 9, 8, 5, 0, 0, 0, 2, 0],
        [0, 0, 0, 3, 2, 0, 8, 0, 1],
        [1, 0, 2, 0, 9, 0, 0, 0, 0],
        #
        [5, 7, 0, 4, 0, 0, 3, 0, 9],
        [3, 2, 0, 0, 0, 0, 0, 1, 7],
        [9, 0, 6, 0, 0, 3, 0, 4, 2],
        #
        [0, 0, 0, 0, 4, 0, 1, 0, 6],
        [6, 0, 9, 0, 3, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 5, 9, 7, 4]
    ]
    sudoku2 = Sudoku.from_list(sudoku2_raw)
    print(sudoku2)
    sudoku2.solve()
    print(sudoku2)

    sudoku3_raw = [
        [8, 0, 0, 4, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 9],
        [0, 7, 0, 3, 0, 8, 6, 0, 0],
        #
        [2, 0, 0, 0, 0, 0, 0, 9, 0],
        [3, 8, 0, 0, 0, 0, 0, 2, 1],
        [0, 5, 0, 0, 0, 0, 0, 0, 8],
        #
        [0, 0, 4, 5, 0, 6, 0, 1, 0],
        [5, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 3, 0, 0, 6]
    ]
    sudoku3 = Sudoku.from_list(sudoku3_raw)
    print(sudoku3)
    sudoku3.solve()
    print(sudoku3)

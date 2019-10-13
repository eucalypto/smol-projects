from sudoku.Field import Field
import numpy as np


class Sudoku:
    def __init__(self):
        self.fields = np.empty((9, 9), dtype="object")
        self.solved = False

    @staticmethod
    def from_list(list_raw: list):
        sudoku = Sudoku()
        for i, row in enumerate(list_raw):
            for j, number in enumerate(row):
                sudoku.set_field(i, j, Field(number))
        return sudoku

    def set_field(self, row, column, field):
        self.fields[row, column] = field

    def get_field(self, row, column):
        return self.fields[row, column]

    def get_row(self, row_number):
        return self.fields[row_number, :]

    def check_row(self, row_number):
        row_entries = [field.number for field in self.get_row(row_number)]
        return Sudoku.check_numbers(row_entries)

    @staticmethod
    def check_numbers(iterable):
        for i in range(1, 10):
            if i not in iterable:
                return False
        return True

    def get_column(self, column_number):
        return self.fields[:, column_number]

    def check_column(self, column_number):
        column_entries = [field.number
                          for field in self.get_column(column_number)]
        return Sudoku.check_numbers(column_entries)

    def get_quadrant(self, row, column):
        row_start = Sudoku.get_quadrant_start(row)
        row_end = row_start + 3
        column_start = Sudoku.get_quadrant_start(column)
        column_end = column_start + 3
        return self.fields[row_start:row_end, column_start:column_end].reshape(1, 9)[0]

    @staticmethod
    def get_quadrant_start(index):
        if index in [0, 1, 2]:
            return 0
        if index in [3, 4, 5]:
            return 3
        if index in [6, 7, 8]:
            return 6

    def check_quadrant(self, row, column):
        quadrant_entries = [field.number for field in self.get_quadrant(row, column)]
        return Sudoku.check_numbers(quadrant_entries)

    def get_state(self):
        return_string = ""
        for row in self.fields:
            for field in row:
                return_string += str(field.fixed)
            return_string += "\n"
        return return_string

    def __str__(self):
        ret = ""
        for row in self.fields:
            for field in row:
                ret += str(field)
            ret += "\n"
        return ret

    def solve(self):
        while not self.solved:
            for row_index, row in enumerate(self.fields):
                for column_index, field in enumerate(row):
                    if field.fixed:
                        self.remove_candidates(row_index, column_index, field.number)
                        self.check_if_solved()

    def remove_candidates(self, row_index, col_index, candidate):
        # row
        for field in self.get_row(row_index):
            field.remove_candidate(candidate)

        # column
        for field in self.get_column(col_index):
            field.remove_candidate(candidate)

        # quadrant
        for field in self.get_quadrant(row_index, col_index):
            field.remove_candidate(candidate)

    def check_if_solved(self):
        for row in self.fields:
            for field in row:
                if not field.fixed:
                    self.solved = False
                    return False
        # otherwise:
        self.solved = True
        return True







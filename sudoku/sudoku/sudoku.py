from sudoku.Field import Field
import numpy as np


class Sudoku:
    def __init__(self):
        self.fields = np.empty((9, 9), dtype="object")

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
        row_start = row*3
        row_end = row_start + 3
        column_start = column*3
        column_end = column_start + 3
        return self.fields[row_start:row_end, column_start:column_end]

    def check_quadrant(self, row, column):
        quadrant_entries = [field.number for field in self.get_quadrant(row, column).reshape(1, 9)[0]]
        return Sudoku.check_numbers(quadrant_entries)

    def __str__(self):
        ret = ""
        for row in self.fields:
            for field in row:
                ret += str(field)
            ret += "\n"
        return ret


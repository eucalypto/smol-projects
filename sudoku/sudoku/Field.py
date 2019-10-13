class Field:
    def __init__(self, number=0):
        self.candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.fixed = False
        self.number = 0
        if number > 9 or number < 0:
            raise ValueError("The number must be between 1 and 9")
        if number != 0:
            self.number = number
            self.candidates = [number]
            self.fixed = True

    def __str__(self):
        return str(self.number)

    def remove_candidate(self, number):
        if number in self.candidates:
            self.candidates.remove(number)
            self.check_ambiguity()

    def check_ambiguity(self):
        if len(self.candidates) == 1:
            self.number = self.candidates[0]
            self.fixed = True

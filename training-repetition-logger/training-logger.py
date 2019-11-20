"""
This logger waits for you to input the number of repetitions you just did.
It then logs them for you with the current timestamp.
"""
import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class Entry:
    """
    This dataclass stores a timestamp entry with timestamp text and number of repetitions.
    """
    timestamp: str
    reps: int


class Workout:
    """
    Main class with data and logic (backend)
    """

    def __init__(self):
        self.entries: List[Entry] = []

    def change_last_number(self, correction: int):
        """change the last number to: correction"""
        try:
            self.entries[-1].reps = correction
        except IndexError:
            # This occurs when the user tries to amend the last entry before
            # there is even a first entry.
            # In this case: do nothing.
            pass

    def add_entry(self, reps: int):
        """Add another entry in workout with current timestamp."""
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.entries.append(Entry(timestamp, reps))

    def __str__(self):
        output = "Your workout:\n"
        for entry in self.entries:
            output += entry.timestamp + "; " + str(entry.reps) + "\n"
        output += "Total reps: " + str(self.total())
        return output

    def total(self) -> int:
        """Return total sum of repetitions."""
        return sum([entry.reps for entry in self.entries])

    def write_to_file(self):
        """Write log message to file in current directory

        The filename is based on the start of the workout.
        """
        filename = self.entries[0].timestamp + " workout log.txt"
        with open(filename, mode="w") as file:
            file.write(str(self) + "\n")


class Workouts:
    """
    Helper class that does input-output
    """

    @classmethod
    def run_in_command_line(cls):
        """
        This is the "main" method that runs the infinite loop for input.

        I don't like it. It is too long and too convoluted. I want to split it up in
        more logical and re-usable parts. But this is the best I can do right now. :(
        """
        workout = Workout()
        while True:
            last_reps = workout.entries[-1].reps \
                if workout.entries != [] \
                else 0
            input_line = input("Count of repetitions to be logged: "
                               f"(default: {last_reps}, or '[h]elp'): ")
            if input_line == "":
                workout.add_entry(last_reps)
                print(workout)
                workout.write_to_file()
            elif input_line.lower().startswith("h"):
                Workouts.print_help()
            elif input_line.lower().startswith("q"):
                print(workout)
                break
            elif input_line.lower().startswith("p"):
                print(workout)
            elif input_line.lower().startswith("a"):
                # Get correct number
                try:
                    correct = Workouts.to_int(input("Please give the new number: "))
                except ValueError:
                    continue
                workout.change_last_number(correct)
                print(workout)
                workout.write_to_file()
                continue
            else:
                try:
                    reps = Workouts.to_int(input_line)
                except ValueError:
                    continue
                workout.add_entry(reps)
                print(workout)
                workout.write_to_file()

    @classmethod
    def to_int(cls, raw: str) -> int:
        try:
            output = int(raw)
        except ValueError as v_error:
            print(v_error)
            print(f"Could not convert {raw} into int. Please try again")
            raise v_error
        return output

    @classmethod
    def print_help(cls):
        print("You have the following commands:\n"
              + "[h]elp: this help message\n"
              + "[q]uit: print workout and quit\n"
              + "[a]mend: amend last number without changing the timestamp\n"
              + "[p]rint: print current workout\n")


if __name__ == '__main__':
    Workouts.run_in_command_line()

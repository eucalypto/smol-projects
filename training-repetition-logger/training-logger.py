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

    def change_last_number(correction):
        # change the last number to: correction
        print("changing number to:", correction)
        pass

    def add_entry(self, reps: int):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "; "
        self.entries.append(Entry(timestamp, reps))

    def __str__(self):
        output = "Your workout:\n"
        for entry in self.entries:
            output += entry.timestamp + str(entry.reps) + "\n"
        output += "Total reps: " + str(self.total())
        return output

    def total(self) -> int:
        return sum([entry.reps for entry in self.entries])


class Workouts:
    """
    Helper class that does input-output
    """

    @classmethod
    def run_in_command_line(cls):
        workout = Workout()
        while True:
            last_reps = workout.entries[-1].reps \
                if workout.entries != [] \
                else 0
            inputline = input("Please insert number of repetitions"
                              f"(default: {last_reps}, or '[h]elp'):")
            if inputline == "":
                workout.add_entry(last_reps)
                print(workout)
            elif inputline.lower().startswith("h"):
                Workouts.print_help()
            elif inputline.lower().startswith("q"):
                print(workout)
                break
            elif inputline.lower().startswith("p"):
                print(workout)
            elif inputline.lower().startswith("a"):
                # Get correct number
                correct = int(input("Please give the new number:"))
                change_last_number(correct)
                continue
            else:
                try:
                    reps = int(inputline)
                except ValueError as verror:
                    print("Could not convert input into a number.")
                    print(verror)
                    print("Please try again.")
                    continue
                workout.add_entry(reps)
                print(workout)

    @classmethod
    def print_help(cls):
        print("You have the following commands:\n"
              + "[h]elp: this help message\n"
              + "[q]uit: print workout and quit\n"
              + "[a]mend: amend last number without changing the timestamp\n"
              + "[p]rint: print current workout\n")


if __name__ == '__main__':
    Workouts.run_in_command_line()

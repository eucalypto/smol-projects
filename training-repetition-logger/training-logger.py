"""
This logger waits for you to input the number of repetitions you just did.
It then logs them for you with the current timestamp.
"""
import datetime

logstring = ""
print(logstring)

workout = [0]


def change_last_number(correction):
    # change the last number to: correction
    print("changing number to:", correction)
    pass


while True:
    inputline = input(f"Please insert number of repetitions (default: {workout[-1]}, or '[h]elp'):")
    if inputline.lower().startswith("q"):
        print("Here's your workout again:\n"
              + logstring
              + "Total reps: "
              + str(sum(workout)))
        break
    elif inputline == "":
        inputline = workout[-1]
    elif inputline.lower().startswith("h"):
        print("You have the following commands:\n"
              + "[h]elp: this help message\n"
              + "[q]uit: print workout and quit\n"
              + "[a]mend: amend last number without changing the timestamp")
        continue
    elif inputline.lower().startswith("a"):
        # Get correct number
        correct = int(input("Please give the new number:"))
        change_last_number(correct)
        continue

    try:
        reps = int(inputline)
    except ValueError as verror:
        print("Could not convert input into a number.")
        print(verror)
        print("Please try again.")
        continue

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "; "
    workout.append(reps)
    logstring += timestamp + str(reps) + "\n"
    print("your workout so far:\n"
          + logstring + "Total reps: "
          + str(sum(workout)))

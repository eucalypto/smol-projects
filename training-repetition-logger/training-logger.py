"""
This logger waits for you to input the number of repetitions you just did.
It then logs them for you with the current timestamp.
"""
import datetime

logstring = ""
print(logstring)

workout = []
while True:
    inputline = input("Please insert number of repetitions (or '[q]uit'):")
    if inputline.lower().startswith("q"):
        print("Here's your workout again:\n"
              + logstring
              + "Total reps: "
              + str(sum(workout)))
        break

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

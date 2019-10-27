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
        break
    reps = int(inputline)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "; "
    workout.append(reps)
    logstring += timestamp + str(reps) + "\n"
    print("your workout so far:\n"
          + logstring + "Total reps: "
          + str(sum(workout)))

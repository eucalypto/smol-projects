import argparse
import datetime
import calendar


# set up command line args
argparser = argparse.ArgumentParser(description="Generate Dynalist log entries for the specified month.")
argparser.add_argument("-m", "--month", type=str, default="now",
                       help="Month in ISO format: '2019-12'. "
                            "If you give nothing, the current month is assumed.")
args = argparser.parse_args()

# input decisions
month = args.month
if month != "now":
    month += "-01"
    try:
        start = datetime.date.fromisoformat(month)
    except ValueError as error:
        print(error)
        exit()
else:
    start = datetime.date.today().replace(day=1)


# Generate dates for months
days_of_month = reversed(list(
    calendar.Calendar().itermonthdates(start.year, start.month)
    ))
for day in days_of_month:
    if day.month != start.month:
        continue
    print(day.isoformat(), day.strftime("%a"))

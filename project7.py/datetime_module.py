import time
from datetime import datetime


def stopwatch():
    """Simple stopwatch that measures elapsed time."""
    input("Press Enter to START the stopwatch...")
    start = datetime.now()

    input("Press Enter to STOP the stopwatch...")
    end = datetime.now()

    elapsed = (end - start).total_seconds()
    print(f"\nElapsed Time: {round(elapsed, 2)} seconds\n")


def show_current_datetime():
    """Return formatted current datetime."""
    now = datetime.now()
    print("\nCurrent Datetime:", now.strftime("%d-%m-%Y %H:%M:%S"))


def date_difference():
    """Calculate difference between two dates."""
    d1 = input("Enter first date (YYYY-MM-DD): ")
    d2 = input("Enter second date (YYYY-MM-DD): ")

    dt1 = datetime.strptime(d1, "%Y-%m-%d")
    dt2 = datetime.strptime(d2, "%Y-%m-%d")

    print("\nDifference:", abs((dt2 - dt1).days), "days")


def formatted_date():
    """Return formatted date."""
    now = datetime.now()
    print("Formatted Date:", now.strftime("%A, %d %B %Y"))


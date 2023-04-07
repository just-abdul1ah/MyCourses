from datetime import date,datetime
from validator_collection import validators
import inflect
import sys


def main():
    birth = input('Date you were born: ')
    try:
        validators.date(birth)
        minutes = calculate(birth)
        minutes = round(minutes)
        engine = inflect.engine()
        number = engine.number_to_words(minutes)
        number = number.replace('and ', '').capitalize()
        print(number + ' minutes')
    except Exception:
        sys.exit('An error occurred.')

def calculate(birth):
    """Calculates the number of minutes between the current date and the inputted date."""
    today = date.today()
    y1 = today.year
    m1 = today.month
    d1 = today.day

    birth = datetime.strptime(birth, '%Y-%m-%d')
    y2 = birth.year
    m2 = birth.month
    d2 = birth.day

    interval = datetime(y1, m1, d1) - datetime(y2, m2, d2)
    minutes = interval.total_seconds() / 60
    return minutes

if __name__ == "__main__":
    main()
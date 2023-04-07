def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO: remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
    return float(d.replace('$', ''))


def percent_to_float(p):
    # TODO: remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
    return float(p.replace('%', '')) / 100


main()
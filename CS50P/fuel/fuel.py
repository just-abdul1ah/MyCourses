# We are going to get a fraction from the user
import sys

def main():
    f = input('Fraction: ').strip()
    print(gauge(convert(f)))


def convert(fraction):
    x,y = fraction.split('/')
    x = int(x)
    y = int(y)
    if x>y:
        raise ValueError
    elif y==0:
        raise ZeroDivisionError
    return round(x*100/y)


def gauge(left):
    if left >= 99:
        return 'F'
    elif left <= 1:
        return 'E'
    else:
        return f'{left}%'


if __name__ == "__main__":
    main()
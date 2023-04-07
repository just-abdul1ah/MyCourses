def main():
    t = input('Hello: ').strip().lower()
    print(f'${value(t)}')


def value(g):
    g = str(g)
    if g.startswith('hello'):
        return 0
    elif g.startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
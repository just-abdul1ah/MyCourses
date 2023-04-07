from cs50 import get_float


def give_change(change):
    change = float("{:.2f}".format(change))

    i25 = int(change / 0.25)
    change -= 0.25 * i25
    change = float("{:.2f}".format(change))
    print(change)

    i10 = int(change / 0.10)
    change -= 0.10 * i10
    change = float("{:.2f}".format(change))
    print(change)

    i5 = int(change / 0.05)
    change -= 0.05 * i5
    change = float("{:.2f}".format(change))
    print(change)

    i1 = int(change / 0.01)
    change -= 0.01 * i1
    change = float("{:.2f}".format(change))
    print(change)

    print(i1 + i5 + i10 + i25)


while True:
    change = get_float('Change owed: ')
    if change >= 0:
        break
give_change(change)

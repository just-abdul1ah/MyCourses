from cs50 import get_int


def makePyramid(h):
    if h == 0:
        return
    makePyramid(h-1)
    i = h
    while (i != height):
        print(' ', end='')
        i += 1
    for i in range(h):
        print('#', end='')
    print('  ', end='')
    for i in range(h):
        print('#', end='')
    print('')


while True:
    height = get_int('Height: ')
    if height > 0 and height < 9:
        break
makePyramid(height)
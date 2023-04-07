from random import randint


def main():
    l = get_level()
    score = 0
    for i in range(10):
        t = 0
        x = generate_integer(l)
        y = generate_integer(l)
        r = x + y
        while True:
            print(f'{x} + {y} = ', end='')
            if t == 3:
                print(r)
                break

            try:
                a = int(input())
                if a == r:
                    score += 1
                    break
                else:
                    print('EEE')
                    t += 1
                    continue
            except Exception:
                print('EEE')
                t += 1
                continue
    print(f'Score: {score}')


def get_level():
    while True:
        try:
            l = int(input('Level: '))
            if l in [1,2,3]:
                return l
            else:
                continue
        except Exception:
            continue


def generate_integer(level):
        if level == 1:
            return randint(0, 10)
        else:
            return randint(1*pow(10,level-1), 10*pow(10,level-1))


if __name__ == "__main__":
    main()
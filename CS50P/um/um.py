import re

def main():
    print(count(input("Text: ")))


def count(s):
    ls = s.lower().split(' ')
    c = 0
    for w in ls:
        if re.search('^um(\.*),?(\?)?$', w):
            c += 1

    return c

if __name__ == "__main__":
    main()
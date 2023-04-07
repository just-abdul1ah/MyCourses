import re

pattern = '([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])'

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if re.search(fr'^{pattern}\.{pattern}\.{pattern}\.{pattern}$', ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
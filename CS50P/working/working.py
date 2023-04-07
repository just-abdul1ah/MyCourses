import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    output = ''
    min1 = '00'
    min2 = '00'
    #if match := re.search(r'([^(:|\s)]+):?([^( AM| PM)]+) (AM|PM)([^\d]+)([^:]+):?([^( AM| PM)]+)(AM|PM).+', s):
    if match := re.search(r'([^(:|\s)]+):?([^(\s)]+)? (AM|PM)([^\d]+)([^(:|\s)]+):?([^\s]+)? (AM|PM)$', s):
        hour1 = match.group(1)
        if match.group(2):
            min1 = match.group(2).strip()

        hour2 = match.group(5)
        if match.group(6):
            min2 = match.group(6).strip()

        mode1 = match.group(3)
        mode2 = match.group(7)

        space = match.group(4)

        if valid_min(min1) and valid_min(min2) and check(space) and valid_hour(hour1) and valid_hour(hour2):
            hour1 = reformat(mode1, hour1)
            hour2 = reformat(mode2, hour2)
            output = f'{hour1}:{min1}{space}' + f'{hour2}:{min2}'
        else:
            raise ValueError

        return output
    else:
        raise ValueError


def check(space):
    if space.strip() != 'to':
        return False
    else:
        return True

def format(i):
    i = int(i.strip())
    if i > 10:
        if i == 12:
            return '00'
        return f'{i}'
    else:
        return f'0{i}'

def reformat(mode, hour):
    if mode == 'AM':
        hour = format(hour)
    elif mode == 'PM':
        if int(hour.strip()) != 12:
            hour = str(int(hour)+12)
            
    return hour

def valid_min(min):
    return (int(min) < 60)

def valid_hour(hour):
    return (int(hour.strip()) <= 12)


if __name__ == "__main__":
    main()
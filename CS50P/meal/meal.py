def main():
    converted_time = convert(input('What time is it? '))
    if 7 <= converted_time <= 8:
        print('breakfast time')
    elif 12 <= converted_time <= 13:
        print('lunch time')
    elif 18 <= converted_time <= 19:
        print('dinner time')

def convert(time):
    hour, minutes = time.split(':')
    return float(hour) + (float(minutes) / 60)
if __name__ == "__main__":
    main()
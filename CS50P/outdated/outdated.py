# so we have a list of months and when the user types a month we just need to check whether it is a valid month
# Or if he inputs a date we should also check that.

month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            date = input('Date: ').strip().lower().title().split(' ')
            if len(date) > 1:
                if date[0] in month:
                    if date[1].find(',') == -1:
                        continue
                    else:
                        date[1] = date[1].replace(',', '')
                    date[0] = month.index(date[0]) + 1
                    date[1] = int(date[1])
                    date[2] = int(date[2])
                    if date[1] > 31 or date[1] <= 0:
                        continue
                    display(date)
                    break
                else:
                    continue
            else:
                new_date = date[0].split('/')
                for d in range(3):
                    if new_date[d].isnumeric():
                        new_date[d] = int(new_date[d])
                    else:
                        raise StopIteration
                if 12 < new_date[0] or new_date[0] <= 0:
                    continue
                elif new_date[1] > 31 or new_date[1] <= 0:
                    continue
                display(new_date)
                break
        except StopIteration:
            continue

def display(d):
    d = list(d)
    d.reverse()
    t = d[2]
    d[2] = d[1]
    d[1] = t

    for n in range(3):
        if n != 2:
            d[n] = str(d[n]) + '-'
        else:
            d[n] = str(d[n])

    for date in d:
        if int(date.replace('-', '')) > 9:
            print(date, end='')
        else:
            print(f'0{date}', end='')

    print()

main()
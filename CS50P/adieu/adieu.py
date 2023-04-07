names = []

def display():
    people = ''
    if len(names) == 1:
        people = names[0]
    elif len(names) == 2:
        people = names[0] + ' and ' + names[1]
    else:
        for name in names:
            i = names.index(name)
            if i == (len(names) - 2):
                people += names[i] + ', and ' + names[i+1]
                break
            people += name + ', '

    print('Adieu, adieu, to ' + people)


while True:
    try:
        name = input('Name: ')
        names.append(name)
    except EOFError:
        print()
        display()
        break
e = input('Expression: ').strip().split(' ')

x = float(e[0])
y = e[1]
z = float(e[-1])

match y:
    case '+':
        print(f'{(x+z):.1f}')
    case '-':
        print(f'{(x-z):.1f}')
    case '*':
        print(f'{(x*z):.1f}')
    case '/':
        if z != 0:
            print(f'{(x/z):.1f}')
        else:
            print('z can not be zero during division')
    case _:
        print('incorrect operator')

# if y == '+':
#     print(f'{(x+z):.1f}')
# elif y == '-':
#     print(f'{(x-z):.1f}')
# elif y == '*':
#     print(f'{(x*z):.1f}')
# elif y == '/':
#     if z != 0:
#         print(f'{(x/z):.1f}')
#     else:
#         print('z can not be zero during division')
# else:
#     print('incorrect operator')


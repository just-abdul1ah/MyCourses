from pyfiglet import Figlet
import sys

def get_input():
    return input('Input: ')

if len(sys.argv) == 1:
    print('Output: \n' + Figlet().renderText(get_input()))
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--f'):
    try:
        print('Output: \n' + Figlet(sys.argv[2]).renderText(get_input()))
    except Exception:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
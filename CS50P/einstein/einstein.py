# Define a main function which prompts the user an input and then calls the calculate function to print the result

def main():
    calculate(int(input('m: ')))

def calculate(mass):
    return print(f'E: {mass * pow(3 * pow(10, 8), 2)}')

main()
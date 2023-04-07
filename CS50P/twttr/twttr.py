def main():
    text = input('Input: ').strip()
    print(f'Output: {shorten(text)}')

def shorten(word):
    for char in word:
        if char.lower() in ['a','e','i','o','u']:
            word = word.replace(char, '')
    return word

if __name__ == '__main__':
    main()

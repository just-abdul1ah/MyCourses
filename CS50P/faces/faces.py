def main():
    print(convert(input('Text: ')))

def convert(text):
    return text.replace(":(", "🙁").replace(':)', '🙂')

main()
from cs50 import get_string


def calculate_grade(text):
    word_list = text.split(' ')
    words = len(word_list)

    sentences = 0
    s1_list = text.split('.')
    s2_list = text.split('!')
    s3_list = text.split('?')
    if (len(s1_list) > 1):
        sentences += len(s1_list) - 1
    if (len(s2_list) > 1):
        sentences += len(s2_list) - 1
    if (len(s3_list) > 1):
        sentences += len(s3_list) - 1

    chars = 0
    for word in word_list:
        for char in word:
            if (ord(char.upper()) > 64 and ord(char.upper()) < 91):
                chars += 1

    L = chars * 100 / words
    S = sentences * 100 / words
    index = 0.0588 * L - 0.296 * S - 15.8
    grade = round(index)
    if (grade < 1):
        print('Before Grade 1')
    elif (grade > 16):
        print('Grade 16+')
    else:
        print(f'Grade {grade}')


text = get_string('Text: ')
calculate_grade(text)
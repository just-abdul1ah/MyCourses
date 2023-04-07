from random import randint
import sys

def play(n):
    guess = randint(1, n)
    while True:
        try:
            g = int(input('Guess: '))
            if g == guess:
                sys.exit('Just right!')
            elif g > guess:
                print('Too large!')
            elif g < guess:
                print('Too small!')
            else:
                continue

        except Exception:
            continue
#This is a comment
#Another comment

while True:
    try:
        n = int(input('Level: '))
        if n > 0:
            play(n)
        else:
            continue
    except Exception:
        continue
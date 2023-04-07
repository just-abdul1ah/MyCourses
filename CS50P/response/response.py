from validator_collection import validators
import sys

try:
    if validators.email(input('Email: ').strip()):
        print('Valid')
except Exception:
    print('Invalid')
    sys.exit()
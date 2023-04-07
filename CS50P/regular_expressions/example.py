import re

email = input('Enter your email: ').strip()

# if re.search(r'^[^@]+@[^@]+\.edu$', email):
#     print('valid')

#re.IGNORECASE ignores uppercase and treats it like lowercase
if re.search(r'^(\w|\.)+@(\w+\.)?\w+\.(edu|com)$',email,re.IGNORECASE):
    print('valid')
else:
    print('invalid')
var_name = input('Variable name: ')

for char in var_name:
    if char.isupper():
        var_name = var_name.replace(char, '_'+char.lower())

print(var_name)

# In order to solve the problem I think we need a dictionary having two keys
# "Amount" and "Item" and whenever an item is added if it exists in the list
# We can just add one more to the existing amount

fruits = {}

while True:
    try:
        item = input().upper()
        if item in fruits:
            fruits[item] += 1
        else:
            fruits[item] = 1
        continue
    except EOFError:
        break

fruit_list = list(fruits.keys())
fruit_list.sort()

for fruit in fruit_list:
    print(f'{fruits[fruit]} {fruit}')
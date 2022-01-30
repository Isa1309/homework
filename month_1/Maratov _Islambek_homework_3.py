numbers = list()
letters = []
floats = list()
data_tuple = ['h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g']

while len(data_tuple) != 0:
    for i in data_tuple:
        if type(i) == str:
            letters.append(data_tuple.pop(data_tuple.index(i)))
        elif type(i) == int or type(i) == float:
            numbers.append(data_tuple.pop(data_tuple.index(i)))
for i in numbers:
    if type(i) == bool:
        letters.append(numbers.pop(numbers.index(i)))
letters.reverse()

for i in numbers:
    if type(i) == float:
        floats.append(numbers.pop(numbers.index(i)))
floats.clear()
numbers.append(2)
numbers.sort()


print()
print(numbers)

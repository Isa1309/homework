names2 = 'jack', 'mary', 'wayne'
strings = []
numbers = list()
bools = []
tpl_lst = []
oblects = [
    'list', 'tuple', 2, 5, 2.9, False, True,
    [1, 2, 3], names2
]
while len(oblects) != 0:
    for i in oblects:
        if type(i) == str:
            strings.append(oblects.pop(oblects.index(i)))
        elif type(i) == int or type(i) == float:
            numbers.append(oblects.pop(oblects.index(i)))
        elif type(i) == bool:
            bools.append(oblects.pop(oblects.index(i)))
        elif type(i) == list or type(i) == tuple:
            tpl_lst.append(oblects.pop(oblects.index(i)))

print(oblects)
print(strings)
print(bools)
print(numbers)
print(tpl_lst)





# names2 += names3
# print(names2)

# print(type(names))
# print(type(names2))
# print(type(names3))









# words = list('oop', 'apple', 'game')
# numbers = [9, 2, 7, 4, 3]
#
# p
# print(numbers.count(2))
#
#
#





#
#
# numbers.clear()











# numbers.sort()
# s_numbers = sorted(numbers)
# print(s_numbers)
# numbers[0] = 'one'

# numbers += words
# numbers.extend(words)

# numbers.append(2.7)
# numbers.insert(2, 2.1)


# numbers.remove("abc")
# # del numbers[2]
# deleted = numbers.pop(3)
# print(deleted)

# strihgs = "python"
# ints = 25
# floats = 2.5
# bools = True or False
# names = [strihgs, ints, floats, bools]
# print(names)
#
# names = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(names)
# print(names[1:-1:2])
#
# print(names[::-1])
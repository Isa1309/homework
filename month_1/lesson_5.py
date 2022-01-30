# print('Hello, John!')
# \
# def greeting(name):
#     print('Hello, {}!'.format(name))
#
# greeting('Azamat')
# greeting('John')
# greeting('Adil')

def greetings(name):
    print('Hello, {}!'.format(name.capitalize()))

# def upper_letter(arg):
#     return arg.upper()
#
# upped_word = upper_letter('bbs')
# print(upped_word)

# def plus(a, b):
#     return a + b
#
# print(plus(3, 2))

# def plus(*args):
#     return round(sum(args) / len(args), 2)
#
# print(plus(4, 8, 6, 44, 65465, 654654))

# def menu(breakfest, lunch, dinner):
#     return dict(breakfest=breakfest, lunch=lunch, dinner=dinner)
#     # return {'breakfes': breakfest, 'lunch': lunch, 'dinner': dinner}
#
# print(menu('каша', 'пельмени', 'плов'))
# print(menu(dinner='лагман', breakfest='яичница', lunch='борщ'))
# #
# def menu(**kwargs):
#     return kwargs
#
# print(menu(first='первый', second='второй', third='третий'))

from random import randint
import datetime

start = datetime.datetime.now()
name = input("Введиете ваше имя: ")
n = int(input("Введите количество попыток: "))
n1 = n

while n1 != 0:
    x = randint(1, 9)
    y = randint(1, 9)
    a = int(input(f"{x} * {y} = ?  "))
    b = (x * y)
    if a == x * y:
        print(b)
        with open('results.txt', 'a') as file:
            file.write(f'{x} * {y} = {a} ({b})'
                       "  Правильно!\n"
                       )
    else:
        print(b)
        with open('results.txt', 'a') as file:
            file.write(f'{x} * {y} = {a} ({b})'
                       "  Неправильно!\n"
                       )
    n1 -= 1
end = datetime.datetime.now() - start

with open('results.txt', 'a') as file:
    file.write(f'Было {n} попыток,'
                f'потраченное время {end}, имя: {name}\n'
                )

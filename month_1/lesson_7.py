from pprint import pprint
import random
from random import randint, choice
from datetime import datetime
import time



def greetings(name):
    hours = datetime.now().hour
    if hours >= 4 and hours <= 11:
        print(f'Доброе утро! {name}')
    if hours >= 12 and hours <= 17:
        print(f'Добрый день! {name}')
    if hours >= 18 and hours <= 23:
        print(f'Добрый вечер! {name}')


greetings("azat")



    # print('Hello, {}!'.format(name.capitalize()))



# print(datetime.now())
# time.sleep(20)
print(datetime.now().hour)




# guys = ['jack', 'alice', 'murat', 'anna', 'gregoriy']
# pprint(random.sample(guys, 2))
# print(randint(1, 5))
# print(choice(guys))
# print(random.a)


# from lesson_5 import greetings as g
# import lesson_5
#
# # greetings('Azamat')
# lesson_5.greetings('Samat')
# g('Kanat')



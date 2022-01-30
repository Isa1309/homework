abiturients1 = [
    {'name': 'Irina', 'ORT': 150},
    {'name': 'Wayne', 'ORT': 220},
    {'name': 'Fred', 'ORT': 90}
]
abiturients2 = [
    {'name': 'Anton', 'ORT': 150},
    {'name': 'Eliza', 'ORT': 220},
    {'name': 'Timur', 'ORT': 90}
]
print(type(abiturients1))
def list_studets(list):
    for i in list:
        for k, v in i.items():
            print(f'{k}: {v}')



def add_students(list, name, ORT):
    list.append(dict(name=name, ORT=ORT))
    list_studets(list)

add_students(abiturients1, input("Введите имя"), input("Введите количество баллов ОРТ"))

def del_students(list, name):
    for i in list:
        if name.title == i['name']:
            del_s = list.pop(list.index(i))
            print(f"{del_s['name']} Удален из студентов!")
    list_studets(list)

del_students(abiturients1, "Fred")



# # list_studets(abiturients1)
# list_studets(abiturients2)


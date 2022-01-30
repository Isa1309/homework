country = {
'japan': {'red', 'white'},
'russia': {'blue', 'white', 'red'},
'usa': {'red', 'blue', 'white'},
'brazil': {'green', 'white', 'yellow', 'blue'},
'canada': {'red', 'white'},
'chine': {'red', 'yellow'}
}

while True:
    quest = (input('Enter the color: '))
    new = set(quest.split())
    i = 0
    for country1, color in country.items():
        if quest in color:
            i = i + 1
            print(country1)
    if i == 0:
        print('program  stopped')
        break


movies = {
    "Jumanji": {
        "Amina": 10,
        "Artem": 9,
        "Irina": 5
    },
    "Spider-Man": {
        "Stas": 9,
        "Sasha": 7,
        "Kamila": 5
    },
    "The Fate of the Furious 8": {
        "Ilya": 10,
        "Islambek": 9,
        "Maxim": 7
    },
    "The maze runner": {
        "Amina": 7,
        "Altynai": 9,
        "Adinai": 5
    },
    "Harry Potter": {
        "Aida": 9,
        "Azamat": 9,
        "Aiym": 7
    },
}
while True:
    for name, grade in movies.items():
        def movies(name1):
            return dict(name1=name)
        print(movies(input("Введите название фильма")))
        if movies(name1) == name:
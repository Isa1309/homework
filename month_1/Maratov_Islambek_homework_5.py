def list_movies():
    for k, v in movies.items():
        print(k)


def find_movie(movie):
    if movie in movies.keys():
        return movie


movies = {
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
    }
}

def add_movie(movie):
    movie = movie.title()
    if not find_movie(movie):
        movies[movie] = {}
        print("Movie added successfully!\n")
    else:
        print("This movie already exist!")

def add_rating(movie):
    movie = movie.title()
    if find_movie(movie):
        name = input('Enter your name: ').title()
        rating = int(input("Enter rating 1 to 10: "))
        if rating <= 0 or rating >=11:
            print("Incorrect rating! ")
        else:
            movies[movie][name] = rating
            print(
                f"A rating has been added for "
                f"{movie}: {name} rated it {rating}"
            )
    else:
        print("This movie doesn't exist")

def list_ratings():
    for i in movies:
        ratings = []
        for k, v in movies[i].items():
            ratings.append(v)
        if len(ratings) >= 1:
            print(f"{i} is rated {round(sum(ratings) / len(ratings))}")
        else:
            print(f"Ratings is not yet available {i}")

while 1:
    list_movies()
    choice = input(
        'Choose the command:\n1) add movie\n'
        '2) add rating\n'
        '3) get list of ratings\n'
        'q) to exit\n'
    )

    if choice == '1':
        add_movie(movie=input('Enter movie: '))
    elif choice == '2':
        add_rating(movie=input('Enter movie: '))
    elif choice == '3':
        list_ratings()
    elif choice == 'q':
        break
    else:
        print('Incorrect command!')

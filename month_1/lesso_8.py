from random import randint, sample

cash = 500

while cash != 0:
    bet = int(input(
        "Введите вашу ставку: "
        f"Доступно: {cash}\n"
    ))
    comp = [randint(1, 6), randint(1, 6)]
    user = [randint(1, 6), randint(1, 6)]
    if sum(comp) > sum(user):
        cash -= bet
        with open('results.txt', 'a') as file:
            file.write(f'comp: {comp} - user: {user}\n'
                       f'Вы проиграли: {}')
    if sum(comp) < sum(user):
        cash += bet

    print(f"comp: {comp}, user: {user}")
    with open('results.txt', 'a') as file:
        file.write(f'comp: {comp} - user: {user}\n')
    with open('results.txt', 'r') as file:
        print(file.read())
    # print(sample(range(1, 6), 2))
    #
    # print(randint(1, 6), randint(1, 6))

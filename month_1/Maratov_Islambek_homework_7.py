import random
import datetime

start = datetime.datetime.now()
secret_numbers = random.randint(1, 100)
attempts = 0

while 1:
    N = int(input("Введите целое число: "))

    if 100 < N < 0:
        print("Вы ввели некоректное число! Введите целое число от 0 до 100 включительно.")
    if secret_numbers > N != secret_numbers:
        print(">")
    if secret_numbers < N != secret_numbers:
        print("<")
    if 1 <= N - secret_numbers <= 5 or -1 >= N - secret_numbers >= -5 and N != secret_numbers:
        print('Очень близко')
    if 6 <= N - secret_numbers <= 10 or -6 >= N - secret_numbers >= -10 and N != secret_numbers:
        print('Близко')
    if N - secret_numbers == 0:
        W = (
            "Вы угадали загаданное число!"
        )
        end = datetime.datetime.now() - start
        break
    attempts += 1
print(
    f"{W}\n"
    f"Вы справились за {end} секунд  и за {attempts} попыток!")

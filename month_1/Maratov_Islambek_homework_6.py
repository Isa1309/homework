ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [2, 4, 6, 8, 10]

new = list(map(lambda x: x * x, evens))
print(new)

while 1:
    N = input("Введите индекс: ")
    if N == "exit":
        break
    else:
        N = int(N)

    def function(ten):
        if N <= -1 or N > 9:
            print("Неверный индекс! Введите индес от 0 до 9 включительно.")
        else:
            print(ten[N])

    function(ten)

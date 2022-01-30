while 1:
    word = str(input('Введите ваше слово: '))
    vowels = 0
    consonants = 0
    if word == 'stop':
        break
    else:
        for i in word:
            letter = i.lower()
            if letter == "a" or letter == "e" or \
                    letter == "i" or letter == "o" or \
                    letter == "u" or letter == "y" or \
                    letter == "а" or letter == "у" or \
                    letter == "о" or letter == "ы" or \
                    letter == "э" or letter == "я" or \
                    letter == "ю" or letter == "ё" or \
                    letter == "и" or letter == "е":
                vowels += 1
            else:
                consonants += 1
        a = (vowels + consonants)
        b = 100
        v = round((b / a * vowels), 2)
        c = round((b / a * consonants), 2)
        print(f"Слово: {word}\n"
              f"Количество букв: {a}\n"
              f"Согласных букв: {consonants}\n"
              f"Гласных букв: {vowels}\n"
              f"Гласные/Согласные: {v}%/{c}%"
              )

Chyi = float(input("Введите среднюю температуру Чуйской области? "))
Osh = float(input("Введите среднюю температуру Ошской области? "))
Naryn = float(input("Введите среднюю температуру Нарынской области? "))
Talas = float(input("Введите среднюю температуру Талаской области? "))
Isyk_Kyl = float(input("Введите среднюю температуру Иссык-Кульской области? "))
Jalal_Abad = float(input("Введите среднюю температуру Джала-Абадской области? "))
Batken = float(input("Введите среднюю температуру Баткенской области? "))


average = ((Chyi + Osh + Naryn + Talas + Isyk_Kyl + Jalal_Abad + Batken) / 7)
average = round(average, 1)


print(f"Средний показатель температуры воздуха по КР на сегодня {average} °C.")
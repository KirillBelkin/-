# Простой калькулятор
choose = 1
while choose != 0:
    choose = "1 - сложение, 2 - Вычитание, 0 - Выход"
    choose = int(input(choose))
    if choose == 1:  # Сложение
        a = int(input("Введите a"))
        b = int(input("Введите b"))
        print("a + b = ", a + b)
    elif choose == 2:  # Вычитание
        a = int(input("Введите a"))
        b = int(input("Введите b"))
        print("a - b = ", a - b)

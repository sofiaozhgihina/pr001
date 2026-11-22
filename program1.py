try:
    a = int(input("Введите 1-е число: "))
    b = int(input("Введите 2-е число: "))
    print(f"Сумма {a} и {a} равна {a+b}")
    print(f"Разность {a} и {a} равна {a - b}")
except ValueError:
    print("Ошибка ввода")
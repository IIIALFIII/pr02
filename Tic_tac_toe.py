# Приветствие
def greet():
    print("---------------------")
    print("   Приветствуем вас  ")
    print("       В игре        ")
    print("   крестики-нолики   ")
    print("---------------------")
    print("  формат ввода: x y  ")
    print("  x - номер строки   ")
    print("  y - номер столбца  ")
    print("---------------------")


# Создаем функцию, выводящую более продвинутое игровое поле
def game():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(game_zone):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


# Функция ввода данных
def ask():
    while True:  # Создаём бесконечный цикл на корректность данных
        cords = input("         Ваш ход: ").split()  # Ввод в строку через пробел
        # Проверка на корректное количество символов
        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue
        # присваиваем переменным введённые элементы
        x, y = cords
        # Проверяем введены ли числа
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue
        # Меняем тип элементов на целое число
        x, y = int(x), int(y)
        # Проверяем диапазон координат
        if x < 0 or y < 0 or x > 2 or y > 2:
            print(" Координаты вне диапазона! ")
            continue
        # Проверяем свободна ли выбранная клетка
        if game_zone[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


# Переменная победы
def win():
    # Переменная с выйгрышными комбинациями
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(game_zone[c[0]][c[1]])

        if symbols == ["X", "X", "X"]:
            print("Выйграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выйграл 0!!!")
            return True
    return False


# Создаём игровую зону с помощью генератора списков
game_zone = [[" "] * 3 for i in range(3)]
# Переменная счётчик
num = 0
# Цикл игры
greet()
while True:
    # Переменная кол-ва ходов
    num += 1
    # Вывод игрового поля через функцию
    game()
    # Очередность хода
    if num % 2 == 1:  # Если число не чётное, то
        print(" Ходит крестик ")
    else:  # В противном случае
        print(" Ходит нолик ")
    # Проверка x, y на корректность с помощью созданной функции
    x, y = ask()
    # Заполнение поля элементами
    if num % 2 == 1:  # Если ходит крестик то
        game_zone[x][y] = "X"
    else:  # В противном случае
        game_zone[x][y] = "0"

    if win():
        break
    # конец игры
    if num == 9:
        print("Ничья")
        break

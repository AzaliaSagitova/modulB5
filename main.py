field =  [[" ", "1", "2", "3"],
          ["1", "-", "-", "-"],
          ["2", "-", "-", "-"],
          ["3", "-", "-", "-"]]

def draw_field():
    for x in field:
        print(x[0], x[1], x[2], x[3])

def cross():
    print("Сейчас ходит крестик X")
    string = int(input("Введите номер строки: "))
    column = int(input("Введите номер столбца: "))

    while string < 1 or string > 3 or column < 1 or column > 3 or field[string][column] == 'X' or field[string][column] == '0':
        string = int(input("Введите номер строки заново: "))
        column = int(input("Введите номер столбца заново: "))

    field[string][column] = "X"

def zero():
    print("Сейчас ходит нолик 0")
    string = int(input("Введите номер строки: "))
    column = int(input("Введите номер столбца: "))

    while string < 1 or string > 3 or column < 1 or column > 3 or field[string][column] == 'X' or field[string][column] == '0':
        string = int(input("Введите номер строки заново: "))
        column = int(input("Введите номер столбца заново: "))

    field[string][column] = "0"

def check():
    for x in field:
        if x[1] == x[2] == x[3] != "-":
            print("Победитель - ", x[1])
            victory[0] = 1
            break
    for i in range(1, 3):
        if field[1][i] == field[2][i] == field[3][i] != "-":
            print("Победитель -", field[1][i])
            victory[0] = 1
            break
    if field[1][1] == field[2][2] == field[3][3] != "-":
        print("Победитель -", field[1][1])
        victory[0] = 1

    elif field[1][3] == field[2][2] == field[3][1] != "-":
        print("Победитель -", field[1][3])
        victory[0] = 1

print("Крестики-нолики 3х3")

draw_field()
k = 0
victory = [0]
while True:
    cross()
    k += 1
    draw_field()
    check()
    if victory[0] == 1:
        break
    elif k == 9:
        print("Ничья")
        break
    zero()
    check()
    if victory[0] == 1:
        break
    k += 1
    draw_field()
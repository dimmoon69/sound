def to_base_12(num, base=12):
    # перевод в "12"
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = alpha[num % base]
    while num >= base:
        num = num // base
        b += alpha[num % base]
    return b[::-1]


# перевод в "10"
def to_base_10(number):
    if "." in number:
        a, b = int(number.split(".")[0], 12), int(number.split(".")[1], 12)
        return float(f"{a}.{b}")
    return int(number, 12)


def check_float(num):
    if num < 0:
        num = abs(num)
        zn = "-"
    else:
        zn = ""

    if isinstance(num, float):
        out = f"{to_base_12(int(str(num).split('.')[0]))}.{to_base_12(int(str(num).split('.')[1]))}"
    else:
        out = to_base_12(num)

    if out.split(".")[-1] == "0":
        out = out.split(".")[0]
    return zn + out


def calculate():
    # операции с числами
    left_number = input('Введите первое число: ')
    operation = input('Введите математическую операцию, для выполнения: ')
    right_number = input('Введите второе число: ')

    left_number_10 = to_base_10(left_number)
    right_number_10 = to_base_10(right_number)

    if operation == '+':
        print(f'{left_number} + {right_number} = {check_float(left_number_10 + right_number_10)}')

    elif operation == '-':
        print(f'{left_number} - {right_number} = {check_float(left_number_10 - right_number_10)}')

    elif operation == '*':
        print(f'{left_number} * {right_number} = {check_float(left_number_10 * right_number_10)}')

    elif operation == '/':
        if right_number != "0":
            print(f'{left_number} / {right_number} = {check_float(left_number_10 / right_number_10)}')
        else:
            print("Деление на 0")
    else:
        print('Вы не ввели допустимый оператор, пожалуйста, запустите программу еще раз.')

    again()


def again():
    calc_again = input('Введите Y для повторения или N для выхода.')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Увидимся позже.')
    else:
        again()


calculate()

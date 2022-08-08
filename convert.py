def calculate():
    number_1 = input('Введите первое число: ')
    operation = input('Введите математическую операцию, для выполнения: ')
    number_2 = input('Введите второе число: ')

    if operation == '+':
        print(f'{number_1} + {number_2} = {convert_base(int(number_1, 12) + int(number_2, 12))}')

    elif operation == '-':
        print('{} - {} = {}'.format(number_1, number_2, convert_base(int(number_1, 12) - int(number_2, 12))))

    elif operation == '*':
        print('{} * {} = {}'.format(number_1, number_2, convert_base(int(number_1, 12) * int(number_2, 12))))

    elif operation == '/':
        print('{} / {} = {}'.format(number_1, number_2, convert_base(int(number_1, 12) / int(number_2, 12))))

    else:
        print('Вы не ввели допустимый оператор, пожалуйста, запустите программу еще раз.')

    # Add again() function to calculate() function
    again()


def again():
    calc_again = input('Повторить введите Y или N для выхода.')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Увидимся позже.')
    else:
        again()


def convert_base(number, to_base=12, from_base=12):
    # first convert to decimal number
    n = int(number, from_base) if isinstance(number, str) else number
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n, m = divmod(n, to_base)
        res += alphabet[m]
        return res[::-1]
    else:
        return 0


calculate()


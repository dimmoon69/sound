import pandas

COEFFICIENT = 1.059463094221


class Calc:
    def __init__(self):
        self.letters = ['c', 'b', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
        self.start = 1
        self.num_interval = 0
        self.interval = 1
        self.data = {}
        self.num_interval = 0
        self.total_interval = []
        self.calc = []
        self.value_1 = None
        self.value_2 = None

    def get_value(self):
        for num in range(10, 200, 10):
            for number, letter in enumerate(self.letters):
                start = round(self.start * COEFFICIENT, 8)
                self.calc.append((f"{num}:{letter}", start))

    def start_value(self):
        if self.value_1 == "10:c":
            self.start = self.value_2
            return True
        else:
            for i, v in enumerate(self.calc):

                if v[0] == self.value_1:
                    for x in range(i):
                        self.value_2 /= COEFFICIENT
                        self.start = self.value_2
                    return True
            return False

    def to_base_12(self, num, base=12):
        # перевод в "12"
        alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        b = alpha[num % base]
        while num >= base:
            num //= base
            b += alpha[num % base]
        return b[::-1]

    def save_dict(self, num, data_num, letter, interval):
        self.data[num][data_num] = f"{num}:{letter}"
        self.data[f"Значение {num}"][data_num] = self.start
        self.data[f"Интервaл {num}"][data_num] = ""
        self.data[f"Частота Гц {num}"][data_num] = ""
        data_num += 1
        self.data[num][data_num] = ""
        self.data[f"Значение {num}"][data_num] = ""
        self.data[f"Интервaл {num}"][data_num] = self.to_base_12(self.num_interval)
        self.data[f"Частота Гц {num}"][data_num] = interval
        data_num += 1
        return data_num

    def save_file(self):
        df = pandas.DataFrame(self.data)
        print(df.fillna(""))
        df.to_excel('calculator.xlsx', index=False)
        print("\nРезультат был сохранен в файл с названием, calculator.xlsx")
        again()

    def calculator(self):
        self.value_1 = input("Введите переменную: ") or "20:n"
        try:
            self.value_2 = float(input("Введите значение: ") or 4.719)
        except:
            print("\nПроверьте введенное значение!")
            again()

        self.get_value()
        check = self.start_value()

        if check:
            for num in range(10, 200, 10):
                data_num = 0
                self.data[num] = {}
                self.data[f"Значение {num}"] = {}
                self.data[f"Интервaл {num}"] = {}
                self.data[f"Частота Гц {num}"] = {}
                for number, letter in enumerate(self.letters):
                    self.interval = round(self.start * COEFFICIENT - self.start, 8)
                    self.num_interval += 1
                    if number == 0:
                        data_num = self.save_dict(num, data_num, letter, self.interval)
                    else:
                        data_num = self.save_dict(num, data_num, letter, self.interval)
                    # print(f"{num}:{letter} = {self.start} "
                    #       f"\n\t\tИнтервал: {self.to_base_12(self.num_interval)} = {self.interval}")
                    self.start = round(self.start * COEFFICIENT, 8)
                    self.total_interval.append(self.interval)
                self.data[f"Частота Гц {num}"][data_num] = ""
                data_num += 1
                self.data[f"Частота Гц {num}"][data_num] = '{:.2f}'.format(sum(self.total_interval))
                # print("Сумма:" + "-" * 20, round(sum(self.total_interval)))
                self.total_interval.clear()
            # print(self.data)
            self.save_file()
        else:
            print("Проверьте введенную переменную!")


def again():
    calc_again = input('\nВведите Y для повторения или N для выхода.')

    if calc_again.upper() == 'Y':
        Calc().calculator()
    elif calc_again.upper() == 'N':
        print('Увидимся позже.')
    else:
        again()


if __name__ == '__main__':
    Calc().calculator()


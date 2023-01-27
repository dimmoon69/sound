import pandas

COEFFICIENT = 1.059463094221


class Calc:
    def __init__(self):
        self.column = 0
        self.start = 0
        self.num_interval = 0
        self.interval = 1
        self.data = {}
        self.total_interval = []
        self.calc = []
        self.value_1 = None
        self.value_2 = None

    def again(self):
        calc_again = input('\nВведите Y для повторения или N для выхода.')

        if calc_again.upper() == 'Y':
            Calc().calculator()
        elif calc_again.upper() == 'N':
            print('Увидимся позже.')
        else:
            self.again()

    def get_value(self):
        for num in range(1, 200, 1):
            start = round(self.start * COEFFICIENT, 8)
            self.calc.append((f"{self.to_base_12(num)}", start))

    def start_value(self):
        if self.value_1 == "1":
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

    def save_dict(self, num, data_num, interval):
        self.data[num][data_num] = self.to_base_12(self.num_interval)
        self.data[f"Значение {num}"][data_num] = self.start
        self.data[f"Интервaл {num}"][data_num] = ""
        self.data[f"Частота Гц {num}"][data_num] = ""
        data_num += 1
        self.data[num][data_num] = ""
        self.data[f"Значение {num}"][data_num] = ""
        self.data[f"Интервaл {num}"][data_num] = self.num_interval
        self.data[f"Частота Гц {num}"][data_num] = interval
        data_num += 1
        return data_num

    def save_file(self):
        df = pandas.DataFrame(self.data)
        print(df.fillna(""))
        df.to_excel('calculator.xlsx', index=False)
        print("\nРезультат был сохранен в файл с названием, calculator.xlsx")
        self.again()

    def calculator(self):
        self.column = input("Введите количество столбцов: ") or 25
        self.value_1 = input("Введите переменную: ") or "1"
        try:
            self.value_2 = float(input("Введите значение: ") or 1)
        except:
            print("\nПроверьте введенное значение!")
            self.again()

        self.get_value()
        check = self.start_value()

        if check:
            for num in range(1, int(self.column), 1):
                data_num = 0
                self.data[num] = {}
                self.data[f"Значение {num}"] = {}
                self.data[f"Интервaл {num}"] = {}
                self.data[f"Частота Гц {num}"] = {}
                for number in range(1, 13):
                    self.interval = round(self.start * COEFFICIENT - self.start, 8)
                    self.num_interval += 1
                    data_num = self.save_dict(num, data_num, self.interval)
                    self.start = round(self.start * COEFFICIENT, 8)
                    self.total_interval.append(self.interval)
                self.data[f"Частота Гц {num}"][data_num] = ""
                data_num += 1
                self.data[f"Частота Гц {num}"][data_num] = '{:.2f}'.format(sum(self.total_interval))
                self.total_interval.clear()
            self.save_file()
        else:
            print("Проверьте введенную переменную!")
            self.again()


if __name__ == '__main__':
    Calc().calculator()


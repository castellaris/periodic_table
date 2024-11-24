import tkinter as tk


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.winfo_toplevel().title("Периодическая таблица")
        self.topLabel = tk.Label(self, text="Нажмите, чтобы узнать информацию о веществе.", font=20)
        self.topLabel.grid(row=0, column=0, columnspan=18)

        column1 = [
            ('H', 'Водород', 'Атомный номер = 1\nАтомная масса =1.01\nСостоние = Газ\nГруппа = Щелочные металлы'),
            ('Li', 'Литий', 'Атомный номер = 3\nАтомная масса = 6.94\nСостояние = Твердое\nГруппа = Щелочные металлы'),
            ('Na', 'Натрий',
             'Атомный номер = 11\nАтомная масса = 22.99\nСостояние = Твердое\nГруппа = Щелочные металлы'),
            ('K', 'Калий', 'Атомный номер = 19\nАтомная масса = 39.10\nСостояние = Твердое\nГруппа = Щелочные металлы'),
            ('Rb', 'Рубидий',
             'Атомный номер = 37\nАтомная масса = 85.47\nСостояние = Твердое\nГруппа = Щелочные металлы'),
            ('Cs', 'Цезий',
             'Атомный номер = 55\nАтомная масса = 132.91\nСостояние = Твердое\nГруппа = Щелочные металлы'),
            ('Fr', 'Франций',
             'Атомный номер = 87\nАтомная масса = 223.00\nСостояние = Твердое\nГруппа = Щелочные металлы')]
        r = 1
        c = 0
        for b in column1:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="grey",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column2 = [('Be', 'Бериллий',
                    'Атомный номер = 4\nАтомная масса = 9.01\nСостояние = Твердое\nГруппа = Щелочно-земельные металлы'),
                   ('Mg', 'Магний',
                    'Атомный номер = 12\nАтомная масса = 24.31\nСостояние = Твердое\nГруппа = Щелочно-земельные металлы'),
                   ('Ca', 'Кальций',
                    'Атомный номер = 20\nАтомная масса = 40.08\nСостояние = Твердое\nГруппа = Щелочно-земельные металлы'),
                   ('Sr', 'Стронций',
                    'Атомный номер = 38\nАтомная масса = 87.62\nСостояние = Твердое\nГруппа = Щелочно-земельные металлы'),
                   ('Ba', 'Барий',
                    'Атомный номер = 56\nАтомная масса = 137.33\nСостояние = Твердое\nГруппа = Щелочно-земельные металлы'),
                   ('Ra', 'Радий',
                    'Атомный номер = 88\nАтомная масса = 226.03\nСостояние = Твердое\nГруппа = Щелочно-земельные металлы')]
        r = 2
        c = 1
        for b in column2:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="light green",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column3 = [('Sc', 'Скандий',
                    'Атомный номер = 21\nАтомная масса = 44.96\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('Y', 'Иттербий',
                    'Атомный номер = 39\nАтомная масса = 88.91\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('La   >|', 'Лантаний',
                    'Атомный номер = 57\nАтомная масса = 138.91\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('Ac   >|', 'Актиний',
                    'Атомный номер = 89\nАтомная масса = 227.03\nСостояние = Твердое\nГруппа = Переходные металлы')]
        r = 4
        c = 2
        for b in column3:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="light goldenrod",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column4 = [('Ti', 'Титан',
                    'Атомный номер = 22\nАтомная масса = 47.90\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('Zr', 'Цирконий',
                    'Атомный номер = 40\nАтомная масса = 91.22\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('Hf', 'Гафний',
                    'Атомный номер = 72\nАтомная масса = 178.49\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('Rf', 'Резерфордий',
                    'Атомный номер = 104\nАтомная масса = 261.00\nСостояние = Синтетика\nГруппа = Переходные металлы')]
        r = 4
        c = 3
        for b in column4:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="light goldenrod",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 10:
                r = 1
                c += 1

        column5 = [('V', 'Ванадий',
                    'Атомный номер = 23\nАтомная масса = 50.94\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('Nb', 'Ниобий',
                    'Атомный номер = 41\nАтомная масса = 92.91\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('Ta', 'Тантал',
                    'Атомный номер = 73\nАтомная масса = 180.95\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('Ha', 'Ганий',
                    'Атомный номер = 105\nАтомная масса = 262.00\nСостояние = Синтетика\nГруппа = Переходные металлы')]
        r = 4
        c = 4
        for b in column5:
            tk.Button(self,
                      text=b[0],
                      width=5, height=2,
                      bg="light goldenrod",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 10:
                r = 1
                c += 1

        column6 = [('Cr', 'Хром',
                    'Атомный номер = 24\nАтомная масса = 51.99\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('Mo', 'Молибден',
                    'Атомный номер = 42\nАтомная масса = 95.94\nСостояние= Твердое\nГруппа = Переходные металлы'),
                   ('W', 'Вольфрам',
                    'Атомный номер = 74\nАтомная масса = 183.85\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('Sg', 'Сиборгий',
                    'Атомный номер = 106\nАтомная масса = 266.00\nСостояние = Твердое\nГруппа = Переходные металлы')]
        r = 4
        c = 5
        for b in column6:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="light goldenrod",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column7 = [('Mn', 'Марганец',
                    'Атомный номер = 25\nАтомная масса = 178.49\nСостояние = Твердое\nГруппа = Переходные металлыs'),
                   ('Tc', 'Технеций',
                    'Атомный номер = 43\nАтомная масса = 178.49\nСостояние = Синтетика\nГруппа= Переходные металлы'),
                   ('Re', 'Рений',
                    'Атомный номер = 75\nАтомная масса = 178.49\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('Bh', 'Борий',
                    'Атомный номер = 107\nАтомная масса = 262.00\nСостояние = Синтетика\nГруппа = Переходные металлы')]
        r = 4
        c = 6
        for b in column7:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="light goldenrod",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column8 = [('Fe', 'Железо',
                    'Атомный номер = 26\nАтомная масса = 55.85\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('Ru', 'Рутений',
                    'Атомный номер = 44\nАтомная масса = 101.07\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('Os', 'Осмий',
                    'Атомный номер = 76\nАтомная масса = 190.20\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('Hs', 'Хассий',
                    'Атомный номер = 108\nАтомная масса = 265.00\nСостояние = Твердое\nГруппа = Переходные металлы')]
        r = 4
        c = 7
        for b in column8:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="light goldenrod",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column9 = [('Co', 'Кобальт',
                    'Атомный номер = 27\nАтомная масса = 58.93\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('Rh', 'Родий',
                    'Атомный номер = 45\nАтомная масса = 102.91\nСостояние = Синтетика\nГруппа = Переходные металлы'),
                   ('Ir', 'Ирридий',
                    'Атомный номер = 77\nАтомная масса = 192.22\nСостояние = Твердое\nГруппа = Переходные металлы'),
                   ('Mt', 'Мейтнерий',
                    'Атомный номер = 109\nАтомная масса = 266.00\nСостояние = Твердое\nГруппа = Переходные металлы')]
        r = 4
        c = 8
        for b in column9:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="light goldenrod",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column10 = [('Ni', 'Никель',
                     'Атомный номер = 28\nАтомная масса = 58.70\nСостояние = Твердое\nГруппа = Переходные металлы'),
                    ('Pd', 'Палладий',
                     'Атомный номер = 46\nАтомная масса = 106.40\nСостояние = Твердое\nГруппа = Переходные металлы'),
                    ('Pt', 'Платина',
                     'Атомный номер = 78\nАтомная масса = 195.09\nСостояние = Твердое\nГруппа = Переходные металлы')]
        r = 4
        c = 9
        for b in column10:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="light goldenrod",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column11 = [('Cu', 'Медь',
                     'Атомный номер= 29\nАтомная масса = 63.55\nСостояние = Твердое\nГруппа = Переходные металлы'),
                    ('Ag', 'Серебро',
                     'Атомный номер = 47\nАтомная масса = 107.97\nСостояние = Твердое\nГруппа = Переходные металлы'),
                    ('Au', 'Золото',
                     'Атомный номер = 79\nАтомная масса = 196.97\nСостояние = Твердое\nГруппа= Переходные металлы')]
        r = 4
        c = 10
        for b in column11:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="light goldenrod",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column12 = [('Zn', 'Цинк',
                     'Атомный номер = 30\nАтомная масса = 65.37\nСостояние = Твердое\nГруппа = Переходные металлы'),
                    ('Cd', 'Кадмий',
                     'Атомный номер = 48\nАтомная масса = 112.41\nСостояние = Твердое\nГруппа = Переходные металлы'),
                    ('Hg', 'Меркурий',
                     'Атомный номер = 80\nАтомная масса = 200.59\nСостояние = Жидкое\nГруппа = Переходные металлы')]
        r = 4
        c = 11
        for b in column12:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="light goldenrod",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column13_1 = [
            ('B', 'Борий', 'Атомный номер = 5\nАтомная масса = 10.81\nСостояние = Твердое\nГруппа = Неметаллы')]
        r = 2
        c = 12
        for b in column13_1:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="Light Blue",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column13_2 = [('Al', 'Аллюминий',
                       'Атомный номер = 13\nАтомная масса = 26.98\nСостояние = Твердое\nГруппа = Остальные металлы'),
                      ('Ga', 'Галлий',
                       'Атомный номер = 31\nАтомная масса = 69.72\nСостояние = Твердое\nГруппа = Остальные металлы'),
                      ('In', 'Индий',
                       'Атомный номер = 49\nАтомная масса = 69.72\nСостояние = Твердое\nГруппа = Остальные металлы'),
                      ('Ti', 'Таллий',
                       'Атомный номер = 81\nАтомная масса = 204.37\nСостояние = Твердое\nГруппа = Остальные металлы')]
        r = 3
        c = 12
        for b in column13_2:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="Light Pink",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column14_1 = [
            ('C', 'Углерод', 'Атомный номер = 6\nАтомная масса = 12.01\nСостояние = Твердое\nГруппа =Неметаллы'),
            ('Si', 'Кремний', 'Атомный номер = 14\nАтомная масса = 28.09\nСостояние = Твердое\nГруппа = Неметаллы')]
        r = 2
        c = 13
        for b in column14_1:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="Light Blue",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column14_2 = [('Ge', 'Германий',
                       'Атомный номер = 32\nАтомная масса = 72.59\nСостояние = Твердое\nГруппа = Остальные металлы'),
                      ('Sn', 'Олово',
                       'Атомный номер = 50\nАтомная масса = 118.69\nСостояние = Твердое\nГруппа = Остальные металлы'),
                      ('Pb', 'Ртуть',
                       'Атомный номер = 82\nАтомная масса = 207.20\nСостояние = Жидкое\nГруппа = Остальные металлы')]
        r = 4
        c = 13
        for b in column14_2:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="Light Pink",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column15_1 = [('N', 'NАзот', 'Атомный номер = 7\nАтомная масса = 14.01\nСостояние = Газ\nГруппа= Неметаллы'),
                      ('P', 'Фосфор',
                       'Атомный номер = 15\nАтомная масса = 30.97\nСостояние = Твердое\nГруппа = Неметаллы'),
                      ('As', 'Мышьяк',
                       'Атомный номер = 33\nАтомная масса = 74.92\nСостояние = Твердое\nГруппа = Неметаллы')]
        r = 2
        c = 14
        for b in column15_1:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="Light Blue",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column15_2 = [('Sb', 'Сурьма',
                       'Атомный номер = 51\nАтомная масса= 121.75\nСостояние = Твердое\nГруппа = Остальные металлы'),
                      ('Bi', 'Висмут',
                       'Атомный номер = 83\nАтомная масса = 208.98\nСостояние = Твердое\nГруппа = Остальные металлы')]
        r = 5
        c = 14
        for b in column15_2:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="Light Pink",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column16_1 = [
            ('O', 'Кислород', 'Атомный номер = 8\nАтомная масса = 15.99\nСостояние = Газ\nГруппа = Неметаллы'),
            ('S', 'Сера', 'Атомный номер = 16\nАтомная масса = 32.06\nСостояние = Твердое\nГруппа = Неметаллы'),
            ('Se', 'Селен', 'Атомный номер = 34\nАтомная масса = 78.96\nСостояние = Твердое\nГруппа = Неметаллы'),
            ('Te', 'Теллур', 'Атомный номер = 52\nАтомная масса = 127.60\nСостояние = Твердое\nГруппа = Неметаллы')]
        r = 2
        c = 15
        for b in column16_1:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="Light Blue",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column16_2 = [('Po', 'Полоний',
                       'Атомный номер = 84\nАтомная масса = 209.00\nСостояние= Твердое\nГруппа = Остальные металлы')]
        r = 6
        c = 15
        for b in column16_2:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="Light Pink",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column17 = [('F', 'Фтор', 'Атомный номер = 9\nАтомная масса = 18.99\nСостояние = Газ\nГруппа= Неметаллы'),
                    ('Cl', 'Хлор', 'Атомный номер = 17\nАтомная масса = 35.45\nСостояние = Газ\nГруппа = Неметаллы'),
                    ('Br', 'Бром',
                     'Атомный номер = 35\nАтомная масса = 79.90\nСостояние = Жидкость\nГруппа = Неметаллы'),
                    ('I', 'Йод', 'Атомный номер = 53\nАтомная масса = 126.90\nСостояние = Твердое\nГруппа= Неметаллы'),
                    ('At', 'Астат',
                     'Атомный номер = 85\nАтомная масса = 210.00\nСостояние = Твердое\nГруппа = Неметаллы')]
        r = 2
        c = 16
        for b in column17:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="Light Blue",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        column18 = [
            ('He', 'Гелий', 'Атомный номер = 2\nАтомная масса = 4.00\nСостояние = Газ\nГруппа = Благородные газы'),
            ('Ne', 'Неон', 'Атомный номер = 10\nАтомная масса = 20.18\nСостояние = Газ\nГруппа = Благородные газы'),
            ('Ar', 'Аргон', 'Атомный номер = 18\nАтомная масса = 39.95\nСостояние = Газ\nГруппа = Благородные газы'),
            ('Kr', 'Криптон', 'Атомный номер = 36\nАтомная масса = 83.80\nСостояние = Газ\nГруппа = Благородные газы'),
            ('Xe', 'Ксенон', 'Атомный номер = 54\nАтомная масса = 131.30\nСостояние = Газ\nГруппа = Благородные газы'),
            ('Rn', 'Радон', 'Атомный номер = 86\nАтомная масса = 222.00\nСостояние = Газ\nГруппа = Благородные газы')]
        r = 1
        c = 17
        for b in column18:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="indian red",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        self.fillerLine = tk.Label(self, text="")
        self.fillerLine.grid(row=10, column=0)

        lanthanide = [('>| Ce', 'Церий',
                       'Атомный номер = 58\nАтомная масса= 140.12\nСостояние = Твердое\nГруппа = Переходные металлы'),
                      ('Pr', 'Празеодим',
                       'Атомный номер = 59\nАтомная масса = 140.91\nСостояние = Твердое\nГруппа = Переходные металлы'),
                      ('Nd', 'Неодим',
                       'Атомный номер = 60\nАтомная масса = 144.24\nСостояние= Твердое\nГруппа = Переходные металлы'),
                      ('Pm', 'Прометий',
                       'Атомный номер = 61\nАтомная масса = 145.00\nСостояние = Синтетика\nГруппа = Переходные металлы'),
                      ('Sm', 'Самарий',
                       'Атомный номер = 62\nАтомная масса = 150.40\nСостояние= Твердое\nГруппа = Переходные металлы'),
                      ('Eu', 'Европий',
                       'Атомный номер = 63\nАтомная масса = 151.96\nСостояние = Твердое\nГруппа = Переходные металлы'),
                      ('Gd', 'Гадолиний',
                       'Атомный номер = 64\nАтомная масса = 157.25\nСостояние = Твердое\nГруппа = Переходные металлы'),
                      ('Tb', 'Тербий',
                       'Атомный номер = 65\nАтомная масса = 158.93\nСостояние = Твердое\nГруппа = Переходные металлы'),
                      ('Dy', 'Дипрозий',
                       'Атомный номер = 66\nАтомная масса = 162.50\nСостояние = Твердое\nГруппа = Переходные металлы'),
                      ('Ho', 'Гольмий',
                       'Атомный номер = 67\nАтомная масса = 164.93\nСостояние = Твердое\nГруппа= Переходные металлы'),
                      ('Er', 'Эрбий',
                       'Атомный номер = 68\nАтомная масса = 167.26\nСостояние = Твердое\nГруппа = Переходные металлы'),
                      ('Tm', 'Туллий',
                       'Атомный номер = 69\nАтомная масса = 168.93\nСостояние = Твердое\nГруппа = Переходные металлы'),
                      ('Yb', 'Иттербий',
                       'Атомный номер = 70\nАтомная масса = 173.04\nСостояние = Твердое\nГруппа = Переходные металлы'),
                      ('Lu', 'Лютеций',
                       'Атомный номер = 71\nАтомная масса = 174.97\nСостояние = Твердое\nГруппа = Переходные металлы')]
        r = 11
        c = 3
        for b in lanthanide:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="light goldenrod",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            c += 1
            if c > 18:
                c = 1
                r += 1

        actinide = [('>| Th', 'Торий',
                     'Атомный номер = 90\nАтомная масса = 232.04\nСостояние = Твердое\nГруппа = Переходные металлы'),
                    ('Pa', 'Проактиний',
                     'Атомный номер = 91\nАтомная масса = 231.04\nСостояние = Твердое\nГруппа = Переходные металлы'),
                    ('U', 'Уран',
                     'Атомный номер = 92\nАтомная масса = 238.03\nСостояние = Твердое\nГруппа= Переходные металлы'),
                    ('Np', 'Нептун',
                     'Атомный номер = 93\nАтомная масса = 237.05\nСостояние = Синтетика\nГруппа = Переходные металлыs'),
                    ('Pu', 'Плутоний',
                     'Атомный номер = 94\nАтомная масса = 244.00\nСостояние = Синтетика\nГруппа = Переходные металлы'),
                    ('Am', 'Америций',
                     'Атомный номер = 95\nАтомная масса = 243.00\nСостояние = Синтетика\nГруппа = Переходные металлы'),
                    ('Cm', 'Кюрий',
                     'Атомный номер = 96\nАтомная масса = 247\nСостояние = Синтетика\nГруппа = Переходные металлы'),
                    ('Bk', 'Берклий',
                     'Атомный номер = 97\nАтомная масса = 247\nСостояние = Синтетика\nГруппа = Переходные металлы'),
                    ('Cf', 'Калифорний',
                     'Атомный номер = 98\nАтомная масса = 247\nСостояние = Синтетика\nГруппа= Переходные металлы'),
                    ('Es', 'Эйнштейний',
                     'Атомный номер = 99\nАтомная масса = 252.00\nСостояние = Синтетика\nГруппа = Переходные металлы'),
                    ('Fm', 'Фермий',
                     'Атомный номер = 100\nАтомная масса = 257.00\nСостояние = Синтетика\nГруппа = Переходные металлы'),
                    ('Md', 'Менделеевий',
                     'Атомный номер = 101\nАтомная масса = 260.00\nСостояние = Синтетика\nГруппа = Переходные металлы'),
                    ('No', 'Нобелий',
                     'Атомный номер = 102\nАтомная масса = 259\nСостояние = Синтетика\nГруппа = Переходные металлы'),
                    ('Lr', 'Лоренсий',
                     'Атомный номер = 103\nАтомная масса = 262\nСостояние = Синтетика\nГруппа = Переходные металлы')]
        r = 12
        c = 3
        for b in actinide:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="light goldenrod",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            c += 1
            if c > 18:
                c = 1
                r += 1

        reset = [('Очистить', 'Нажмите, чтобы узнать информацию о веществе:', '')]
        r = 12
        c = 0
        for b in reset:
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg="black",
                      fg="white",
                      command=lambda text=b: self.name(text[1]) & self.info(text[2])).grid(row=r, column=c)
            r += 1
            if r > 7:
                r = 1
                c += 1

        self.infoLine = tk.Label(self, text="", justify='left')
        self.infoLine.grid(row=1, column=3, columnspan=10, rowspan=4)

    def name(self, text):
        self.topLabel.config(text=text)

    def info(self, text):
        self.infoLine.config(text=text)


root = tk.Tk()
a = App(root)
a.grid(row=0, column=0, sticky='nsew')
a.mainloop()
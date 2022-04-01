main_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for el in main_list:
    name = el.split()[-1]
    ed_name = name.lower().title()
    print(f'Привет, {ed_name}!')


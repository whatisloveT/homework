original_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in original_list:
    print(f'Привет, {i.split()[-1].title()}!')

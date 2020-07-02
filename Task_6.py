goods = []
characteristics = {'name': '', 'price': '', 'amount': '', 'pcs': ''}
analytics = {'name': [], 'price': [], 'amount': [], 'pcs': []}
num = 0
characteristics = None
control = None
while True:
    control = input("'нажмите В для выхода', 'нажмите Enter, чтобы продолжить', 'нажмите A, чтобы посмотреть аналитику'").upper()
    if control == 'В':
        break
    num +=1
    if control == 'A':
        print(f'\n Текущая аналитика \n {"-"} * 30')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print('-' * 30)
            for f in characteristics.keys():
                characteristics = input(f'Input feature "{f}"')
                characteristics[f] = int(characteristics) if (f == 'price' or f == 'amount') else characteristics
                analytics[f].append(characteristics[f])
            goods.append((num, characteristics))

goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(my_list)
print(my_analys)




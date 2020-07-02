# def season(month):
#     if month < 3 or month == 12:
#         return "Winter"
#     if 3 <= month < 6:
#         return "Spring"
#     if 6 <= month < 9:
#         return "Summer"
#     if 9 <= month < 12:
#         return "Autumn"
# b = 1
# while b<13:
#     print(b)
#     print(season (b))
#     b+=1
#
# print('введите месяц: ')

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Укажите номер месяца: "))
if month ==1 or month == 12 or month == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print("Такого месяца не существует")



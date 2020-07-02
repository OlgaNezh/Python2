my_list = [7, 5, 3, 3, 2]
print(f'рейтинг: {my_list}')
rating = int(input('введите число: '))
while rating != 111:
    for el in range(len(my_list)):
        if my_list[el] == rating:
            my_list.insert(el+1, rating)
            break
        elif my_list[0] < rating:
            my_list.insert(0, rating)
        elif my_list[-1] > rating:
            my_list.append(rating)
        elif my_list[el] > rating and my_list[el + 1] < rating:
            my_list.insert(el + 1, rating)
print(f'список: {my_list}')
rating = int(input('введите число: '))


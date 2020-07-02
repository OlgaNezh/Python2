# a = 0
# b = 1
# c = 2
# d = 3
# a,b,c,d = d,c,a,b
# a,b,c,d
# (0, 1, 2, 3)
# e = 3.75
# f = "hello"
# e, f = f,e
# e
# 'hi'
# f
# 3.75
# print(e)
# print(b)
# print(c)


el_count = int(input("Укажите число элементов списка "))
my_list = [8]
i = 0
el = 0
while i < el_count:
    my_list.append(input("Укажите следующее значение списка "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)

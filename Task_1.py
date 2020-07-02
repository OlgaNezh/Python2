c = [c * 3 for c in 'list' if c != 'i']
c
['lll', 'sss', 'ttt']
c = [c + d for c in 'list' if c != 'i' for d in 'spam' if d != 'a']
c
['ls', 'lp', 'lm', 'ss', 'sp', 'sm', 'ts', 'tp', 'tm']

my_int = 5
my_float = 1.2
my_str = "This is a python lesson"
my_list = ['a', '5']
my_tuple = ('b', '9')
my_dict = {'name': 'Olga', 'age': '37'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')


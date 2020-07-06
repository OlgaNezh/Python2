def add(usr_input: str) -> float:
    usr_str_list = usr_input.split()
    usr_num_list = list(map(float, filter(lambda x: x.isdigit(), usr_str_list)))
    return sum(usr_num_list)

total = 0
while True:
    get_input = input('enter numbers ')
    total += add(get_input)
    print(f'Total: {total}', end='\n\n')
    if 'Q' in get_input.upper():
        break
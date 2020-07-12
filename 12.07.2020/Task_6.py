def get_number_from_str(s):
    l = len(s)
    number_list = []
    i = 0
    while i < l:
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            number_list.append(int(s_int))
    return number_list
subjects = {}
syll = []

try:
    with open('file_6', 'r') as task6:
        for string in task6.readlines():
            S = string.replace("\n", "").partition(": ")
            subjects = {
                "subject": S[0],
                "hours": sum(get_number_from_str(S[2]))
            }
            syll.append(subjects)

        print(syll)
except IOError:
    print("Произошла ошибка ввода-вывода!")





def my_func (a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return 'b cannot be a zero'
    except ValueError:
        return 'enter only a number'
print(my_func(int(input('Enter a= ')), int(input('Enter b= '))))


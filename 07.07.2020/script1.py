def salary(hrsworked, payrate, bonus):
    if hrsworked <= 40:
        salary = (payrate * hrsworked) * 22 + bonus
    elif hrsworked > 40:
        salary = (payrate * (1.5 * (hrsworked - 40))) *22 + bonus
    return salary

payrate = int(input("Ставка в час: "))
hrsworked = int(input("Количество отработанных часов: "))
bonus = int(input("Премия: "))
print(salary(payrate, hrsworked, bonus))


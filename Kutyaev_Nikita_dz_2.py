
# Задание №1
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 3))
print(type(15 ** 3))


# Задание №2
list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for elem in list_1:
    if elem.isdigit():
        new_list.extend(['"', f'{int(elem):02d}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        new_list.extend(['"', f'{elem[0]}{int(elem[1:]):02d}', '"'])
    else:
        new_list.append(elem)
result = ' '.join(new_list)
print(result)


# Задание №4
name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in name_list:
    print('Привет, ', i.split()[-1].title(), '!')


# Задание №5
prices = [26.54, 23.2, 123.4, 59, 990.99, 499, 149.6, 789.45, 456.3, 55]
for price in prices:
    rub = int(price)
    kop = (price - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ')  # вывод списка в 1 строку

print(id(prices))
prices.sort()
print(id(prices))     # новый список не создан
for price in prices:
    rub = int(price)
    kop = (price - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ')  # вывод сортированного списка в 1 строку

prices = [26.54, 23.2, 123.4, 59, 990.99, 499, 149.6, 789.45, 456.3, 55]
for price in sorted(prices)[::-1][:5]:
    rub = int(price)
    kk = (price - int(price)) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')   # вывод 5 самых дорогих товаров
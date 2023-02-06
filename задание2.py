a = int(input('Введите количество элементов: '))
temp = []
for i in range(a):
    chisla = int(input('Введите числа: '))
    temp.append(chisla)
print(f'Введенные числа: {temp}')

items = temp
n = int(input('Введите число, которое хотите найти: '))
 
def nearest_value(items, n):
    found = items[0]
    for item in items:      
        if abs(item - n) < abs(found - n):
            found = item 
    return found 
 
print(f'Ближайшее число к {n} в списке {items} является: {nearest_value(items, n)}')


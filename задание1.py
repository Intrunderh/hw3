spisok = [int(i) for i in input('Заполните список: ').split()]
chislo = int(input('Введите число, которое хотите посчитать: '))
print('Количество вхождений числа:', spisok.count(chislo))
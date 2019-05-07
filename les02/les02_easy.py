# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruit = ['banana', 'apple', 'melon', 'watermelon', 'lemon', 'orange', 'cherry', 'pineapple']
x = 0
while x < len(fruit) :
    print(x+1, '{0:>10}'.format(fruit[x]))
    x += 1


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


list1 = ['True detective','Game of thrones', 'Breaking bad', 'Preason break', 'Friends']
list2 = ['Black mirror','Game of thrones', 'Big bang theory', 'Method', 'Friends']

result = list(set(list1) & set(list2))
print(result)

for f in result:
    list1.remove(f)
print(list1)






# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

numbers = [1, 3, 8, 54, 99, 4523, 4, 201, 456, 88552, 41, 7, 33]

new = []
# new.append(numbers[1] / 4 )
# print(new)
# print(len(numbers))

z = 0
while z < len(numbers):
    if numbers[z] % 2 == 0:
        new.append(numbers[z] / 4 )
    else:
        new.append(numbers[z] * 2 )
    z += 1
print(new)
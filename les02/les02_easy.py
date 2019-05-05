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

# fruit = ['banana', 'apple', 'melon', 'watermelon', 'lemon', 'orange', 'cherry', 'pineapple']
# x = 0
# while x < len(fruit) :
#     print(x+1, '{0:>10}'.format(fruit[x]))
#     x += 1


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list1 = ['True detective','Game of thrones', 'Breaking bad', 'Preason break', 'Friends']
list2 = ['Black mirror','Game of thrones', 'Big bang theory', 'Method', 'Friends']

result = list(set(list1) & set(list2))
print(result)
# y = 0
# while y < len(result):
#     list1.remove(y)
#     i =+ 1
#
# print(list1)






# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
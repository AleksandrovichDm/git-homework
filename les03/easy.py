# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

# def people(name, age, city):
#     print(name, ', ', age, 'ears old, ', 'live in ', city)
#
# name = input('What is your name?')
# age = input('How old are you?')
# city = input('Where do you live?')
#
# people(name, age, city)


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

# def numbers (x, y, z):
#     print(max(x, y, z))
#
# n1 = float(input('Input first number:'))
# n2 = float(input('Input second number:'))
# n3 = float(input('Input third number:'))
# numbers(n1, n2, n3)


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def text (*args):
    return max(map(len, args))

data = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(text(data))
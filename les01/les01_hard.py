# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

print('Hello!')
name = input('Please, enter your name: ')
surname = input('Please, enter your surname: ')
age =  int( input('Enter your age: '))
weight =  int( input('Enter your weight: '))

if age < 30 and weight > 50 and weight < 120 :
    print(name, surname, ',',  age, ' ears old, ', 'weight ', weight, ' - good condition')
elif  age >= 30 and age <= 40 and weight <= 50 or weight >= 120 :
    print(name, surname, ',', age, ' ears old, ', 'weight ', weight, ' - should lead the right way of life')
elif  age > 40 and age <= 80 and weight <= 50 or weight >= 120 :
    print(name, surname, ',', age, ' ears old, ', 'weight ', weight, ' - should see a doctor')
elif  age > 80 and weight <= 50 or weight >= 120 :
    print(name, surname, ',', age, ' ears old, ', 'weight ', weight, ' - are you still alive?')
else:
    print('Another answer')
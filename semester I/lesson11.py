string = input() + ' '

space = string.find(' ')

word = string[:space]
new_string = string[space+1:]

'''
>
<
>=
<=
!=
==
'''
# print(string.count(' '))
for i in range(string.count(' ')):
    space = new_string.find(' ')
    if len(new_string[:space]) >= len(word):
        word = new_string[:space]
    new_string = new_string[space+1:]

print(f'The longest word is {word}')

# a = 'abc, @GGnc, @ahc'

# list_a = a.split(', ')

# print(len(list_a))

# # print(len(a))
# students = ['Anna', 'Dmytro', 'Serhii', 'Ivan']

# students.pop()

# print(students)

# currencies = {
#     'USD': 36.42,
#     'EUR': 39.03,
#     'GBP': 43.84
# }

# currencies['PLN'] = 8.18
# currencies['USD'] = 39
# currencies['EUR'] = 41
# currencies['GBP'] = 44
# currencies['CNY'] = 5.3
# currencies['CZK'] = 1.6
# currencies['TRY'] = 1.93

# print(currencies)

# currency = input('Enter the currency you would like to exchange: ')

# if currency not in currencies.keys():
#     print('We don\'t support such currency')
# else:
#     amount = float(input('How much money you would like to exchange: '))
#     result = round(amount*currencies[currency], 2) 
#     print('Here is your {} UAH'.format(result))


# numbers = {
#     "one": 1,
#     "two": 2,
#     "three": 3
# }

# for i in numbers:
#     print(i)

# for i in numbers.keys():
#     print(i)

# for i in numbers.values():
#     print(i)

# print(numbers.items())

# for key, value in numbers.items():
#     print(key, value)

# for key in numbers.keys():
#     numbers[key] = numbers[key]*2

# print(numbers)

# transport = {
#     'AA1111AA': 'Іванов Іван',
#     'IVANOV'  : 'Іванов Іван',
#     'AA0007AA': 'Семенов Андрій',
#     'AA007AA' : 'Іванов Іван',
#     'AВ1111AВ': 'Вінниця Водоканал',
#     'AІ1010КК': 'Семенов Андрій',
# }

# transport['II6767AO'] = 'Петренко Петро'
# transport['CA8888CE'] = 'Іванов Олексій'

# car_plate = input('Enter the plate to find car owner: ')

# car_owner = transport.get(car_plate, 'Not found')
# print('Car owner of plate {} is {}'.format(car_plate, car_owner))

# car_owners = dict()

# # {'Ivanov': 1, 'Petrov': 2}

# for owner in transport.values():
#     if car_owners.get(owner, 0) == 0:
#         car_owners[owner] = 1
#     else:
#         auto_count = car_owners[owner]
#         auto_count += 1
#         car_owners[owner] = auto_count

# for owner, auto_count in car_owners.items():
#     if auto_count > 1:
#         print(f'Owner {owner} has {auto_count} cars.')
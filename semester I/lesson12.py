# grades = {
#     "Dmytro": 2,
#     "Anna": 5,
#     "Mykyta": 3,
#     "Andrii": 4
# }

# good_grades = dict()

# for student_name, grade in grades.items():
#     if grade >= 4:
#         good_grades[student_name] = grade

# print(good_grades)



# forecast = {
#     "Kyiv": 25,
#     "Cherkasy": 27,
#     "Odessa": 30,
#     "Donetsk": 26
# }

# total_temperature = 0
# count = 0

# for temp in forecast.values():
#     total_temperature += temp
#     count += 1

# result = total_temperature/count
# print(f'Avg of temperatures = {result}')

# for key in forecast.keys():
#     print(forecast[key])

# forecast = [
#     {"Kyiv": 25},
#     {"Cherkasy": 27},
#     {"Odessa": 30},
#     {"Donetsk": 26}
# ]

# for dict in forecast:
#     for key in dict:
#         print(dict[key])


# numbers = [1, 2, 3]

# print(5 in numbers)

# password = '1244143querTy'

# if '123' in password or 'querty' in password:
#     print('This password is too weak')
# else:
#     print('Ok')

# prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23}
# print(3 in prime_numbers)

# user = {
#     "name": "Bill",
#     "surname": "Bosh",
#     # "age": 22
# }

# if "age" in user.keys():
#     print(f'User {user["name"]}, age - {user["age"]}')
# else:
#     print(f'{user["name"]}, {user["surname"]}')

# password = input('Enter your password: ')
# print(len(password))
# if len(password) < 8:
#     print('The password is too short')
# else:
#     print('ok')

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for i in alphabet:
#     print(i)

# clients = [
#     ['White House', 'Іванов', 3],
#     ['Shelter', 'Іванова', 5], 
#     ['Верховина', 'Іванова', 5], 
#     ['Буковель', 'Іванова', 5],
#     ['Shelter', 'Іванова', 7]
# ]

# hotels = dict()

# # {
# #   'White House': 3
# # }

# for voucher in clients:
#     voucher_hotel = voucher[0]
#     voucher_clients = voucher[2]

#     if hotels.get(voucher_hotel, 0) == 0:
#         hotels[voucher_hotel] = voucher_clients
#     else:
#         # hotel_clients = hotels[voucher_hotel]
#         # hotels[voucher_hotel] = hotel_clients + voucher_clients

#         hotels[voucher_hotel] += voucher_clients


# for hotel, clients in hotels.items():
#     print(f'У готелі {hotel} наразі проживає {clients} клієнтів.')

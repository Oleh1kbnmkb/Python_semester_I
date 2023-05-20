import random


#Завдання_1
#Написати програму, яка буде підраховувати суму всіх непарних чисел від 1 до 100.

# sum = 0
# for number in range(1, 100+1):
#     if number % 2 != 0:
#         print(number)
#         sum += number

# print('sum:', sum)

# Написати програму, яка приймає на вхід рядок, введений з клавіатури, і підраховує кількість входження в рядок першої
# літери, з якої починається цей рядок.
# string = input('Enter your string: ')
# first_char = string[0]
# count = 0
# for char in string:
#     if char == first_char:
#         count += 1

# print(f'Amount of the first letter {first_char} is {count}')

# print(my_list)
# list()

# iterable = list('Python')
# first_element = iterable[0]
# second_element = iterable[1]
# last_element = iterable[-4]
# print(iterable)
# print(first_element)
# print(second_element)
# print(last_element)




# last_element_of_second_list = my_list[2][2][0]
# print(last_element_of_second_list)

# my_list.append(9)
# print(my_list)

# my_list.clear()

# my_list.remove(4)

# my_list.pop(1)

# extension = [[4, 6, 8, 3, 2]]
# my_list.extend(extension)

# my_list.insert(2, 5)



# my_list.sort(reverse=True)

# print(len(my_list))


# copy_list = my_list.copy()

# print(copy_list)


# if 111 in my_list:
#     print('Okay')
# else:
#     print('Bad')

# for element in sorted(my_list):
#     print(element)


# goods = ['Bananas', 'Tomatoes', 'Apples', 'Milk', 'Pineapple', 'Peach', 'Cucumber']
# sold_goods = []

# while True:
#     match = input('Вітаю в системі магазину!\nДля показу всіх товарів натисніть 1.\nДля постачання товарів натисніть 2.\n\
# Для продажу товарів натисніть 3\nДля виводу проданих товарів за день натисніть 4.\nДля перегляду історії продажів натисніть 5.\n\
# Для виходу натисніть 0: ')
#     if match == '0':
#         print('Thank you!')
#         break
#     elif match == '1':
#         for good in goods:
#             print(good)
#     elif match == '2':
#         print('Products delivery')
#         product = input('Enter the product you would like to deliver: ')
#         goods.append(product)
#     elif match == '3':
#         print('Selling products')
#         product = input('Enter the product you would like to buy: ')
#         sold_goods.append(product)
#         goods.remove(product)
#     elif match == '4':
#         for good in sold_goods:
#             print(good)
#     elif match == '5':
#         for i in reversed(sold_goods):
#             print(i)

# a = [['Serhii', 'Petrenko'], ['Andrii', 'Nester']]


# goods.remove('Milk')
# print(goods)



# my_list = [1, 66, 8, 30, 2, 2, 2]
# a = 1

# for element in my_list:
#     a *= element

# print(a)

# max = 0

# for element in my_list:
#     if element > max:
#         max = element

# print(max(my_list))
    
# my_list = ['abc', 'xyz', 'aba', '1221']

# count = 0

# for element in my_list:
#     if len(element) >= 2 and element[0] == element[-1]:
#         print(element)
#         count += 1

# print(count)

# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]

# result = False

# for i in list1:
#     for j in list2:
#         if i == j:
#             result = True
#             break

# print(result)


# random_number = random.randint(0, 5)

# while True:
#     guess = int(input('Try to guess the number from 0 to 5: '))
#     if guess == random_number:
#         print('You are right!')
#         break
#     else:
#         print('Please try again!')

# my_list = [1, 3, 7, 8, 2, 9, 4, 21, 7, 2, [3, 4, 7, 3, 1, 3, 6, 8, 0]]
# for element in my_list:
#     if type(element) == list:
#         element.sort()

# tmp = my_list[-1]
# my_list.pop(-1)

# my_list.sort()
# my_list.extend([tmp])

# print(my_list)
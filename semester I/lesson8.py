# a = "bebebe" * 10

# print(a)

# b = 'bebebebebebebebebebebebebebebe\nbebebe bebebebebebebebebebebebe'
# print(b)

# print(b.count('be',3, 10))

# c = 'BBBBBBBBBBBBBBBBBBBBBBbb'
# print(c.lower())

# print(b.upper())

# print(b.title())

# print(b.capitalize())

# print(c.swapcase())

# '''4'''

# '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada, est vitae suscipit vestibulum,'''

# my_string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada, est vitae suscipit vestibulum,'
# n = int(input())


# if n > len(my_string):
#     print('Wrong input!')
# else:
#     new_string = my_string[n:]
#     print(new_string)


# s = "I am learning strings in Python. Some new methods got now."
# sentences = s.split('. ')
# sentences.pop(-1)

# print(sentences)

# a = input('Enter the sting: ')
# print(f'Symbols - {len(a)}')
# b = a.split()
# print(b)
# print(f'Words - {len(b)}')

# sentences = ["I am learning strings in Python", "Some new methods got now."]
# text = '. '.join(sentences)

# print(text)


# clean = '   spacious;   '.strip()
# print(clean)

# dog_text = "All dogs bark like dogs."
# print(dog_text)
# cat_text = dog_text.replace('dogs', 'cats')
# print(cat_text)

# map = {
#     ord('з'): 'z',
#     ord('ю'): 'u',
#     ord('а'): 'A'
# }

# translated = 'з'.translate(map)

# print(translated)


# s = 'Мене звати %s. Мені %d років.' % ('Олег', 14)
# print(s)

# s = 'Мене звати {0}. Мені {1} років.'.format('Oleg', 14)
# print(s)

# name = 'Олег'
# age = 14
# s = f"Мене звати {name}. Мені {age} років."
# print(s)

# print('pi: {:0.6}'.format(3.1415926))

# print(' "{}" "{:+}" "{:-}" "{: }" '.format(1, 2, -3, 4))


# print("|{:<10}|{:-^10}|{:>10}|".format('left', 'center', 'right'))

# delimiter = '-' * 80
# goods = [['Апельсин', 6, 150], ['Лимон', 8, 90], ['Картопля', 123, 445]]
# total_sum = 0
# number = 0

# print(delimiter)
# print("|{:^5}|{:<40}|{:>15}| {:>14}|".format('#', 'Товар', "Кількість", "Вартість"))
# print(delimiter)

# for good in goods:
#     name = good[0]
#     amount = good[1]
#     money = good[2]
#     number += 1
#     total_sum += money
#     print("|{:^5}|{:<40}|{:>15}|{:>15}|".format(number, name, amount, money))

# print(delimiter)
# print("|{:<62}|{:>15}|".format(' Total:', total_sum))
# print(delimiter)
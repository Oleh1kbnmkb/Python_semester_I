# west = ['South America', 'North America', 'Antarctica']


# west.extend(['Eurasia', 'Africa', 'Australia'])

# west.sort()

# print(west)


# my_list = [['Andrii', 'Petrenko'], ['Andrii', 'Ivanov'], ['Andrii', 'Nesterenko'], ['Yaroslav', 'Polischuk']]

# count = 0

# for element in my_list:
#     if element[0] == 'Andrii':
#         count += 1

# print(count)


# a = 'My_awesome_string'
# b = "My_awesome_string"
# song = '''Jingle bells, jingle bells
# Jingle all the way
# Oh, what fun it is to ride
# In a one horse open sleigh'''

# one_line_text = "Textual data in Python is handled with str objects, or strings."\
#     "Strings are immutable sequences of Unicode code points."\
#     "String literals are written in a variety of ways: single quotes, double quotes, triple quoted."


# print(one_line_text)

# an integer to a string
# s = str(15)
# print(type(s))

# a list to a string
# s = str([12, 11])
# print(type(s))


# ------------------------

# s = 'ABCDEFGHI'
# first_element = s[0]
# last_element = s[-1]
# e = s[4]

# # -------------------------

# s = 'abcdefghijk'


# print(s[3:6])

# print(s[:6])

# print(s[3:])

# print(s[::-1])

# is_palindrome = 'otto'

# if is_palindrome == is_palindrome[::-1]:
#     print(True)
# else:
#     print(False)


# print(s[:-5])
# print(s[-1:-6:-2])

# my_list = [1, 2, 3]

# my_list[0] = 4

# print(my_list)


# s = 'abcdefghijk'

# s[0] = 'z'

# a = 'Hello, '
# b = 'World'

# print(a+b)

# delimiter = '-' * 25
# print(len(delimiter))

# a = 'Jingle bells, jingle bells Jingle all the way Oh, what fun it is to ride In a one horse open sleigh'

# for char in a:
#     print(char)

# l = 'hellO, worlD!'
# print(l.lower())
# print(l.upper())
# print(l.capitalize())
# print(l.swapcase())
# print(l.title())


# s = "Hi there!"
# start = 0
# end = 5

# print(s.find('er', 0, 7))
# print(s.find('i'))


# e = 'Big, Bigger, Biggest'
# x = e.rfind('Big')
# print(x)

# stop_words = ['купити', 'продати', 'реклама']

# user_string = input()

# for stop_word in stop_words:
#     if user_string.find(stop_word) != -1:
#         print('It is spam message!')
#         break
# else:
#     print('It is not spam')
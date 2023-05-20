# old_string = 'Hello everrry booooooooooooody jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj'

# space = old_string.find(' ')

# if space == -1:
#     print('Word -', old_string)
# else:
#     word = old_string[:space]

#     while True:
#         new_space = old_string.find(' ', space+1)
#         new_word = old_string[space+1:new_space]
#         if len(word) < len(new_word):
#             word = new_word
#             new_string = old_string[space+1:]
#         if len(new_string.split()) == 0:
#             break
#         space = new_space
#         old_string = old_string[space+1:]
# print(word)

# a = dict()

# print(type(a))

# months = {
#     1: 'January',
#     2: 'February',
#     3: 'March',
#     4: 'April',
#     5: 'May'
# }


# # print(months)
# currencies = {
#     'USD': 36.42,
#     'EUR': 39.03,
#     'GBP': 43.84
# }

# # print(currencies.get('PLN', 'Current currency does not exist'))
# # print(currencies['PLN'])

# months[6] = 'June'
# months[7] = 'July'
# months[8] = 'August'
# months[9] = 'September'

# # print(len(months), months)

# # a = months.pop(3)
# # months.pop(4)
# # months.pop(5)


# # months.clear()

# months.update({10: 'October', 11: 'November'})
# months.update({12: 'December'})


# print(months)


# monthes = {
#     1:  'січень',
#     2:  'лютий',
#     3:  'березень',
#     4:  'квітень',
#     5:  'травень',
#     6:  'червень',
#     7:  'липень',
#     8:  'серпень',
#     9:  'вересень',
#     10: 'жовтень',
#     11: 'листтопад',
#     12: 'грудень'
# }


# report_date = '21.11.2022'

# month = int(report_date[3:5])

# month_name = monthes.get(month)

# print('Report from', month_name)
# booking_book = {}

# def booking(clients_name, amount=2):
#     booking_book[clients_name] = amount
#     print(f'Client {clients_name}, booked {amount}-places table.')


# booking('Vysotskyi')
# booking('Petrenko', 4)

# print(booking_book)


# x = 10

# def func(x):
#     global x
#     x = 2
#     print(x)

# print(x)
# func(2)
# print(x)

# def func(a, b=10, c=2):
#     c += a + b
#     return c

# result = func(10)
# result += func(2, 5)

# print(result)

# def func(a, *b):
#     print(b)
#     print(sum(b)+a)


# func(10, 1,2,3,4)

# {"a": 5}

# def func(a, **b):
#     sum = 0
#     for key in b:
#         sum += b[key]
#     print(sum)

# func(10, k=1, n=2, l=3, m=4)

# import math
# print(math.pow(2, 2))

# print(16**0.5)


# import math

# def func(a, b):
#     c = math.sqrt(a**2 + b**2)
#     # c = (a**2 + b**2)**0.5
#     return c

# print(func(3,4))


# def get_value_from_dict(dict, key):
#     return dict.get()

# a = {"name": 'Petro', "age": 15, "is_adult": False}

# result = get_value_from_dict(a, "date_of_birth")
# print(result)
# a = 'fjfkfkfkfkfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'

# b = list(a)

# some_str = "This is awesome string"
# print(some_str[0:5]+'aaa')



# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# [3, 6, 9]

# even_numbers = numbers[1:-1:2]
# odd_numbers = numbers[0:-1:2]
# l = numbers[2:-1:3]

# print(even_numbers)
# print(odd_numbers)
# print(l)


'''
a[start:stop]  	# items start through stop-1
a[start:]     	 # items start through the rest of the array
a[:stop]       	# items from the beginning through stop-1
a[:]           	# a copy of the whole array
a[-1]    		# last item in the array
a[-2:]   		# last two items in the array
a[:-2]   		# everything except the last two items
a[::-1]         # reversed string
'''


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print(numbers[0:6])
# print(numbers[6:])
# print(numbers[:6])

# b = numbers.copy()
# c = numbers[:]

# print(numbers[-2:])
# print(numbers[:-2])

# print(numbers[::-1])

# a = numbers[1:3]
# print(a)

# a = set('hello')

# a = '067'
# print(int(a))

# b = {1, 2, 3}
# print(b)

# c = {'067', '068', '066', '099', '099'}

# print(c)


# numbers = {1, 2, 3}
# numbers.add(4)
# numbers.remove(3)
# numbers.discard(6)
# print(numbers)


a = set('hello') 
b = set('hi there!')

# print(a)
# print(b)

# print(a ^ b)    
# print(a | b)
# print(a.union(b))

# print(a & b)
# print(a.intersection(b))

'''
Дано список клієнтів, які купили товар А та список клієнтів, які купили товар В.
*Знайти:*
клієнтів, які купили обидва товари А і B
створити один список клієнтів, шляхом операції об’єднання
вивести результати на екран
'''

# customers_A = {'Ivanov', 'Petrov', 'Sidorov'}
# customers_B = {'Ivanova', 'Petrova', 'Sidorov'}

# customers_A_B = customers_A & customers_B
# print(customers_A_B)

# all_customers = customers_A | customers_B
# print(all_customers)

# print(sorted(all_customers))
# all_customers = customers_A.union(customers_B)



# # first set
# A = {1, 3, 4, 5}

# # second set
# B = {0, 1, 2, 4, 4}

# print('Intersection using &:', A & B)
# print('Intersection using intersection():', A.intersection(B)) 


# print('Union using | :', A | B)
# print('Union using .union():', A.union(B))


# # first set
# A = {2, 3, 5}

# # second set
# B = {1, 2, 6}

# # # perform difference operation using -
# # print('Difference using -:', B - A)

# # # perform difference operation using difference()
# # print('Difference using difference():', B.difference(A)) 

# # perform difference operation using ^
# print('using ^:', A ^ B)

# # using symmetric_difference()
# print('using symmetric_difference():', A.symmetric_difference(B)) 


# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5}

# print(B.issubset(A))


# [5,4,3,2,1]
number = int(input('Enter the number: '))

print(type(number),number)

a = str(number)

print(type(a), a)

b = a[::-1]

print(type(b), b)

pre_result = list(b)

# print(type(pre_result), pre_result)

# for i in range(0, len(pre_result)):
#     pre_result[i] = int(pre_result[i])


# for i in pre_result:
#     int(i)
# print(pre_result)

# result = [int(i) for i in pre_result]

# f = [i for i in range(5)]

# print(f)
# print(result)


# f = []
# for i in range(5):
#     f.append(i)

# print(f)

# f = [i for i in range(5)]
# print(f)


# a = 'My awesome string'

# space = a.find(' ')
# print(space)

# first_word = a[0:space]
# print(len(first_word), first_word)
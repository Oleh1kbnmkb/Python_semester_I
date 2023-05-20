# surname = input('Enter your surname: ')
# counter = dict()

# for char in surname:
#     counter[char] = surname.count(char)

# most_common = max(list(counter.items()), key=lambda x: x[1])

# print(most_common[0])


# text = input('Enter: ')

# for char in text:
#     if char.isdigit():
#         text = text.replace(char, '')


# print(text)


# def convert(a):
#     return 'Yes' if a else 'No'

# print(convert(False))


# def reverse(a):
#     a = str(a)
#     return list(a[::-1])

# print(reverse(123))
# [3, 2, 1]


# def game(player1,player2): 
#     scisors = 'scisors' 
#     stone = 'stone' 
#     paper = 'paper' 
 
#     if player1 == player2: 
#         print('draw') 
#     elif player1 == scisors and player2 == stone: 
#          print('player2 is won') 
#     elif player1 == stone and player2 == scisors: 
#          print('player1 is won')     
#     elif player1 == paper and player2 == stone: 
#          print('player1 is won')     
#     elif player1 == stone and player2 == paper: 
#          print('player2 is won') 
#     elif player1 == scisors and player2 == paper: 
#          print('player1 is won')  
#     elif player1 == paper and player2 == scisors: 
#          print('player2 is won')     
 
# game('stone' , 'scisors')
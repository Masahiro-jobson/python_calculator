# character_name = "John"
# character_age = 50
# isMale = True
# print("There once was a man named " + character_name + ",")
# print("he was " + str(character_age) + " old.")
#
#
# character_name = "Tom"
# character_age = "50"
# print("He really liked the name " + character_name)
# print("but didn't like being " + character_age + ".")

# phrase = "Masa \" Academy"
# print(phrase.replace("Masa", "Giraffe"))

#math is module and imported for round, floor, celi, and sqrt function
from math import*
# print(-2.097)
# print(3 + 4.5)
# print(3 * 4.5 + 5)
# print(3 * (4.5 + 5))
# print(10 % 3)

# my_num = -5
# print(round(3.5))
# print(floor(3.5))
# print(ceil(3.5))
# print(sqrt(25))
#

# #input from someone
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "!")
# print("Hello " + age + "!")

#Basic calculator
# num1 = input ("Enter a number:")
# num2 = input ("Enter another number:")
# result = float(num1) + float(num2)
# print (result)

#Mad Libs Game
# color = input("Enter a color: ")
# plural_noun = input("Enter a a plural noun:")
# celebrity = input("Enter a celebrity:")
#
# print("Roses are " + color)
# print( plural_noun + " are blue")
# print("I love " +  celebrity)

# List
friends = ["Kevin", 2, False, "Karen", "Jim"]
# friends[1] = "Michael"
# print(friends[0])
# print(friends[1:3])
# print(friends[1:])

# List Function
# lucky_numbers = [4, 8, 15, 16, 23, 42]
# friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Toby"]
# friends.append("Jack")
# friends.extend(lucky_numbers)
# friends.insert(0, "Jobson")
# friends.remove("Oscar")
# friends.pop()
# print(friends)
# friends.clear()
# print(friends)
# print(friends.index("Karen"))
# print(friends.count("Jim"))
# lucky_numbers.sort()
# print(lucky_numbers)
# lucky_numbers.reverse()
# print(lucky_numbers)

# friends2 = friends.copy()
# print(friends2)

# tuples
# tuple is immutable, which means it can't be changed and modified.
# And it's only one specified type, while list can have any types of elements.
# coordinates = (4, 5)
# coordinates [1] = 10
# print (coordinates[0])

# functions
# it's a collection of code which executes a specific task.
# def say_hi(name, age ):
#     print("Hello " + name + " you are " + str(age))

# print("Top")
# sayhi()
# print("Bottom")

# say_hi("Jack",35)
# say_hi("Kevin",49)

# Return Statement
# def cube(num):
#     return num*num*num
#
# result = cube(4)
# print(result)

# If statements
# is_male = True
# is_tall = False
#
# if is_male or is_tall:
#     print("You are a male or tall or both")
# elif is_male and not (is_tall):
#     print("You are a short male")
# elif not(is_male) and (is_tall):
#     print("You are not a male but are tall")
# else:
#     print("You are not a male and not tall")
#

# If statements & comparison operator
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(300,4,5))




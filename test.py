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

# Dictionary
# monthConversions = {
#     # left value is called "key"
#     # We can use number for key too.
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
# }
#
# print(monthConversions.get("Luv", "Not a valid key"))

# While loop
# i = 0
# while i<=10:
#     print(i)
#     i += 1
# print("Done with loop")

# secret_word = "Lion"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not (out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print ("Out of Guesses, YOU LOSE!")
# else:
#     print("YOU WIN!")

#For loop
# friends = ["Jim", "Karen", "Kevin"]
# len(friends)
# for index in range(5):
#     if index == 0:
#         print("First Iteration")
#     else:
#         print("Not First")

# Exponent Function
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
# print(raise_to_power(3, 2))

# 2D list and Nested lo0p
# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
#
# for row in number_grid:
#     for col in row:
#         print(col)
#
# print(number_grid[2][1])

# Basic Translator
# Lion language
# Vowels -> g
# ----------------
#
# dog -> dgg
# cat -> cgt

# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
#
# print(translate(input("Enter a phrase: ")))

# Try Except
# To protect the program
# ZeroDivisionError and ValueError is built-in excepetion class
# They make exception class which is stored in variable after "as" statement.
# try:
#     answer = 10/0
#     number = int(input("Enter a number: "))
#     print(number)
# # err ("as" showed) is variable which contains ZeroDivisionError class
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Invalid Input")

# Reading files from imported file.
# r is read, w is write, a is append (add), r+ is read and write
# test_file = open("test.txt", "r")
# for test in test_file.readlines():
# readable is function which returns boolean value
# print(test_file.read())
# print(test_file.readline())
# print(test_file.readlines()
# print(test_file.readlines()[1])
#     print(test)
#     test_file.close()

# Write files
# employee_file = open ("index.html", "w")
#
# employee_file.write("<p>This is HTML</p>")
# employee_file.close()

# Modules and Piles
# Pip is package manager

# Classes and Objects

# Building MCQ quiz

# Object functions

# MCQ quiz with Class and object difinition

# Inheritance
# region first code
# print("Hello World!")
# endregion


# region drawing a shape
# print("   /|      -----")
# print("  / |     |     |")
# print(" /  |     |     |")
# print("/___|      -----")
# endregion


# region variables & datatypes
# character_name = "omar"
# character_age = "21"
# num = 20
# num2 = 20.123
# boo = True
# print(num)
# print("hello i am " + character_name + " i am " + character_age)
# endregion


# region working with string
# print("Omar \nnew line")
# print("Omar \"quotation mark\"")
#
# phrase = "My name is omar"
# print(phrase.lower())
# print(phrase.upper())
# print(phrase.isupper())
# print(phrase.upper().isupper())
# print(len(phrase))
# print(phrase[0])
# print(phrase.index("a"))
# print(phrase.index("om"))
# print((phrase.replace("omar", "khaled")))
# endregion


# region working with numbers
# print(2)
# print(2.123)
# print(2 + 3)
# print(2 * (3 + 2))
# print(10 % 3)
#
# my_num = 5
# print(my_num)
# print(str(my_num) + " my number")
#
# my_num = -5
# print(abs(my_num))
#
# print(pow(3, 2))
# print(max(4, 6))
# print(min(4, 6))
# print(round(3.4))
#
# from math import *
# print(floor(3.7))
# print(ceil(3.4))
# print(sqrt(36))
# endregion


# region getting input from users
# name = input("Enter yor Name: ")
# age = input("Enter your age: ")
# print("hello " + name + " your age is " + age)
# endregion


# region building basic calculator
# num1 = input("Enter the first number ")
# num2 = input("Enter the second number ")
# result = float(num1) + float(num2)
# print(result)
# endregion


# region lists
# friends = ["ahmed", "ibrahim", "maghraby", "eid", 4, True]
# print(friends)
# print(friends[0])
# print(friends[-1])
# print(friends[1:])
# print(friends[1:3])
#
# friends[4] = 5
# print(friends)
# endregion


# region list functions
# people = ["hesham", "safi"]
# friends = ["ahmed", "ibrahim", "maghraby", "eid"]
#
# friends.extend(people)
# print(friends)
#
# friends.append("eslam")
# print(friends)
#
# friends.insert(1, "eid")
# print(friends)
#
# friends.remove("eslam")
# print(friends)
#
# friends.pop()
# print(friends)
#
# print(friends.index("ibrahim"))
#
# print(friends.count("eid"))
#
# friends.sort()
# print(friends)
#
# friends.reverse()
# print(friends)
#
# friends2 = friends.copy()
# print(friends2)
#
# friends.clear()
# print(friends)
# endregion


# region tuple
# coordinates = (4, 5)
# print(coordinates[1])
#
# coordinates2 = [(4, 5), (6, 7), (7, 8)]
# print(coordinates2)
# endregion


# region functions
# def my_func():
#     print("Hello User")
#
#
# def my_func2(name, age):
#     print("hello " + name + "you are " + str(age))
#
#
# my_func()
# my_func2("omar", 21)
# endregion


# region return statement
# def cube(num):
#     return num * num * num
#
#
# result = cube(3)
# print(result)
# endregion


# region if statement
# is_male = True
# is_tall = True
#
# if is_male and is_tall:
#     print(1)
# elif is_male and not is_tall:
#     print(2)
# elif not is_tall and is_tall:
#     print(3)
# else:
#     print(4)
# endregion


# region if statement & comparisons
# def max_num(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     else:
#         return num3
#
#
# print(max_num(1, 2, 3))
# endregion


# region building a better calculator
# num1 = float(input("Enter the first number: "))
# op = input("Enter the operator: ")
# num2 = float(input("Enter the second number: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "*":
#     print(num1 * num2)
# elif op == "/":
#     print(num1 / num2)
# else:
#     print("Enter a valid operator")
# endregion


# region dictionary
# monthConversion = {
#     "jan": "january",
#     "feb": "february",
#     "mar": "march",
#     4: "april"
# }
#
# print(monthConversion["jan"])
# print(monthConversion.get("feb"))
# print(monthConversion.get(4))
# print(monthConversion.get("dec", "NOT valid"))
# endregion


# region while loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# print("finished")
# endregion


# region building guess game
# secret_word = "omar"
# guess_word = ""
# guess_counter = 0
#
# while guess_word != secret_word and guess_counter < 3:
#     guess_word = input("enter guess word: ")
#     guess_counter += 1
#
# if guess_word == "omar":
#     print("you win!")
# else:
#     print("you lose")
# endregion df df


# region for loop
# for letter in "omar reda":
#     print(letter)
#
# print(" ")
# colors = ['red', 'yellow', 'green']
# for color in colors:
#     print(color)
#
# print(" ")
# for num in range(10):
#     print(num)
#
# print(" ")
# for num in range(3, 10):
#     print(num)
#
# print("")
# for num in range(len(colors)):
#     print(num)
#
# print("")
# for num in range(3):
#     if num == 0:
#         print("1st iteration")
#     else:
#         print("not 1st iteration")
# endregion


# region exponent functon
# print(2 ** 4)
#
#
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
#
# print(raise_to_power(2, 3))
# endregion


# region 2D lists & nested loops
# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# print(number_grid[1][2])
#
# for row in number_grid:
#     for col in row:
#         print(col)
# endregion


# region build a translator
# def translator(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "M"
#             else:
#                 translation = translation + "m"
#
#         else:
#             translation += letter
#     return translation
#
#
# print(translator(input("Enter a phrase: ")))
# endregion


# region try except
# try:
#     number = int(input("enter a number: "))
#     number2 = 10/number
#     print(number)
# except ValueError:
#     print("Enter a valid number")
# except ZeroDivisionError as err:
#     print(err)
# endregion


# region reading files
# employee_file = open("employees.txt", "r")
#
# # print(employee_file.readable())
# # print(employee_file.read())
#
# # print(employee_file.readline())
# # print(employee_file.readline())
# # print(employee_file.readline())
#
# # print(employee_file.readlines())
#
# # print(employee_file.readlines()[0])
#
# for employee in employee_file.readlines():
#     print(employee)
# employee_file.close()
# endregion


# region writing files
# # employee_file = open("employees.txt", "a")
# # employee_file.write("\nemp5 - data analyst")
#
# # employee_file = open("employees.txt", "w")
# # employee_file.write("emp5 - data analyst")
#
# # employee_file = open("index.html", "w")
# # employee_file.write("<p> hi </p>")
#
# employee_file.close()
# endregion


# region modules & pipe
# import useful_tools
# print(useful_tools.test(2))
# endregion


# region classes and objects
# from student import Student
# student1 = Student("omar", "CS", 3.3, False)
# student2 = Student("std", "Art", 3.1, False)
#
# print(student1.name)
# print(student2.major)
# endregion


# region building a multiple choice quiz
# from question import Question
#
# question_prompts = [
#     "What color are Apples?\n (a) Red\n (b) Purple\n (c) Orange\n\n",
#     "What color are Bananas?\n (a) Teal\n (b) Magenta\n (c) Yellow\n\n",
#     "What color are Strawberries?\n (a) Yellow\n (b) Red\n (c) Blue\n\n"
# ]
#
# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b")
# ]
#
#
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt + "your answer: ")
#         if answer == question.answer:
#             score += 1
#     print("you got " + str(score) + "/" + str(len(questions)) + " correct")
#
#
# run_test((questions))
# endregion


# region object functions
# from student import Student
#
# std1 = Student("Omar", 'CS', 3.1, False)
# std2 = Student("Khaled", 'M', 3.8, False)
#
# print(std1.on_honor_roll())
# print(std2.on_honor_roll())
# endregion


# region inheritance
# from chef import Chef
# from chinesChef import ChinesChef
#
# my_chef = Chef()
# my_chines_chef = ChinesChef()
#
# my_chef.make_chicken()
# my_chef.make_special_dish()
#
# my_chines_chef.make_fried_rice()
# my_chines_chef.make_special_dish()
# endregion

### LIST COMPREHENSION ###

# # new_list = [new_item for item in list]
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)     # prints '2, 3, 4'

# # adding an 'if' test at the end...
# names = ['Dave', 'Jon', 'Peter', 'Gerald', 'Stavros', 'Glen']
# # print(names)
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# # print the longer (>5 letter) names in UPPERCASE
# capit_names = [name.upper() for name in names if len(name) > 5]
# print(capit_names)

"""Exercise 1"""

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆

# #Write your 1 line code 👇 below:

# squared_nums = [n**2 for n in numbers]

# #Write your code 👆 above:

# print(squared_nums)

"""Exercise 2"""

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above

# #Write your 1 line code 👇 below:

# result = [num for num in numbers if num % 2 == 0]

# #Write your code 👆 above:

# print(result)

"""Exercise 3"""
### loops through and compares 2 lists for common variables ###

# with open("100Days\day26_listcomprehension/file1.txt") as f1:
#     nums1 = f1.readlines()

# with open("100Days\day26_listcomprehension/file2.txt") as f2:
#     nums2 = f2.readlines()

# result = [int(num) for num in nums1 if num in nums2]

# print(result)

""" Dictionary comprehension """

# names = ['Nick', 'Gerald', 'Steve', 'Gene', 'Peter', 'Harold']
# # scores = ['90', '87', '75', '95', '80', '78']

# import random

# #  student_scores = {new_key:new_value for item in list}
# student_scores = {student:random.randint(1,100) for student in names}
# print(f"All scores: {student_scores}")

# passed_students = {student:score for (student, score) in student_scores.items() if score > 80}
# print(f"Passed: {passed_students}")


""" Exercise 4 """
### Count the letters of each word in the sentence ###

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

words = sentence.split()        # creates a list of words in the sentence
result = {word:len(word) for word in words}     # create the new dictionary with each word and the length of each word

### OR ###
result = {word:len(word) for word in sentence.split()}

print(result)



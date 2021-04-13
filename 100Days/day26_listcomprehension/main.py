# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

from typing import NewType
import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

df = pandas.read_csv("100Days\day26_listcomprehension/nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in the format: {"A": "Alfa", "B": "Bravo"}

# create 'nato_dict' by iterating through each row in 'df', assigning key:value pairs to each 'row.letter' & 'row.code'...
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}
# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_input = input("Enter a word to convert:\n").upper()
# for each letter in the input word, give it the value from the corresponding letter in the 'nato_dict'...
output_list = [nato_dict[letter] for letter in word_input]

print(output_list)
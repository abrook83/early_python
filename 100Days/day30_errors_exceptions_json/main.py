from typing import NewType
import pandas

df = pandas.read_csv("100Days\day26_listcomprehension/nato_phonetic_alphabet.csv")

# create 'nato_dict' by iterating through each row in 'df', assigning key:value pairs to each 'row.letter' & 'row.code'...
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

def code():
    word_input = input("Enter a word to convert:\n").upper()
    # for each letter in the input word, give it the value from the corresponding letter in the 'nato_dict'...
    try:
        output_list = [nato_dict[letter] for letter in word_input]
    except KeyError:
        print("Whoops, enter only alphabet characters...")
        code()      # in the case of an exception, just restart the function!
    else:
        print(output_list)

code()
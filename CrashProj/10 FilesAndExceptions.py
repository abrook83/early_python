#     ### Reading files

# filename = 'CrashProj/pi_digits.txt'        # assign a variable to the file name

# # with open (filename) as file_object:         # 'with open' opens the file to perform the function...
# #     contents = file_object.read()            # ...then closes the file as the code block completes.
# # print(contents)

# ### 'with' & 'open' closes the file at the end of the block

# # print("\n")

# # with open (filename) as file_object:        # use 'with' syntax to open & close the file appropriately
# #     for line in file_object:
# #         print(line.strip())                 # strip (specifically rstrip) to remove newlines within the file's text

# ### '.readlines() retains file data for use later in the program ###

# # print("\n")

# with open (filename) as file_object:
#     lines = file_object.readlines()         # '.readlines' creates a list of the individual lines in the file...  
#                                             # ...the file will have closed, but the data will remain in the list.
# for line in lines:
#     print(line.strip())

# ### Working with a file's contents ### 
# # file opened and data placed into list as above ^^
# print("\n")

# pi_string = ''          # create empty variable 'pi_string'
# for line in lines:
#     pi_string += line.rstrip()      # adds each line from the file to the variable 'pi_string', removing the newline

# print(pi_string)
# print(len(pi_string))


    ### Writing to a file

# file = 'programming.txt'

# # opening a pre-existing file in write mode, will automatically rease the contents of the file.

#                 # the 'open' function creates a file if one does not exist with that name.
# with open (file, 'w') as worktext:      # first argument 'file' is to open 'file', 'w' tells to write to the file.
#     worktext.write("Programming is fun!.... So far.\n")
#     worktext.write("Let's see where this text ends up shall we?\n") # requires newlines for the resultant text.

# with open (file, 'a') as worktext:
#     worktext.write("Now let's 'append' to add another line!\n")


    ### Exceptions

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Sorry, you can't divide by zero!")

print("Give me 2 numbers, I'll divide the first by the second!")
print("Enter 'q' to quit.")

while True:
    first = input("First number: ")
    if first == 'q':
        print("Thanks for comin'")
        break
    second = input("Second number: ")
    if second == 'q':
        print("Thanks for comin'")
        break
    try:
        answer = int(first) / int(second)
        print(f"The answer is {answer}")
    except ZeroDivisionError:
        print("Sorry, you can't divide by zero!") 


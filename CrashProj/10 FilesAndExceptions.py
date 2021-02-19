filename = 'CrashProj/pi_digits.txt'        # assign a variable to the file name

# with open (filename) as file_object:         # 'with open' opens the file to perform the function...
#     contents = file_object.read()            # ...then closes the file as the code block completes.
# print(contents)

### 'with' & 'open' closes the file at the end of the block

# print("\n")

# with open (filename) as file_object:        # use 'with' syntax to open & close the file appropriately
#     for line in file_object:
#         print(line.strip())                 # strip (specifically rstrip) to remove newlines within the file's text

### '.readlines() retains file data for use later in the program ###

# print("\n")

with open (filename) as file_object:
    lines = file_object.readlines()         # '.readlines' creates a list of the individual lines in the file...  
                                            # ...the file will have closed, but the data will remain in the list.
for line in lines:
    print(line.strip())

### Working with a file's contents ### 
# file opened and data placed into list as above ^^
print("\n")

pi_string = ''          # create empty variable 'pi_string
for line in lines:
    pi_string += line.rstrip()      # adds each line from the file to the variable 'pi_string', removing the newline

print(pi_string)
print(len(pi_string))
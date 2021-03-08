### 10.1 Learning Python ###

text = 'CrashProj\Learnings.txt'        # assigns the file to a variable

# 1st print

with open (text) as file_object:        # assigns the opened file as a variable 'file_object'
    contents = file_object.read()       # reads the opened file and assigns it to 'contents'
print(contents)

print("\n")

# 2nd print

with open (text) as file_object:
    for lines in file_object:           # loops through each line in the opened file....
        print(lines.rstrip())           # ...and prints each line with the right stripped to remove newlines.

print("\n")

# 3rd print

with open (text) as file_object:
    lines = file_object.readlines()        # the 'readlines()' method takes the file's contents and makes a list from it

for line in lines:
    print(line.rstrip())

print("\n")

### 10.2 Learning C ###

with open (text) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip().replace('Python','C')        # strip whitespace, then replace the word 'Python' with 'C'
    print(line)

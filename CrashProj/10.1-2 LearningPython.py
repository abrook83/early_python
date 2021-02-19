### 10.1 Learning Python ###

text = 'CrashProj\Learnings.txt'

# 1st print

with open (text) as file_object:
    contents = file_object.read()
print(contents)

print("\n")

# 2nd print

with open (text) as file_object:
    for lines in file_object:
        print(lines.rstrip())

print("\n")

# 3rd print

with open (text) as file_object:
    lines = file_object.readlines()        # 'readlines()' takes the file's contents and makes a list from it

for line in lines:
    print(line.rstrip())

print("\n")

### 10.2 Learning C ###

with open (text) as file_object:
    lines = file_object.readlines()        # 'readlines()' takes the file's contents and makes a list from it

for line in lines:
    line = line.rstrip().replace('Python','C')
    print(line)

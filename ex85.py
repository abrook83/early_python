fname = input("Enter file name: ")
# if the fname length is less than 1 char., then just use this file...
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From "): continue
    count = count + 1
    words = line.split()
    print(words[1])
print("There were", count, "lines in the file with From as the first word")

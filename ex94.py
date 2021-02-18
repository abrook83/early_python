# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages. The program looks for 'From ' lines
# and takes the second word of those lines as the person who sent the mail. The
# program creates a Python dictionary that maps the sender's mail address to a
# count of the number of times they appear in the file. After the dictionary
# is produced, the program reads through the dictionary using a maximum loop
# to find the most prolific committer.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"      # if there's no file name, just open mbox...
tfile = open(name)                              # open the doc
count = 0
adrs = dict()
for line in tfile:                              # read every line in the file...
    if not line.startswith('From '): continue   # select lines starting w/ from
    words = line.split()                        # split lines into words
    addr = words[1:2]                           # read the second word as the address
    for word in addr:
        adrs[word] = adrs.get(word,0) + 1       # add addr to adrs dictionary, count up 1.
# above - add the word to the adrs dictionary = the dictionary gets the word, & if the
# word is not in there, make the default count value 0. Then add one.
bigc = None         # set empty variables bigc & bigw
bigw = None
for word,count in adrs.items():         # for each word & count (key & value) in the adrs dictionary,
    if bigc is None or count > bigc:    # if bigc is None or smaller than the counter,
        bigw = word                     # then bigc takes on the value of the count,
        bigc = count                    # and associates the word with it as bigw.
print(bigw, bigc)

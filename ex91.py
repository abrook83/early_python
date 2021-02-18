count = 0
dic_words = dict()                   # Initializes the dictionary
fh = open('words.txt')                      # open the document
for line in fh:
    words = line.split()                    # split lines into individual words
    for word in words:
        if word in dic_words:        # if the word is already in there,
            continue                        # Discards duplicates
        dic_words[word] = count      # Value is first time word appears, square brackets adds the word to the dictionary
        count += 1                     # for every word count up 1
print(len(dic_words))
print(dic_words)
if 'who' in dic_words:
    print('True')
else:
    print('False')

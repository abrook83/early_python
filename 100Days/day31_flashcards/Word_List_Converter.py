# Access and open the file -
with open(r"100Days\day31_flashcards\Nouns Frequency List.txt") as de_words_4000:
    lines = de_words_4000.readlines()

# decode the german letters

# turn each line into a list split at the '-' and '~'
for line in lines[:5]:
    words = line.split()
    en_word = words[1]
    de_words = words[3:5]
    de_plural = words[6:]
    print(en_word)
    print(de_words)
    print(de_plural)




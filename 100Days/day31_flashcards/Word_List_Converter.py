# Access and open the file -
with open(r"100Days\day31_flashcards/Nouns Frequency List.txt") as de_words_4000:
    lines = de_words_4000.readlines()

# decode the german letters

# turn each line into a list split at the '-' and '~'
for line in lines[:5]:
    words = line.split('-')
    en_word = words[0].split()[1]
    de_word = words[1].split('~')[0]
    de_plural = words[1].split('~')[1]
    print(f"Eng Word: {en_word}")
    print(f"DE Word: {de_word}")
    print(f"DE Plural: {de_plural}")




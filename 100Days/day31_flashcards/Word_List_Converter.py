import csv
# Access and open the file -
with open(r"100Days\day31_flashcards/Nouns Frequency List.txt") as de_words_4000:
    lines = de_words_4000.readlines()

# decode the german letters

csv_file = open("DE_Words.csv", "w")
writer = csv.writer(csv_file)

# turn each line into a list split at the '-' and '~'
for line in lines:
    words = line.split('-')
    en_word = words[0].split()[1].strip()
    de_word = words[1].split('~')[0].strip()
    de_plural = words[1].split('~')[1].strip()
    new_string = f"{en_word},{de_word},{de_plural}\n"
    csv_file.write(new_string)

csv_file.close()
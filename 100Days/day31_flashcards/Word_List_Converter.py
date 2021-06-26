import csv
# Access and open the file -
DE_dict = open("100Days\day31_flashcards/Nouns Frequency List.txt", encoding='utf-8', errors='ignore')
lines = DE_dict.readlines()
print(lines[:5])

# decode the german letters

csv_file = open("DE_Words.csv", "w")
writer = csv.writer(csv_file)

# turn each line into a list split at the '-' and '~'
for line in lines[:8]:
    print(line)
    words = line.split('-')
    en_word = words[0].split()[1].strip().encode('utf-8','ignore')
    de_word = words[1].split('~')[0].strip().encode('utf-8','ignore')
    de_plural = words[1].split('~')[1].strip().encode('utf-8','ignore')
    new_string = f"{en_word},{de_word},{de_plural}\n"
    csv_file.write(new_string)

csv_file.close()
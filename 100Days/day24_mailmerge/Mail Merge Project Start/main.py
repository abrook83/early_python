#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

### My code ###

# open the names list
with open("100Days\day25_mailmerge\Mail Merge Project Start\Input/Names\invited_names.txt") as name_list:
    # creates a list of the names....
    names = name_list.readlines()
    
with open("100Days\day25_mailmerge\Mail Merge Project Start\Input\Letters\starting_letter.txt") as template:
    # the file is open, but must be read...
    letter = template.read()
    # loop through the names list
    for name in names:
        # strip the newlines from each name
        new_name = name.strip()     # can't strip this within the replace method....?
        # create new text, replacing the [name] space with the name currently held...
        new_letter = letter.replace("[name]", new_name)
        # save the new text as a file in the output folder...
        with open(f"100Days/day25_mailmerge/Mail Merge Project Start/Output/ReadyToSend/letter to {new_name}.txt", mode='w') as letter_to:
            letter_to.write(new_letter)


### Course code ###

# PLACEHOLDER = "[name]"


# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()

# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)

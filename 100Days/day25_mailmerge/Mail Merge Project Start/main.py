#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# open the names list
with open("100Days\day25_mailmerge\Mail Merge Project Start\Input\Names\invited_names.txt") as names:
    # for each of the names in the list...
    for name in names:
        # open the starting letter...
        with open("100Days\day25_mailmerge\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter:
            # loop through the words in the template...
            for word in letter:
                # if the word is "[name]"...
                if word == "[name]":
                    # replace it with the name from the list
                    word.replace(name)
        # save the new file in the output folder...

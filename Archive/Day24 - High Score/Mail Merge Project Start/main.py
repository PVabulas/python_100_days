import os
import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Day24 - High Score/Mail Merge Project Start/Input/Letters/starting_letter.txt") as f:
    letter = f.read()
with open("./Day24 - High Score/Mail Merge Project Start/Input/Names/invited_names.txt") as f:
    names = []
    for line in f.readlines():
        names.append(line.strip())

logging.debug(f"{names}")

for name in names:
    out = letter.replace("[name]", name)
    out_name = f"./Day24 - High Score/Mail Merge Project Start/Output/ReadyToSend/invite to {name}.txt"
    logging.debug(f"{out_name}")
    with open(out_name, "w") as f:
        f.write(out)

# print(os.listdir())


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
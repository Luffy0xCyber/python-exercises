# VERSION 2 : elaborate version

phrase = input("Enter a sentence: ")
cpt = 0
mot = ""

for lettre in phrase:
    if lettre.isalpha():
        mot += lettre
    else:
        if len(mot) > 0:
            cpt += 1
            mot = ""
# For the last word of the sentence, if it exists
if len(mot) > 0:
    cpt += 1

print(f"The sentence \"{phrase}\" contains {cpt} words.")
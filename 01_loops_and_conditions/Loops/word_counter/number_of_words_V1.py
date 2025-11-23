# VERSION 1 : simple version

phrase = input("Enter a sentence: ")
cpt = 0
mot = ""

for lettre in phrase:
    if lettre != " ":
        mot += lettre
    else:
        if len(mot) > 0:
            cpt += 1
        else:
            mot = ""
# for the last word of the phrase, if it exists
if len(mot) > 0:
    cpt += 1

print(f" The sentence \"{phrase}\" contains {cpt} words.")


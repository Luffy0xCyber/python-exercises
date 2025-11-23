# @author : Anas EL Faijah

import random

# initialize my random Var :

# Initialize aleatoire to a value that is not between 1 and 6
aleatoire = -1  

# Taking the input of the user :

user = int(input("Choose a number between 1 and 6 : "))

# Verify the number is between 1 and 6 :

while user > 6 or user <= 0:
    print("The chosen number is invalid! ")
    user = int(input("Choose a number between 1 and 6 : "))

# Calcul :

# initialize a counter :

cpt = 0

while aleatoire != user:
    aleatoire = random.randint(1, 6)
    print(aleatoire)
    cpt += 1

# Print the counter

print("The number of rolls is ", cpt)
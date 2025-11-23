import math

# validate number input
nb = int(input("Number of which you want to calculate the powers? "))
while nb <= 0:
    nb = int(input("Number of which you want to calculate the powers? "))

# validate exponent input
exp = int(input("Value of the exponent? "))
while exp <= 0:
    exp = int(input("Value of the exponent? "))

# calculate and display powers
res = 0
print("Exponent       Power ")
for nombre in range(exp):
    res = int(math.pow(nb, nombre))
    print(f"{nombre:>8} {res:>11}")
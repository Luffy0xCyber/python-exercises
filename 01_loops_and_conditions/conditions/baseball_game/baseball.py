# Constants :

MSG_YES = "The match will be played"
MSG_NO = "The match is postponed"
MSG_INCORRECT = "Invalid answers! "

# Data Acquisition :

user_weather = input("What is the weather :(C)loudy, (S)unny, (R)ainy ?").lower()
try:
    user_humidity = int(input("What is the humidity rate in % (0 to 100)? "))
except ValueError:
    user_humidity = -1 

# Processing :

if user_weather == "c" and 0 <= user_humidity <= 100:
    print(MSG_YES)

elif user_weather == "s" and 0 <= user_humidity < 90:
    print(MSG_YES)
elif user_weather == "s" and 90 <= user_humidity <= 100:
    print(MSG_NO)

elif user_weather == "r" and 0 <= user_humidity <= 100:
    print(MSG_NO)
else:
    # If input didn't match any valid scenario
    print(MSG_INCORRECT)
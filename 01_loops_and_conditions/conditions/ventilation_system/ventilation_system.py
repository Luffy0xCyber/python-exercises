# Constants
MSG_SUPPLY = "Install supply fans"
MSG_EXTRACT = "Install extraction fans"
MSG_BOTH = "Install supply and extraction fans"
MSG_ERROR = "Invalid answers!"

# Data Acquisition
heating_type = input("What is the heating type, (A)ir or (C)ombustion? ").lower()

# Processing
if heating_type == 'a':
    
    gas_check = input("Is the soil saturated with gas : (Y)es, (N)o? ").lower()
    
    if gas_check == 'y':
        print(MSG_BOTH)
    elif gas_check == 'n':
        print(MSG_EXTRACT)
    else:
        print(MSG_ERROR)

elif heating_type == 'c':

    try:
        humidity = int(input("What is the indoor humidity rate (in %)? "))
        
        if 70 < humidity <= 100:
            print(MSG_BOTH)
        elif 0 <= humidity <= 70:
            print(MSG_SUPPLY)
        else:
            # Covers numbers like 110 or -5
            print(MSG_ERROR)
            
    except ValueError:
        # Runs if user types non-numbers (like "hello")
        print(MSG_ERROR)

else:
    # Invalid heating type
    print(MSG_ERROR)
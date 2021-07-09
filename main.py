import random as rd
import math

length = int(input("How long do you want you password to be?"))
print()
include_special = input("Include special characters? (Y/N)")

if include_special.upper() == "Y":
    spec_limit_double = length / 2
    spec_limit = math.floor(spec_limit_double)

print()

include_caps = input("Include capitol letters? (Y/N)")

if include_caps.upper() == "Y":
    caps_limit = spec_limit
    
elif include_caps.upper() == "N":
    caps_limit = 0




while length != 0:
    
    num_or_let = rd.randint(1, 3)
    


    if num_or_let == 1:
        choose_num = rd.randint(0, 9)
        print(choose_num, end  = "")

    elif num_or_let == 2:
        choose_let = rd.choice("abcdefghijklmnopqrstuvwxyz")
        let_caps = rd.randint(1,2)
        
        if let_caps == 1 and caps_limit != 0:
            print(choose_let.upper(), end = "")
            caps_limit -= 1

        elif let_caps == 1 and caps_limit == 0:
            print(choose_let, end = "")

        
        elif let_caps == 2:
            print(choose_let.lower(), end = "")



    elif num_or_let == 3:

        if include_special.upper() == "Y" and spec_limit != 0:
            choose_spec = rd.choice("!@#$%^&*()?<>")
            print(choose_spec, end = "")
            spec_limit -= 1

        elif include_special.upper() == "Y" and spec_limit == 0:
            num_or_let2 = rd.randint(1, 2)

            if num_or_let2 == 1:
                choose_num = rd.randint(0, 9)
                print(choose_num, end  = "")

            elif num_or_let2 == 2:
                choose_let = rd.choice("abcdefghijklmnopqrstuvwxyz")
                print(choose_let, end = "")

        elif include_special.upper() != "Y":
            num_or_let2 = rd.randint(1, 2)

            if num_or_let2 == 1:
                choose_num = rd.randint(0, 9)
                print(choose_num, end  = "")

            elif num_or_let2 == 2:
                choose_let = rd.choice("abcdefghijklmnopqrstuvwxyz")
                print(choose_let, end = "")
                


    length -= 1




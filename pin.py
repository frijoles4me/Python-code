import random as r

userPin = 6
num = [1,2,3,4,5,6,9,10]

def enterPin():
    pin = int(input("Enter Your Pin. "))
    print(f"Your entered {pin}")

    if pin != userPin:
        print('Wrong pin. Try again')
        while pin != userPin:
            global num
            pin = r.choice(num)
            print(pin)
        if pin == userPin:
            print(f"loop enter wright pin {pin}")
    else:
        print('you entered the right pin')
       
        

enterPin()


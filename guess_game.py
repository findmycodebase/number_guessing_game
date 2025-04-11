import random
computer_number= random.randint(0,10)
attempts = 0
while True:
    try:
        user_number= int(input("Guess the golden number: "))
        attempts +=1
    except ValueError:
        print("Enter a valid number")
        continue
    if (user_number>computer_number):
        print("This is too high")
    elif (user_number<computer_number):
        print("This is too low")
    else:
        print("Such a good guess, you had just " + str(attempts) + " attempts")
        break 
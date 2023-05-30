import random
def easygame():
    ans = random.randint(1, 10)
    guesses = 3
    while guesses > 0:
        message = "You have {} guesses.".format(guesses)
        print(message)
        num = input("I'm thinking of a number between one and ten.")
        if int(num) == ans:
            print("Nice job! You guessed it!\n")
            break
        else:
            print("{} is incorrect\n".format(num))
            guesses -= 1
            if guesses == 1 and ans > 2 and ans < 8:
                print("Hint: The is answer is between " + str(ans-2) + " and " + str(ans+2))
            elif guesses == 1 and ans <= 2:
                print("Hint: The answer is a low number.")
            elif guesses == 1 and ans >= 8:
                print("Hint: The answer is a high number.")
    if guesses == 0:
        print("You lose!!! The answer was " + str(ans) + "\n")
def medgame():
    ans = random.randint(1, 30)
    guesses = 3
    while guesses > 0:
        message = "You have {} guesses.".format(guesses)
        print(message)
        num = input("I'm thinking of a number between one and thirty.")
        if int(num) == ans:
            print("Nice job! You guessed it!\n")
            break
        else:
            print("{} is incorrect\n".format(num))
            guesses -= 1
            if guesses == 2 and ans > 10 and ans < 20:
                print("Hint: The is answer is between " + str(ans-5) + " and " + str(ans+5))
            elif guesses == 2 and ans <= 10:
                print("Hint: The answer is less than or equal to ten.")
            elif guesses == 2 and ans >= 20:
                print("Hint: The answer is a greater than or equal to twenty.")
            elif guesses == 1 and ans > 10 and ans < 20:
                print("Hint: The is answer is between " + str(ans-3) + " and " + str(ans+3))
            elif guesses == 1 and ans <= 5:
                print("Hint: The answer is less than or equal to five.")
            elif guesses == 1 and ans >= 25:
                print("Hint: The answer is a greater than or equal to twenty-five.")
            elif guesses == 1 and ans <= 10 and ans > 5:
                print("Hint: The answer is between six and ten.")
            elif guesses == 1 and ans >= 20 and ans < 25:
                print("Hint: The answer is between twenty and twenty-four.")
    if guesses == 0:
        print("You lose!!! The answer was " + str(ans) + "\n")
def hardgame():
    ans = random.randint(1, 50)
    guesses = 3
    while guesses > 0:
        message = "You have {} guesses.".format(guesses)
        print(message)
        num = input("I'm thinking of a number between one and fifty.")
        if int(num) == ans:
            print("Nice job! You guessed it!\n")
            break
        else:
            print("{} is incorrect\n".format(num))
            guesses -= 1
            if guesses == 2 and ans > 15 and ans < 35:
                print("Hint: The is answer is between " + str(ans-10) + " and " + str(ans+10))
            elif guesses == 2 and ans <= 15:
                print("Hint: The answer is less than or equal to fifteen.")
            elif guesses == 2 and ans >= 35:
                print("Hint: The answer is a greater than or equal to thirty-five.")
            elif guesses == 1 and ans > 15 and ans < 35:
                print("Hint: The is answer is between " + str(ans-5) + " and " + str(ans+5))
            elif guesses == 1 and ans <= 10:
                print("Hint: The answer is less than or equal to ten.")
            elif guesses == 1 and ans >= 40:
                print("Hint: The answer is a greater than or equal to fourty.")
            elif guesses == 1 and ans >= 10 and ans <= 15:
                print("Hint: The answer is between ten and fifteen.")
            elif guesses == 1 and ans >= 35 and ans <= 40:
                print("Hint: The answer is between thirty-five and thirty-fourty.")
    if guesses == 0:
        print("You lose!!! The answer was " + str(ans) + "\n")
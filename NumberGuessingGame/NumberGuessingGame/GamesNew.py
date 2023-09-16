import random
def Game(guessCount, max):
    ans = random.randint(1, max)
    guesses = guessCount
    while guesses > 0:
        print("You have {} guesses.".format(guesses))
        num = input("I'm thinking of a number between 1 and {}.".format(max))
        try:
            if int(num) == ans:
                print("Nice job! You guessed it! It took {} tries\n".format(guessCount - guesses + 1))
                break
            else:
                print("{} is incorrect\n".format(num))
                guesses -= 1
                if guesses <= 3 and guesses != 1 and ans <= max/2:
                    print("Hint: The answer is a low number.")
                else:
                    print("Hint: The answer is a high number.")
        except ValueError:
            print("Not a number")
    if guesses == 0:
        print("You lose!!! The answer was " + str(ans) + "\n")
from Games import *
while True:
    choice = input("Select a game difficulty: \nA) Easy \nB) Intermediate \nC) Hard\n")
    if choice.lower() == "a" or choice.lower() == "easy":
        easygame()
    elif choice.lower() == "b" or choice.lower() == "intermediate":
        medgame()
    elif choice.lower() == "c" or choice.lower() == "hard":
        hardgame()
    else:
        print("Invalid choice. Try again.")
        continue

    play = input("Do you want to play again?(y/n)")
    if play.lower() == "n" or play.lower() == "no":
        break
    else:
        print("\n")
from GamesNew import *
while True:
    choice = input("Select a game difficulty: \nA) Easy \nB) Intermediate \nC) Hard\n")
    if choice.lower() == "a" or choice.lower() == "easy":
        Game(5, 10)
    elif choice.lower() == "b" or choice.lower() == "intermediate":
        Game(5, 30)
    elif choice.lower() == "c" or choice.lower() == "hard":
        Game(3, 100)
    else:
        print("Invalid choice. Try again.")
        continue

    play = input("Do you want to play again?(y/n)")
    if play.lower() == "n" or play.lower() == "no":
        break
    else:
        print("\n")
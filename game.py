import random

player_wins = 0
computer_wins = 0

def Choose_Option():
    user_choice = input("Please choose one : Rock,Paper,Scissors\n ")
    print("")
    if user_choice in ["Rock","rock","r","R"]:
        user_choice = "r"
    elif user_choice in ["Paper","paper","p","P"]:
        user_choice = "p"
    elif user_choice in ["Scissors","scissors","s","S"]:
        user_choice = "s"
    else:
        print("Sorry Invalid options, Try again")
        Choose_Option()
    return user_choice

def Computer_Option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice

while True:
    print("")
    user_choice = Choose_Option()
    comp_choice = Computer_Option()
    print("")

    if user_choice == 'r':
        if comp_choice == 'r':
            print("Ohh You and Computer chose Rock,Match Tied")

        elif comp_choice == "s":
            print("Computer chose Scissor,You won")
            player_wins += 1

        elif comp_choice == "p":
            print("Computer chose Paper,Computer won")
            computer_wins += 1

    elif user_choice == "s":
        if comp_choice == "s":
            print("Ohh You and Computer chose Scissor,Match Tied")

        elif comp_choice == "r":
            print("Computer chose Rock,Comp wins")
            computer_wins += 1

        elif comp_choice == "p":
            print("Computer chose paper,You won")
            player_wins += 1


    elif user_choice == "p":
        if comp_choice == "p":
            print("Ohh You and Computer chose Paper,Match Tied")

        elif comp_choice == "r":
            print("Computer chose Rock,You won")
            player_wins += 1

        elif comp_choice == "s":
            print("Computer chose Scissors,Computer won")
            computer_wins += 1


    print("")
    print("Player wins :" + str(player_wins) + " times" )
    print("Computer wins :" + str(computer_wins) + " times")
    print("")

    user_choice = input("Do you want to play again? : (y/n)")
    print("")
    if user_choice in ["yes","Yes","Y","y"]:
        pass
    elif user_choice in ["No","no","N","n"]:
        break
    else:
        break

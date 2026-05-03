import random 

print("Welcome to rock paper scissors game!!")
choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
 
while True:
    user = input("Enter your choice: (rock, paper, scissors):").lower()
    if user not in choices:
        print("invalid choice!! please enter rock paper or scissors")
        continue
    computer = random.choice(choices)
    print(f"computer chose: {computer}")

    if user == computer:
        print("its a tie!!")
    elif user == "rock" and computer == "scissors":
        print("You wonnnn!!!")
        user_score += 1
    elif user == "paper" and computer == "rock":
        print("you wonn!!!")
        user_score += 1
    elif user == "scissors" and computer == "paper":
        print("you wonn!!")
        user_score += 1
    else:
        print("you lose!!")
        computer_score += 1
    
    print(f"Your score was {user_score} and computer score was {computer_score}")
        
    play_again = input("do you want to play agai?: (yes/no): ").lower()

    if play_again == "yes":
        continue
    elif play_again == "no":
        print("Thnaks for playing!!. see yaa")
        print(f"Your final score is: {user_score} and computer score is {computer_score}")
        break
    else:
        print("invalid input!!")
        exit()
        
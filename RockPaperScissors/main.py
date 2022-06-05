import random


print("Rock Paper Scissors \n To play:\n R=Rock \n P=Paper \n S=scissors")
play_options=input("Do you play? Yes or No?: ")
cpu_options={"R":"Rock","P":"Paper","S":"scissors"}

if play_options =="yes":
    user_pick=input("Rock Paper Scissors? :")
else:
    exit("Bye, Enjoy")
while True:
    if user_pick in cpu_options :
        cpu_pick = random.choice(list(cpu_options))
        if user_pick == cpu_pick:
            print("It is a tie")
        elif user_pick == "R" and cpu_pick =="S":
            print("Player Win")
        elif user_pick == "P" and cpu_pick =="R":
            print("Player Win")
        elif user_pick == "S" and cpu_pick =="P":
            print("Player Win")
        else:
            print("Computer wins")

        print(f"{user_pick}:{cpu_pick}")
        break
    else:
        user_pick =input("Wrong Input?: ")
        continue
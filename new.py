import random


computer = random.choice([0,1,2])
player = input("Enter your choice [r,p,s]: ")
Dict = {"r":0,"p":1,"s":2}
reverse_dict = {0:"rock",1:"paper",2:"scissors"}

you = Dict[player]

print(f"You chose {reverse_dict[you]}\nComputer chose {reverse_dict[computer]}")

if computer==you:
    print("Its a draw")
else:
    if computer==0 and you ==1:
        print("You Win")
    elif computer == 0 and you == 2:
        print("You lose")
    elif computer == 1 and you == 0:
        print("You lose")
    elif computer == 1 and you == 2:
        print("You Win")
    elif computer == 2 and you == 0:
        print("You Win")
    elif computer == 2 and you == 1:
        print("You lose")
    else:
        print("Something went wrong")

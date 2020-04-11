import random

print("Hello..there...Let's Play Snake-Water-Gun..")
l = ["s", "w", "g"]
player_total = 0
pc_total = 0
i = 0
while i < 10:
    print("Enter S for Snake \nEnter W for Water \nEnter G for Gun")
    s = input("Enter Your Choice Here..: ")
    b = random.choice(l)

    if b == s:
        player_total = player_total + 0
        pc_total = pc_total + 0
        print(f"Your guess is {s} and computer's guess is {b}")
        print("Your score : ",player_total," Computer's score : ",pc_total)

    elif b == "s" and s == "w":
        pc_total = pc_total + 1
        player_total = player_total + 0
        print(f"Your guess is {s} and computer's guess is {b}")
        print("Your score : ",player_total," Computer's score : ",pc_total)

    elif b == "w" and s == "s":
        pc_total = pc_total + 0
        player_total = player_total + 1
        print(f"Your guess is {s} and computer's guess is {b}")
        print("Your score : ",player_total," Computer's score : ",pc_total)

    elif b == "w" and s == "g":
        player_total = player_total + 1
        pc_total = pc_total + 0
        print(f"Your guess is {s} and computer's guess is {b}")
        print("Your score : ", player_total, " Computer's score : ", pc_total)

    elif b == "g" and s == "w":
        player_total = player_total + 0
        pc_total = pc_total + 1
        print(f"Your guess is {s} and computer's guess is {b}")
        print("Your score : ", player_total, " Computer's score : ", pc_total)

    elif b == "g" and s == "s":
        player_total = player_total + 0
        pc_total = pc_total + 1
        print(f"Your guess is {s} and computer's guess is {b}")
        print("Your score : ", player_total, " Computer's score : ", pc_total)

    elif b == "s" and s == "g":
        player_total = player_total + 1
        pc_total = pc_total + 0
        print(f"Your guess is {s} and computer's guess is {b}")
        print("Your score : ",player_total," Computer's score : ",pc_total)
    else:
        print(f"Your guess is {s} and computer's guess is {b}")
        print("Wrong Input Dude..")
    i+=1
    print()
if player_total > pc_total:
    print("You are a winner..")
    print("..........Score card..........")
    print("Your Score is : ",player_total)
    print("Computer's Score is : ",pc_total)
else:
    print("Sorry you've lost this game..")
    print("..........Score card..........")
    print("Your Score is : ", player_total)
    print("Computer's Score is : ", pc_total)


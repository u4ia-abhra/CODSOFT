#Rock Paper Scissor game
import random
l=["Rock","Paper","Scissor"]
n=int(input("Enter number of rounds : "))
x=0
y=0
for i in range(n):
    Cc=random.choice(l)
    ui=int(input('''Enter 
    0 for Rock
    1 for Paper
    2 for Scissor
    '''))
    if(ui==0 or ui==1 or ui==2):
        Uc = l[ui]
    else:
        print("Invalid input")
        break;
    if(Uc==Cc):
        print("User's choice : ", Uc)
        print("Computer's choice : ", Cc)
        print("Round tied")
        x=x+1
        y=y+1
    elif(Uc=="Rock"):
        print("User's choice : ", Uc)
        print("Computer's choice : ", Cc)
        if(Cc=="Scissor"):
            print("User wins round")
            x=x+1
        else:
            print("Computer wins round")
            y=y+1
    elif (Uc == "Paper"):
        print("User's choice : ", Uc)
        print("Computer's choice : ", Cc)
        if (Cc == "Rock"):
            print("User wins round")
            x = x + 1
        else:
            print("Computer wins round")
            y = y + 1
    elif (Uc == "Scissor"):
        print("User's choice : ", Uc)
        print("Computer's choice : ", Cc)
        if (Cc == "Paper"):
            print("User wins round")
            x = x + 1
        else:
            print("Computer wins round")
            y = y + 1
    else:
        print("Logical error")
        break;
print("User score: ",x)
print("Computer score: ",y)
if(x>y):
    print("User wins game")
elif(x<y):
    print("User loses game")
else:
    print("Game tied")
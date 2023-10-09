print("Welcome to Treasure island. Your mission is to find thr tressure")
question_1=input("Left or Right :")
# question_2=''
if(question_1=="left"):
    question_2 = input("Swim or wait :")
    if (question_2 == "wait"):
        question_3 = input("which door :")
        if (question_3 == "blue"):
            print("Eaten by beasts.Game Over ")
        elif (question_3 == "red"):
            print("Eaten by beasts.Game Over ")
        elif (question_3 == "yellow"):
            print("You win")
        else:
            print("Game over")
    else:
        print("Attacked by trout.Game Over")

else:
    print("Fall into a hole Game Over")






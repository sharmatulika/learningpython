import random
print("This program is about loops")
print("Random Name selector")
print("Enter 8 names")
names=[]
for i in range(0,8):
    name=input()
    names.append(name)

selector=random.randint(0,7)
print("Randomly selected name is ",names[selector])

    
print("Random Color guessor")
colors=["red","blue","green","yellow","black","white","orange","purple"]

while True:
    color_selector=random.randint(0,7)
    selected_color=colors[color_selector]
    while True:
        user_color=input("Guess the color: ").lower()
        if(user_color==selected_color):
            print("You guessed right. Selected color was:",selected_color)
            break
        else:
            print("You guessed incorrectly")
    play_again=input("Do you want to play again? (yes/no)").lower()
    if(play_again=="no"):
        break
        


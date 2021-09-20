import requests
import json
import pprint
import random

print("This program is a trivia game")
url="https://opentdb.com/api.php?amount=1"

end_game=""
correct_ans_cnt=0
while end_game!="quit":    
    r=requests.get(url)
    if(r.status_code!=200):
        end_game=input("Sorry, please enter to try again or type 'quit' to quit")
    else:
        data=json.loads(r.text)
        pprint.pprint(data)
        ans=data["results"][0]["correct_answer"]
        question=data["results"][0]["question"]
        options=data["results"][0]["incorrect_answers"]
        options.append(ans)
        random.shuffle(options)
        print(question+"\n")
        for option in options:
            print(option)
        user_ans=input("Enter your answer:")    
        if(user_ans.lower()==ans.lower()):
            end_game=input("That is the correct answer. Press enter for another question or type 'quit' to quit").lower()
            correct_ans_cnt+=1
        else:
            end_game=input("That is the incorrect answer. Press enter for another question or type 'quit' to quit").lower()
    
print("You had ",correct_ans_cnt," correct answers")

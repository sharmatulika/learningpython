import matplotlib.pyplot as plt
import time as t

times=[]
mistakes=0

print("This program will help you type faster. You will have to type the word 'programming' as fast as you can for five times")
input("Press enter to continue")
while len(times)<5:
    start=t.time()
    word=input("type the word:")
    end=t.time()
    time_lapsed=end-start
    times.append(time_lapsed)
    if(word.lower()!="programming"):
        mistakes+=1
print("You made ", mistakes,"mistakes")
print("Now let's see your evolution")
t.sleep(3)
x=[1,2,3,4,5]
y=times
legendx=["1","2","3","4","5"]
plt.xticks(x,legendx)
plt.ylabel("time in seconds")
plt.xlabel("Attempts")
plt.title("Your typing evolution")
plt.plot(x,y)
plt.show()

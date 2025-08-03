import random

points=0    #points defined
life =5

f1= open('abc', 'r')
high_score=f1.read()
high_score_i = None
if high_score == "":
    high_score_i = 0
else:
    high_score_i = int(high_score)
f1.close()
print("High Score is : " + str(high_score))
can_continue = True

while can_continue and life >0:               #using loop for win or lose
    ran= random.randint(0,1)        #random function used
    print("Life : " , life)
    print("CPU picked: ", ran)
    print("Points scores : ", points)
    val=int(input("In this game , Choose either 0 or 1 : "))
    if val==ran:   
        points+=1
        print("You Won")
    else:
        print("You Lost")
        can_continue = False
        life-=1
        if life == 0:
            break

    a=input("Do you still want to continue? (y/n) : ")
    if a in ['Y','y']:                           #using loop for to ask if still want to continue       
        can_continue = True
    else:
        can_continue = False
        score=open('abc','w')           # score stored in file abc and print it
        if points > high_score_i:
            score.write(str(points))
            print("New high score " + str(points))
        elif points==0 and high_score_i == 0:
            score.write(str(points))
            print("High score is :" + str(high_score_i))
        score.close()

    print("\n")

score=open('abc','w')
if points > high_score_i:
    score.write(str(points))
    print("New high score " + str(points))
elif points==0 and high_score_i == 0:
    score.write(str(points))
    print("High score is :" +str(high_score_i))
score.close()

print("Points score : ", points)


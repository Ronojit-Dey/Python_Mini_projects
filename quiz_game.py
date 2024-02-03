print("Welcome to my Quiz Game")

playing = input("Do you wan to Play? ")
print(playing)
if playing.lower() != "yes": #YES, yES, yeS, YEs, YES, yes
    quit()


print("Let's GO")
score = 0


answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Corrct")
    score += 1
else:
    print("Wrong")    
 
answer = input("Who is Faster SSD or Hard Drive ")
if answer.upper() == "SSD":
    print("Corrct")
    score += 1
else:
    print("Wrong")  

answer = input("Which computer is the fastest Computer ")
if answer.lower() == "super computer":
    print("Corrct")
    score += 1
else:
    print("Wrong")  

answer = input("What is the Fastest Memory ")
if answer.lower() == "cache memory":
    print("Corrct")
    score += 1
else:
    print("Wrong")  

print("Your Total Score " + str(score) + " Correct")    
print("Your Total Percentage " + str((score / 4)* 100) + " %")   

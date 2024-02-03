#My code

# import random



# top_of_range = input("Type a Number ")
# user_guess = int 
# if top_of_range.isdigit():
#     top_of_range = int(top_of_range)

#     if top_of_range <=0:
#         print("type a Number larger than 0 ")
#         quit()
# else:
#     print("type a Number Next time ") 
#     quit()
           


# r = random.randint(0,top_of_range)
# print(r)

# while True:
#     print("Make a Guess")
#     user_guess == input("Enter your guess ")
#     if user_guess.isdigit():
#         user_guess = int(user_guess)
#     else:
#         print("type a Number Next time ") 
#         continue

#     if user_guess == r:
#         print("You got it")
#     else:
#         print("You got it wrong")

    #chat gpt code

import random

top_of_range = input("Type a Number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Type a number larger than 0.")
        quit()
else:
    print("Type a number next time.")
    quit()

r = random.randint(0, top_of_range)
print(r)

while True:
    user_guess = input("Make a Guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
        if user_guess == r:
            print("You got it!")
            break  # Exit the loop if the guess is correct
        else:
            print("Try again.")
    else:
        print("Type a number next time.")

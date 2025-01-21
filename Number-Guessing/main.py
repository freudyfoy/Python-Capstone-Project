from random import randint
from art import logo

answer = randint(1, 100)
#print(answer)

print(logo)
print(f"Guessing number 1 - 100")
mode = input("Choose mode 'easy' or 'hard': ")

if mode == "easy":
    turns = 10
elif mode == "hard":
    turns = 5
else:
    pass

print(f"You have {turns} attemps to make a guess")
user_ans = int(input("Make a guess: "))
while user_ans != answer and turns != 1:

    if user_ans < answer:
        print("too low")
    else:
        print("too high")
    turns = turns - 1
    #print(turns)
    print(f"You have {turns} attempts to make a guess")
    user_ans = int(input("Make a guess: "))

if user_ans == answer:
    print(f"You win! The answer is {answer}")
else:
    print(f"Try again next time!")
    print(f"The answer is {answer}")
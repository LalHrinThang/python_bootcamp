#import lib / data from python project files
import random

from art import logo,vs
from game_data import data
import os

# formatting data to print
def format_data(comparison):
    comparison_name =comparison["name"]
    comaprison_desc = comparison["description"]
    comparison_country = comparison["country"]
    return f"{comparison_name}, a {comaprison_desc}, from {comparison_country}"

# follower checker
def follower_check(guess,a_followers,b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
score = 0
continue_game = True
comparison_A = random.choice(data)
comparison_B = random.choice(data)
# Todo : print random data for comparison from data
print(logo)
while continue_game:
    comparison_A = comparison_B
    comparison_B = random.choice(data)
    while comparison_A == comparison_B:
        comparison_B = random.choice(data)

    print(f"Compare A : {format_data(comparison_A)}")
    print(vs)


    print(f"Compare B : {format_data(comparison_B)}")

# Todo : User Input

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = comparison_A["follower_count"]
    b_followers = comparison_B["follower_count"]
    #print(f"A follower : {a_followers} / B follower : {b_followers}")
# Todo : Check who has more followers => A or B 
    correct_ans = follower_check(guess,a_followers,b_followers)
#print(correct_ans)

# Todo : True =>add the score and print otherwise print only and end the game + adding while loop 

# Clearing the Screen
    os.system('clear')

    print(logo)
    if correct_ans:
        score += 1
        print(f"You're right, Current Score : {score}")
    else:
        continue_game = False
        print(f"Sorry,your answer is wrong, \n Final Score : {score}")
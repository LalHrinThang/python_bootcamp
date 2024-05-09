#import lib / data from python project files
import random

from art import logo,vs
from game_data import data


# formatting data to print
def format_data(comparison):
    comparison_name =comparison["name"]
    comaprison_desc = comparison["description"]
    comparison_country = comparison["country"]
    return f"{comparison_name},a {comaprison_desc}, from {comparison_country}"

# follower checker
def follower_check(guess,a_followers,b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
# Todo : print random data for comparison from data
print(logo)
comparison_A = random.choice(data)
comparison_B = random.choice(data)
if comparison_A == comparison_B:
    comparison_B = random.choice(data)

print(f"Compare A : {format_data(comparison_A)}")
print(vs)


print(f"Compare B : {format_data(comparison_B)}")

# Todo : User Input

guess = input("Who has more followers? Type 'A' or 'B': ").lower()

a_followers = comparison_A["follower_count"]
b_followers = comparison_B["follower_count"]

# Todo : Check who has more followers => A or B 
correct_ans = follower_check(guess,a_followers,b_followers)
#print(correct_ans)
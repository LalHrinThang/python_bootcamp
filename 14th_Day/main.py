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


# Todo : print random data for comparison from data
print(logo)
comparison_A = random.choice(data)
comparison_B = random.choice(data)
if comparison_A == comparison_B:
    comparison_B = random.choice(data)

print(f"Compare A : {format_data(comparison_A)}")
print(vs)


print(f"Compare B : {format_data(comparison_B)}")
import random

RULES = 'Find the greatest common divisor of given numbers.'

def find_gcd(x, y): 
    if(y == 0):
        return x 
    else: 
        return find_gcd(y, x % y) 

def start_game():
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    right_answer = str(find_gcd(first_num, second_num))
    question = f"{first_num} {second_num}"
    return question, right_answer
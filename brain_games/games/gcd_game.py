import random

RULES = 'Find the greatest common divisor of given numbers.'

def game_logic():
    def gcd(x, y): 
        if(y == 0):
            return x
        else: 
            return gcd(y, x % y) 
    first_num = random.randint(0, 100)  
    second_num = random.randint(0, 100)  
    right_answer = str(gcd(first_num, second_num))
    question = f"{first_num} {second_num}"
    return question, right_answer

import random
import operator


RULES = 'What is the result of the expression?\n'

def get_math_operator(math_operator):
    math_operator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    }.get
    return math_operator

def start_game():
    operatot_list = ['+', '-', '*']
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    sign = random.choice(operatot_list)
    operator = get_math_operator(sign)
    right_answer = str(operator(first_num, second_num))
    qwestion = f"{first_num} {sign} {second_num}"
    return qwestion, right_answer

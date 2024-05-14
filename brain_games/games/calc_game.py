import random
import operator

get_operator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}.get

RULES = 'What is the result of the expression?\n'

def game_logic():
    operatot_list = ['+', '-', '*']
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    sigh = random.choice(operatot_list)
    operator = get_operator(sigh)
    right_answer = str(operator(first_num, second_num))
    qwestion = f"{first_num} {sigh} {second_num}"
    return qwestion, right_answer

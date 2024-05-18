import random
import operator


RULES = 'What is the result of the expression?\n'

get_operator = {
'+': operator.add,
'-': operator.sub,
'*': operator.mul,
}.get

def start_game():
    operatot_list = ['+', '-', '*']
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    sign = random.choice(operatot_list)
    operator = get_operator(sign)
    right_answer = str(operator(first_num, second_num))
    qwestion = f"{first_num} {sign} {second_num}"
    return qwestion, right_answer

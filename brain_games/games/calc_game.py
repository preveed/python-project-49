import random


RULES = 'What is the result of the expression?\n'


def operations(operator, x, y):
    return {
        '+': lambda: x + y,
        '-': lambda: x - y,
        '*': lambda: x * y,
    }.get(operator)()


def start_game():
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    operatot_list = ['+', '-', '*']
    sign = random.choice(operatot_list)
    right_answer = str(operations(sign, first_num, second_num))
    qwestion = f"{first_num} {sign} {second_num}"
    return qwestion, right_answer

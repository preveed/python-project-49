import random


RULES = 'What is the result of the expression?\n'


def make_operations(operator, x, y):
    functions = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
    }
    return functions[operator](x, y)


def start_game():
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    operatot_list = ['+', '-', '*']
    sign = random.choice(operatot_list)
    right_answer = make_operations(sign, first_num, second_num)
    qwestion = f"{first_num} {sign} {second_num}"
    return print(qwestion, right_answer)

import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".\n'


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def start_game():
    question = random.randint(1, 100)
    right_answer = is_even(question)
    return question, right_answer

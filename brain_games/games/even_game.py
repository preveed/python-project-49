import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".\n'


def is_even(num):
    return num % 2 == 0


def start_game():
    question = random.randint(1, 100)
    result = is_even(question)
    if result:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer

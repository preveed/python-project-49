import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".\n'

def game_logic():
    question = random.randint(1, 100)
    if question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer


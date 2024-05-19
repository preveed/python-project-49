import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start_game():
    question = random.randint(1, 99)
    if question == 2:
        right_answer = 'yes'
        return question, right_answer
    if question % 2 == 0:
        right_answer = 'no'
        return question, right_answer
    else:
        for i in range(3, int(question ** 0.5) + 1, 2):
            if question % i == 0:
                right_answer = 'no'
                return question, right_answer
            else:
                right_answer = 'yes'
        return question, right_answer

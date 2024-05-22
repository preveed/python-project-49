import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 2:
        answer = 'yes'
        return answer
    if number % 2 == 0:
        answer = 'no'
        return answer
    else:
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                answer = 'no'
                return answer
            else:
                answer = 'yes'
                return answer


def start_game():
    question = random.randint(1, 99)
    right_answer = is_prime(question)
    return question, right_answer

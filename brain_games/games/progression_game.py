import random

RULES = 'What number is missing in the progression?'


def make_progression():
    start = random.randint(0, 10)
    lenght = random.randint(4, 10)
    addition = random.randint(1, 5)
    progression = [start]
    for _ in range(lenght):
        start += addition
        progression.append(start)
    return progression


def start_game():
    progression_string = make_progression()
    miss_place = random.randint(0, len(progression_string) - 1)
    right_answer = str(progression_string[miss_place])
    progression_string[miss_place] = '..'
    question = " ".join(map(str, progression_string))
    return question, right_answer

import random

RULES = 'What number is missing in the progression?'

def game_logic():
    start = random.randint(0, 10)
    lenght = random.randint(4, 10)
    addition = random.randint(1, 5)
    progress = [start]
    for i in range(lenght):
        start += addition
        progress.append(start)
    miss_place = random.randint(0, len(progress)-1)
    right_answer = str(progress[miss_place])
    progress[miss_place] = '..'
    question = " ".join(map(str, progress))
    return question, right_answer
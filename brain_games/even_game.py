import random
import prompt
import sys


def even_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".\n')
    i = 0
    while i < 3:
        num = random.randint(1, 100)
        print(f'Question: {num}\n')
        while True:
            answer = input('Your answer: ')
            if answer == 'yes' or answer == 'no':
                break
            else:
                print("Tupe 'yes' or 'no'!")
        if num % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        if answer == right_answer:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was \
'{right_answer}'.\nLet's try again, {name}!")
            sys.exit()
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    even_game()

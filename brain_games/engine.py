NUMBER_OF_ROUNDS = 3

def run(game):
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    for _ in range(NUMBER_OF_ROUNDS):
        qestion, right_answer = game.start_game()
        print(f'Qestion: {qestion}')
        user_answer = input('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was"
            f"'{right_answer}'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}')

import prompt

NUMBER_OF_ROUNDS = 3

def engine_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    for _ in range(NUMBER_OF_ROUNDS):
        qestion, right_answer = game.game_logic()
        print(f'Qestion: {qestion}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was"
            f" '{right_answer}'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}')


if __name__ == '__main__':
    engine_game()

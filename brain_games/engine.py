import prompt

NUMBER_OF_ROUNDS = 3


def get_inputs(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.RULES)
    for _ in range(NUMBER_OF_ROUNDS):
        question, right_answer = game.start_game()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was"
                  f" '{right_answer}'.\nLet's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')

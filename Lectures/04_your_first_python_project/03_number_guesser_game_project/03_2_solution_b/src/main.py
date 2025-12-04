# The comments are the codes that were thought in the course, they may be different from what we have here.
from game_logic.number_generator import generate_random_number
from game_logic.hint_generator import provide_hint
from game_logic.scorer import Scorer
from utils.input_validator import get_valid_input

# from src.utils.input_validator import get_valid_input
# from src.game_logic.number_generator import generate_random_number
# from src.game_logic.hint_generator import provide_hint


def main():
    number_to_guess = generate_random_number(1, 100)
    scorer = Scorer()
    # actual_number = generate_random_number(1, 100)
    # score = 100

    while True:
        # user_input = get_valid_input(1, 100)
        # if user_input == actual_number:
        # print(f'You guessed the number correctly!')
        # print(f'Your score is {score}.)
        # break
        # else:
        # provide_hint(user_input, actual_number)
        # score -= 10
        # score = max(0, score)

        guess = get_valid_input("Enter your guess: ", 1, 100)
        if guess == number_to_guess:
            print(f"Congratulations! Your final score is: {scorer.get_score()}")
            break
        else:
            hint = provide_hint(guess, number_to_guess)
            print(hint)
            scorer.decrement_score()


if __name__ == "__main__":
    main()

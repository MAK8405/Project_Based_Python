# Generate random number:
import random

# 👉 random is a module
# A module in Python = a file that contains many functions, classes, and variables.


def validate_input(input_num):
    # 1 < input_num < 100
    # > 100
    # < 1
    # q
    # non digit
    if not input_num.isdigit():
        # with isdigit we can if a string is a number or not
        print("Invalid input. Please enter a number.")
        return False

    input_num = int(input_num)
    if input_num < 1 or input_num > 100:
        print("Invalid input. Please enter a number between 1 and 100.")
        return False

    return True


def start_game():
    # int(random.random() * 100 + 1)
    # random.random is a uniform distribution, every number between 0 to 1 have a same luch for generate.
    # Better choice than the up one than 2 previous line
    rand_num = random.randint(1, 100)
    score = 100

    # Indefinite loop -> we don't know till where it will continue, we will continue till it is finished.
    while True:
        input_num = input("Enter your guess between 1 and 100:")
        # The output of "input" is always string and we should convert it to integer"
        # plus the user should enter a number, not a character
        # before convert it to string, we should validate the input
        # non digit -> not a number

        if input_num == "q":
            print("Goodbye!")
            break
        # -> When we reach the proper condition we will break the lopp

        if not validate_input(input_num):
            # q for quit
            continue

        input_num = int(input_num)
        if input_num == rand_num:
            print(f"You guessed correctly! Your score is: {score}")
            wanna_play = input("Do you want to play again? (y/n)")
            if wanna_play == "y":
                rand_num = random.randint(1, 100)
                score = 100
                continue
            else:
                print("Goodbye!")
                break
            # -> When we reach the proper condition we will break the lopp

        elif input_num > rand_num:
            print("You guessed too high!")
        else:
            print("You guessed too low!")

        score -= 10
        score = max(score, 0)


if __name__ == "__main__":
    start_game()

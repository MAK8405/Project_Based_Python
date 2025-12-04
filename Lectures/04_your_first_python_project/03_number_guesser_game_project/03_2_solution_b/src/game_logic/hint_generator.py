def provide_hint(guess, actual_number):
    """Provide a hint based on the difference between guess and actual_number."""
    if guess < actual_number:
        return "Try a higher number!"
        # print('Your guess is too low.')
    else:
        return "Try a lower number!"

    # elif guess > actual_number:
    # print('Your guess is too high')

def get_valid_input(prompt, start, end):
    """Get a valid integer input from the user between start and end (inclusive)."""
    while True:
        try:
            user_input = int(input(prompt))
            if start <= user_input <= end:
                return user_input
            else:
                print(f"Please enter a number between {start} and {end}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# def get_valid_input(start, end):
#     while True:
#         try:
#             user_input = int(input('Enter a number: '))
#             if start <= user_input <= end:
#                 return user_input
#             else:
#                 print(f'Invalid input. Please enter a number between {start} and {end}.')
#                 continue
#         except ValueError:
#             print('Invalid input. Please enter a number.')
#             continue

# if __name__ == '__main__':
#     print(get_valid_input(1, 100))

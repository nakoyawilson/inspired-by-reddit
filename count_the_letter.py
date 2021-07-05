def count_i(letter, input_string):
    """Takes a string and returns the number of times the chosen letter appears in the string"""
    count = input_string.count(letter)
    return count

print("This program counts how many times a letter of your choice appears in a sentence.")
continue_program = "y"
while continue_program == "y":
    continue_program = input("Do you want to submit a sentence? Type 'y' or 'n': ").lower()
    if continue_program == "y":
        user_input = input("Enter a sentence: ").lower()
        user_letter = input("Choose a letter: ").lower()
        result = count_i(user_letter, user_input)
        print(f"The letter {user_letter} appears {result} time(s) in the sentence.")
    else:
        print("Goodbye")
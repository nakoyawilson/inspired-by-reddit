def make_string_alpha(non_alpha_string):
    """Removes all non-alpha characters and returns string of alpha characters"""
    alpha_string = ""
    for char in non_alpha_string:
        if char.isalpha():
            alpha_string += char
    return alpha_string

print("""
This program removes all non-alpha characters from the given input.
For example, if the input is:
-Hello, 1 world$!
The output is:
Helloworld""")
continue_program = "y"
while continue_program == "y":
    continue_program = input("Do you want to submit a string? Type 'y' or 'n': ")
    if continue_program == "y":
        user_input = input("Enter a string of characters: ")
        result = make_string_alpha(user_input)
        print(result)
    else:
        print("Goodbye")
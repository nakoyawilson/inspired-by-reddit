def is_positive(number):
    if number > 0:
        return True

def is_negative(number):
    if number < 0:
        return True

continue_program = True
while continue_program:
    number = int(input("Please enter a positive or negative integer, or 0 to quit: "))
    pos_count = 0
    neg_count = 0
    if number == 0:
        conitnue_program = False
        print(f"You entered {pos_count} positive integer(s) and {neg_count} negative integer(s).")
    elif number > 100 or number < -100:
        print("Invalid input. Please make sure your integer is between -100 and 100.")
    else:
        is_positive(number)
        is_negative(number)
        if is_positive(number):
            pos_count += 1
        else:
            neg_count += 1
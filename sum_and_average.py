def sum_and_average(list_of_numbers):
    """Takes a list of numbers and returns the sum and average"""
    num_list = []
    for num in str_num_list:
        num = float(num)
        num_list.append(num)
    len_of_list = len(num_list)
    sum_of_num = sum(num_list)
    average_of_num = sum_of_num/len_of_list
    return sum_of_num, average_of_num

print("This program takes a list of numbers and returns the sum and average")
continue_program = "y"
while continue_program == "y":
    continue_program = input("Do you want to submit a list of numbers? Type 'y' or 'n': ")
    if continue_program == "y":
        str_num_list = input("Enter a list of numbers separated by spaces. Press enter when you are finished.\n").split()
        sum_nums, average_nums = sum_and_average(str_num_list)
        print(f"The sum of the numbers you entered is: {sum_nums}")
        print(f"The average of the numbers you entered is: {average_nums}")
    else:
        print("Goodbye")
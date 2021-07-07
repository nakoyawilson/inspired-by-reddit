from statistics import median

def find_median(list_of_int):
    """Takes a list of integers and returns the median of the sorted list"""
    for index, num in enumerate(list_of_int):
        list_of_int[index] = int(num)
    list_of_int.sort()
    median_of_list = median(list_of_int)
    return median_of_list

start_program = True
while start_program:
    print("This program takes a list of integers and returns the median of the sorted list.")
    start_program = input("Do you want to input a list of integers? Type 'y' or 'n': ")
    if start_program == "y":
        num_list = input("Input list of integers separated by spaces: ").split()
        the_median = find_median(num_list)
        print(f"The median is: {the_median}")
    else:
        start_program = False
        print("Goodbye")



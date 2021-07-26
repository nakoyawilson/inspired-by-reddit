numbers = input("Enter a list 10 integers separated by spaces: ")
list_of_numbers = numbers.split()
while len(list_of_numbers) < 10:
    numbers_needed = 10 - len(list_of_numbers)
    additional_numbers = input(f"Please enter {numbers_needed} more numbers separated by spaces: ")
    list_of_numbers.extend(additional_numbers.split())
if len(list_of_numbers) > 10:
    list_of_numbers = list_of_numbers[:10]
    print("Too many integers we submitted. Only the first 10 will be used.")
largest_odd_number = 0
for number in list_of_numbers:
    if int(number) % 2 == 1 and int(number) > largest_odd_number:
        largest_odd_number = int(number)
if largest_odd_number == 0:
    print("No odd numbers were entered")
else:
    print(f"The largest odd number entered was: {largest_odd_number}")

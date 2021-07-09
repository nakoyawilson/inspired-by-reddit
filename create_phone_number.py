def create_phone_number(list_of_numbers):
    for index, num in enumerate(list_of_numbers):
        list_of_numbers[index] = str(num)
    string_of_num = "".join(list_of_numbers)
    phone_number = f"({string_of_num[:3]}){string_of_num[3:6]}-{string_of_num[6:]}"
    return phone_number


# Test
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
phone_number = create_phone_number(list_of_numbers)
print(phone_number)
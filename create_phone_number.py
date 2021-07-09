def create_phone_number(list_of_numbers):
    for index, num in enumerate(list_of_numbers):
        list_of_numbers[index] = str(num)
    string_of_num = "".join(list_of_numbers)
    phone_number = f"({string_of_num[:3]}){string_of_num[3:6]}-{string_of_num[6:]}"
    return phone_number
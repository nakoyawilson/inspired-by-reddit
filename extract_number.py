import re

def extract_numbers(sentence):
    """Extracts number before the word presence and returns the number without a comma"""
    num_regex = re.compile(r'(\d+,\d+) presence')
    extracted_numbers = num_regex.findall(sentence)
    numbers = []
    for number in extracted_numbers:
        new_number = number.replace(",", "")
        numbers.append(new_number)
    return numbers


example1 = extract_numbers("4,183 presence, More than 98% presence, 1,000 trial")
example2 = extract_numbers("100% satisfaction, 1,011 presence, More than 98% presence")
example3 = extract_numbers("100% satisfaction, Free trial, 1,137 presence")
example4 = extract_numbers("""4,183 presence, More than 98% presence, 1,000 trial,
100% satisfaction, 1,011 presence, More than 98% presence,
100% satisfaction, Free trial, 1,137 presence""")
print(example1)
print(example2)
print(example3)
print(example4)

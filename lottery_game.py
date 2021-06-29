import random
import time

# Declare variables
user_numbers = []
lottery_numbers = []
max_numbers = 5
max_value = 40

# Input
print("Welcome to the Lottery Program! Pick {} numbers from 1 - {}".format(max_numbers, max_value))

while len(user_numbers) < max_numbers:
    user_num = int(input("Pick a number: "))
    if user_num > 0 and user_num <= max_value:
        if user_num not in user_numbers:
            user_numbers.append(user_num)
        else:
            print("Number already chosen. Please choose a different number.")
    else:
        print("Invalid entry. Try again")

# Picks Unique Lottery Numbers
while len(lottery_numbers) < max_numbers:
    lottery_num = random.randint(1, max_value)
    if lottery_num not in lottery_numbers:
        lottery_numbers.append(lottery_num)

# Checks for winning numbers
correct_picks = 0
for number in user_numbers:
    if number in lottery_numbers:
        correct_picks += 1

# Results
print("Calculating...")
time.sleep(1)
print("*")
time.sleep(1)
print("*")
time.sleep(1)
print("*")

print("Your lottery picks: {}.".format(user_numbers))
print("Winning numbers: {}.".format(lottery_numbers))
if correct_picks == max_numbers:
    print("JACKPOT! You won $1,000,000.")
elif correct_picks == max_numbers - 1:
    print("Congratulations! You won $100,000.")
elif correct_picks == max_numbers - 2:
    print("Congratulations! You won $10,000.")
else:
    print("Sorry, you are not a winner.")
from lottery import Lottery

# variable from Lottery class and define winning numbers
lotto = Lottery()
lotto.winning_numbers = lotto.draw_numbers()

# define my ticket variable and count, to track how many tickets bought
my_ticket = lotto.draw_numbers()
count = 1

# Introduce rules for lotto jackpot
print(f"To win the jackpot you need to match {lotto.numbers_to_match} numbers ranging from {lotto.numbers_range[0]} to {lotto.numbers_range[-1]}")
if lotto.bonus_to_match:
    print(f"You also need to match {lotto.bonus_to_match} bonus number(s) ranging from {lotto.bonus_range[0]} to {lotto.bonus_range[-1]}\n")


# Define maximum number of tickets to buy
max_tickets = input("How many tickets would you like to buy?\n")
while max_tickets.isdigit() == False:
    max_tickets = input("Sorry, that is not a number!\nHow many tickets would you like to buy?\n")

# Keep buying more tickets and incrementing count until we get the winning numbers
while my_ticket != lotto.winning_numbers and count < int(max_tickets):
    my_ticket = lotto.draw_numbers()
    count += 1
    print(f"{count} {my_ticket}")

# Exit statement when we failed to get a winning ticket
if count == int(max_tickets):
    print(f"\nSorry! You bought {count} tickets, but still didn't win the jackpot!!")
    print("Better luck next time :-)")

# Print winning numbers when we get a match
if my_ticket == lotto.winning_numbers:
    print("\nYOU WIN!!!\nYour winning numbers are:")
    for num in my_ticket:
        print(f"-{num}")

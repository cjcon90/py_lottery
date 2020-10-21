from random import choice
class Lottery:
    """A class to simulate a real life lottery"""
    def __init__(self):
        self.numbers_range = range(1, 41) # define range of main draw numbers
        self.numbers_to_match = 5 # define how many numbers in main draw
        self.bonus_range = range(1, 11) # define range of bonus numbers
        self.bonus_to_match = 1 # define how many bonus numbers
        self.winning_numbers = [] # variable for winning numbers

    def draw_numbers(self):
        """Function to draw numbers based on main draw and bonus range & length"""
        numbers = []
        bonus = []
        while len(numbers) < self.numbers_to_match:
            draw_num = choice(self.numbers_range)
            if draw_num not in numbers:
                numbers.append(draw_num)
        while len(bonus) < self.bonus_to_match:
            draw_num = choice(self.bonus_range)
            if draw_num not in bonus:
                bonus.append(draw_num)
        
        return sorted(numbers) + sorted(bonus)
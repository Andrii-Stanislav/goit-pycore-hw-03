import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    random_list = random.sample(range(min, max), quantity)
    
    random_list.sort()
    
    return random_list

# * Test

# lottery_numbers = get_numbers_ticket(1, 47, 6)
# print("Ваші лотерейні числа:", lottery_numbers)

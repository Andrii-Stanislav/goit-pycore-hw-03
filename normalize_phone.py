import re

def normalize_phone(phone_number: str) -> str:
    only_numbers_phone = re.sub(r"\D", "", phone_number)

    return f"+{only_numbers_phone}" if only_numbers_phone.startswith("38") else f"+38{only_numbers_phone}"

# * function example without regex
def normalize_phone_2(phone_number: str) -> str:
    phone_number_list = []

    for char in phone_number:
        if char.isdigit():
            phone_number_list.append(char)

    only_numbers_phone = "".join(phone_number_list)

    return f"+{only_numbers_phone}" if only_numbers_phone.startswith("38") else f"+38{only_numbers_phone}"


# * Test

# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

# sanitized_numbers_2 = [normalize_phone_2(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers_2)

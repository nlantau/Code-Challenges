# nlantau, 2020-12-17
import os
import re

day = "16.txt"
day = os.path.join(os.path.dirname(__file__), day)

fin = open(day, "r")
data = fin.read().strip()

# RegEx time!
class_numbers = re.compile(
    r"""((?<=class:\s)(?P<f_low>\d+)-(?P<f_high>\d+)\s\w+\s(?P<s_low>\d+)-(?P<s_high>\d+))"""
)
row_numbers = re.compile(
    r"""((?<=row:\s)(?P<f_low>\d+)-(?P<f_high>\d+)\s\w+\s(?P<s_low>\d+)-(?P<s_high>\d+))"""
)
seat_numbers = re.compile(
    r"""((?<=seat:\s)(?P<f_low>\d+)-(?P<f_high>\d+)\s\w+\s(?P<s_low>\d+)-(?P<s_high>\d+))"""
)
your_ticket_numbers = re.compile(r"""((?<=your ticket:)\n(?P<y_nums>[\d+,?]+))""")
nearby_ticket_numbers = re.compile(
    r"""((?<=nearby tickets:)\n(?P<near_nums>[\d+(,|\n)]+))"""
)

# Search data for matching Regex patterns
class_match = class_numbers.search(data)
row_match = row_numbers.search(data)
seat_match = seat_numbers.search(data)
your_ticket_match = your_ticket_numbers.search(data)
nearby_ticket_match = nearby_ticket_numbers.search(data)

class_range_low = range(
    int(class_match.group("f_low")), int(class_match.group("f_high")) + 1
)
class_range_high = range(
    int(class_match.group("s_low")), int(class_match.group("s_high")) + 1
)
row_range_low = range(int(row_match.group("f_low")), int(row_match.group("f_high")) + 1)
row_range_high = range(
    int(row_match.group("s_low")), int(row_match.group("s_high")) + 1
)
seat_range_low = range(
    int(seat_match.group("f_low")), int(seat_match.group("f_high")) + 1
)
seat_range_high = range(
    int(seat_match.group("s_low")), int(seat_match.group("s_high")) + 1
)

# Make 'near_nums' a list of list with parsed integers
near_nums = [n.split(",") for n in nearby_ticket_match.group("near_nums").split()]
near_nums = [[int(num) for num in nested_list] for nested_list in near_nums]

# List contaning all faulty tickets
ticket_scanning_error_rate = list()

# Getting all the faulty tickets
for li in near_nums:
    for num in li:
        if (
            num not in class_range_low
            and num not in class_range_high
            and num not in row_range_low
            and num not in row_range_high
            and num not in seat_range_low
            and num not in seat_range_high
        ):
            ticket_scanning_error_rate.append(num)

# Print results
print(f"Ticket scanning error rate: {sum(ticket_scanning_error_rate)}")
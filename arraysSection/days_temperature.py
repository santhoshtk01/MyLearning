# Program to complete the challenge project given by the instructor


def get_input(days: int) -> list:
    temperatures = []
    for index in range(days):
        val = int(input("Enter day {0}'s temperature : ".format(index)))
        temperatures.append(val)

    return temperatures


def find_days(values: list) -> int:
    average = sum(values) / len(values)
    count_days = 0

    for val in values:
        if val > average:
            count_days += 1

    return count_days


num_of_days = int(input("Enter how many day's Temperature : "))
values = get_input(num_of_days)
print("Days - {0}".format(find_days(values)))

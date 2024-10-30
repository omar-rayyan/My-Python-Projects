# Countdown
def countdown(num):
    return [i for i in range(num, -1, -1)]

# Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]

# First Plus Length
def first_plus_length(list):
    return list[0] + len(list)

# Values Greater than Second
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    second_value = list[1]
    new_list = [i for i in list if i > second_value]
    print(len(new_list))
    return new_list

# This Length, That Value
def length_and_value(size, value):
    return [value] * size
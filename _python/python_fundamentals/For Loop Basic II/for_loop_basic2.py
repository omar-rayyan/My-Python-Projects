# Biggie Size

def biggie_size(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] = "big"
    return lst

# Count Positives

def count_positives(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] > 0:
            count += 1
    lst[len(lst) - 1] = count
    return lst

# Sum Total

def sum_total(lst):
    total_sum = 0
    for num in lst:
        total_sum += num
    return total_sum

# Average

def average(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum / len(lst)

# Length

def length(lst):
    return len(lst)

# Minimum

def minimum(lst):
    if len(lst) == 0:
        return False
    minimum_value = lst[0]
    for num in lst:
        if num < minimum_value:
            minimum_value = num
    return minimum_value

# Maximum

def maximum(lst):
    if len(lst) == 0:
        return False
    maximum_value = lst[0]
    for num in lst:
        if num > maximum_value:
            maximum_value = num
    return maximum_value

# Ultimate Analysis

def ultimate_analysis(lst):
    if len(lst) == 0:
        return False
    
    total_sum = 0
    minimum_value = lst[0]
    maximum_value = lst[0]
    length = 0
    
    for num in lst:
        total_sum += num
        if num < minimum_value:
            minimum_value = num
        if num > maximum_value:
            maximum_value = num
        length += 1
    
    average = total_sum / length
    
    return {
        'sumTotal': total_sum,
        'average': average,
        'minimum': minimum_value,
        'maximum': maximum_value,
        'length': length
    }

# Reverse List

def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left] = lst[right]
        lst[right] = lst[left]
        left += 1
        right -= 1
    return lst
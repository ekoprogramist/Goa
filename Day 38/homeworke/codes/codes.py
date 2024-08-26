#first codewars:
def filter_list(l):
    return [item for item in l if isinstance(item, int)]
#second codewars:

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    
    return numbers[0] + numbers[1]

#theerd codewars:
def solution(text, ending):
    return text.endswith(ending)

#forth codewars:
from collections import Counter

def stray(arr):
    counts = Counter(arr)
    for num in counts:
        if counts[num] == 1:
            return num


#fifth codewars:
def sort_by_length(arr):
    return sorted(arr, key=len)



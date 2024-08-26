#first codewars:
def make_upper_case(s):
    return s.upper()

#second codewars:
def hero(bullets, dragons):
    bullets_needed = 2 * dragons
    return bullets >= bullets_needed

#third codewars:
def invert(lst):
    list = []
    if lst == []:
        return []
    for i in lst:
        list.append(-i)
    return list
#forth codewars:
def difference_in_ages(ages):
    small = min(ages)
    big = max(ages)
    age = big - small
    return small,big,age 

#fifth codewars:
def sum_mix(arr):
    number = 0
    for i in arr:
        number += int(i)
    return number
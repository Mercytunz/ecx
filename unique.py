"""
Create a function unique that takes a list(L) which contains numbers as a para-
meter and returns a sorted new list with unique elements of the first list.
"""


def unique(*numbers):
    seen = []
    for number in numbers:
        if number not in seen:
            seen.append(number)
    return f"Unique List: {seen}"
samList = unique(1,2,3,3,3,3,4,5)
samList1 = unique(1,2,3,3,3,3,4,5,3,3,3,3,4,5,6,6,11,22,33,44)
samList2 = unique(1,2,3,3,3,3,4,5,5,3,3,3,3,4,5,6,6,110,20,19,34)
print(samList)
print(samList1)
print(samList2)
    

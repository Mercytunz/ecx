import math

number = input("Enter a number:\t")

def is_perfect_square(number):
    num = int(number)
    num = num**0.5
    num = math.ceil(num)
    if type(num) is not int:
        print(f"{number} is not a perfect square")
    elif type(num) is int:
        return f"{num} is a perfect square"
numb = is_perfect_square(number)
print(numb)
    
        

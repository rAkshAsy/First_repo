'''
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''

def high_and_low(numbers:str):
    numbers = numbers.split()
    higher, lower = int(numbers[0]), int(numbers[0])
    for num in numbers:
        higher = int(num) if int(num) > higher else higher
        lower = int(num) if int(num) < lower else lower
        
    return f'{higher} {lower}'

# Better issues  
# def high_and_low(numbers):
#   numbers = [int(c) for c in numbers.split(' ')]
#   return f"{max(numbers)} {min(numbers)}"


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")) # 42 -9
print(high_and_low("1 2 3")) # 3 1
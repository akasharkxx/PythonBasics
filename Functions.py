# Functions
# Parameters
# Return Values

def multiply(numArray):
    total = 1
    for num in numArray:
        total *= num
    return total

result = multiply([1,2,3,4,5])
print(result)
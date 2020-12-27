from math import inf

def high_and_low(numbers):

    lowest = inf

    highest = -inf

    numbers = numbers.split(" ")    

    for number in numbers:

        number = int(number)

        if  number > highest:
            highest = number
        
        if number < lowest:
            lowest = number

    return f"{highest} {lowest}"


print(high_and_low('20000 1 -23 2 3 090989'))
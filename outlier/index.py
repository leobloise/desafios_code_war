def find_outlier(integers):

    meaning_numbers = []

    for integer in integers:

        meaning_numbers.append(integer % 2)
    
    if meaning_numbers.count(0) > 1:

        return integers[meaning_numbers.index(1)]
    
    else:
       
        return integers[meaning_numbers.index(0)]

print(find_outlier([0, 2, 4, 3]))


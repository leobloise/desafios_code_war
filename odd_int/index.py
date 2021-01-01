def find_it(seq):
    
    result = [number for number in seq if seq.count(number) % 2 != 0]

    return result[0]

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
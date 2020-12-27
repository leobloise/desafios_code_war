def split_number(number):
    return int(number)

def convert_to_tuple(n):
    return tuple(map(split_number,list(str(n))))

def couldBeInt(number):
    
    import re
    
    return bool(re.search('\.0$', str(number)))

def dig_pow(n, p):
    
    digits = convert_to_tuple(n)

    x = 0

    for digit in digits:

        x += digit**p
        p += 1

    k = str(x / n)

    if(couldBeInt(k)):
        return int(float(k))

    return -1

print(dig_pow(92, 1))
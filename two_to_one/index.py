def longest(s1, s2):
    
    s3 = f'{s1}{s2}'

    s4 = []

    for letter in s3:
        
        if letter not in s4:
            s4.append(letter)

    s4 = sorted(s4)

    return "".join(s4)


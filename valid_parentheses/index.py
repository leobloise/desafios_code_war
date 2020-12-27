def remove_unless_parentheses(text):
    
    phrase = []

    for letter in text:

        if letter == '(' or letter == ')':
            phrase.append(letter)
    
    return "".join(phrase)



def valid_parentheses(string):
    
    string = remove_unless_parentheses(string)

    string = list(enumerate(list(string)))

    need_close = []

    closing = []

    for index, parenthesis in string:

        if parenthesis == '(':
            need_close.append(index)
            continue
            
        if parenthesis == ')':
            closing.append(index)
            continue
    
    if len(need_close) != len(closing):
        return False
    
    for close_parentheses in closing:

        for open_parentheses in need_close: 

            if close_parentheses > open_parentheses:

                need_close.remove(open_parentheses)
                break
    
    if len(need_close) != 0:
        return False
    
    return True
def duplicate_count(text):
    
    text = text.lower()

    text_list = list(text)

    counted = set()

    for letter in text_list:

        qtd = text_list.count(letter)

        if qtd >= 2:
            counted.add(letter)

    return len(counted)


print(duplicate_count('aaaaaaaaaabbbbbbbbbbbbbbbcccccccccccccccccccccdeeeeeeeeeeeeeeeeeeeee')) 
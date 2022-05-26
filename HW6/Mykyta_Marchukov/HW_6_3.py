def count_symbols(word):
    '''
    This function that calculates the number of characters included in a given string
    '''
    result = {}
    for item in word:
        if item in result:
            continue
        else:
            result.update({str(item): word.count(item)})
    return result

print(count_symbols(input('Enter text: ')))

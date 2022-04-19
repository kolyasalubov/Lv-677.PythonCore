
def count_symbols(word_1):
    result = {}
    for item in word_1:
        if item in result:
            continue
        else:
            result.update({str(item): word_1.count(item)})
    return result        
print(count_symbols("hello"))   
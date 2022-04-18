def largest_number(number1, number2):
    """
    :param number1:
    :param number2:
    :return:
    """
    if number1 > number2:
        return number1
    elif number2 > number1:
        return number2
    else:
        return number1


print(largest_number(25, 60))
digital_4 = input("Enter 4 digit number: ")
mult = 1
dobutok = int(digital_4)


if len(digital_4) == 4:
    while dobutok != 0:
        mult = mult * (dobutok % 10)
        dobutok = dobutok // 10


    print(f"multiplication of numbers = {mult}")
    digital_list = list(digital_4)
    sort_digital = "".join(sorted(digital_4))
    digital_list.reverse()
    digital_reverse = "".join(digital_list)
    print(f"reverse number: {digital_reverse }")
    print(f"number sorted: {sort_digital}")
else:
    print("There are no 4 digits in the number")

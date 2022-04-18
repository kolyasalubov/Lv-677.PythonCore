def func_dict(input_txt):
    output_list = list(input_txt)
    output_dict = {}
    for i in output_list:
        output_dict[i] = input_txt.count(i)
    return output_dict


input_txt = input("Enter string - ")

print(f'Output {func_dict(input_txt)}')






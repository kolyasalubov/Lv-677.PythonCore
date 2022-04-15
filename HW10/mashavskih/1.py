def ageexeption():
    try:
        age = int(input('Enter age: '))
        if age%2 == 0:
            print('{1} is Even'.format(age))
        elif age <=0:
            raise ValueError("That is not a positive number!")
        else:
            print('{0} is Odd'.format(age))
    except ValueError as e:
        print(e)
ageexeption()

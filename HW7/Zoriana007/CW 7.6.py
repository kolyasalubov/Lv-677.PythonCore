def conversion (bool_name):
    
    if bool_name == "Yes":
        return "True"
    elif bool_name == "No":
        return "False"
    else:
        return """Error!
Input only 'Yes' or 'No' words. Please try again."""
    
print(conversion("Yes"))
print(conversion("No"))
print(conversion("Else"))




# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
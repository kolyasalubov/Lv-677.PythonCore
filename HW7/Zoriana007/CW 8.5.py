def banjo (name:str):
    
    for letter in name:
        
        if name[0] == "R" or name[0] == "r" in name:
            return "You play banjo!"
        else:
            return "You dont play banjo!"
        
print(banjo("Zoriana"))
print(banjo("Ronaldo"))




# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.
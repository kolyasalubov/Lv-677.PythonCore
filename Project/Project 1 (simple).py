""" Mad Libs Generator
----------------------------------------
"""
# //Loop back to this point once code finishes
loop = 1
while (loop < 10):
# All the questions that the program asks the user
    adjective = input("Choose an adjective: ")
    superiative = input("Choose a superiative: ")
    noun_singular = input("Choose a singular noun: ")
    adjective2 = input("Choose an adjective: ")
    noun_singular2 = input("Choose a singular noun: ")
    adjective3 = input("Choose an adjective: ")
    noun_singular3 = input("Choose a singular noun: ")
    verb = input("Choose a verb: ")
    noun_singular4 = input("Choose a singular noun: ")
    verb2 = input("Choose a verb: ")
    noun_singular7 = input("Choose a singular noun: ")
    adjective4 = input("Choose an adjective: ")
    adjective5 = input("Choose an adjective: ")
    noun_plural = input("Choose a plural noun: ")
    city = input("Name a city: ")
    noun_singular5 = input("Choose a singular noun: ")
    noun_singular6 = input("Choose a singular noun: ")

# // Displays the story based on the users input
    print(f"My cubicle is {adjective}. It's the {superiative} cubicle in the office.\
I have a {noun_singular} on my desk next to {adjective2} {noun_singular2}.\
In my drawer I also have {adjective3} {noun_singular3}.\
One time coworker tried to {verb} a {noun_singular4} on my desk.\
I said to him: 'Hey! How would you like it if I {verb2} your {noun_singular7}?'. I will do it if you don't leave.\
My one complaint about my cubicle is {adjective4}. I think everyone here at the office complaints about this.\
We also complaint that our cubicle is {adjective5}.\
If we had money in our budget, my boss could purchase some {noun_plural} to help alleviate this problem.\
Our boss doesn't understand. His office is the size of {city}.\
He has enough space to put a {noun_singular5} and {noun_singular6} there!")
    
    loop = loop + 1
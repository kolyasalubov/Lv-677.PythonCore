def weekexeption():
    try:
        days_dict ={'1':"Sunday" ,'2':"Monday",'3':"Tuesday", '4':"Wednesday", '5':"Thursday", '6':"Friday", '7':"Saturday"}
        user_input = input("Enter day number: ")
        print ("The day of the week is", days_dict[user_input])
    except KeyError:
        print("This not a number of the day of week")
weekexeption()

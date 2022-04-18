zen_of_P = """Beautiful is better than ugly.       
Explicit is better than implicit.    
Simple is better than complex.       
Complex is better than complicated.  
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.  
Errors should never pass silently.   
Unless explicitly silenced.
In the face of ambiguity, refuse the 
temptation to guess.
There should be one-- and preferably 
only one --obvious way to do it.     
Although that way may not be obvious 
at first unless you're Dutch.        
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

better_number = (zen_of_P.count("better"))
is_number = (zen_of_P.count("is"))
never_number = (zen_of_P.count("never"))

print ("Word BETTER used", better_number, "times")
print ("Word IS used", is_number, "times")
print ("Word NEVER used", never_number, "times")


upper_case = (zen_of_P.upper())
print(upper_case)


replacing_i = (zen_of_P.replace('i','&'))
print(replacing_i)





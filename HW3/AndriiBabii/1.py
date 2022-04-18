string = "Although never is often better than *right* now." #16 строчка ZenOfPython

string_upper = string.upper() #Стрічка в верхньому регістрі

string_replace = string.replace("i", "&") #Замінна 'i' на '&'


#Підрахунок входжень "is", "never", "better"
string_count_is = string.count("is") 
string_count_never = string.count("never")
string_count_better = string.count("better")

#Вивід
print("\n", string_upper,"\n", string_replace, "\n'Is': ", string_count_is, "\n'never': ", string_count_never, "\n'better': " , string_count_better)

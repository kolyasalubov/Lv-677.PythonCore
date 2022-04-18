def operations_on_numbers():                                         #Функція щодо операцій над числами
    while True:
        a = input('Variable a:\n')                                    #Вводимо число "а"        
        try:  
            number_a=float(a)                                        #Перевірка, що число "а" введено без помилки (іншого формату)                                        
        except ValueError:                                           #Перевірка на помилку невірного формату значення (a==str)
            print('Put the number!Try again...\n')
            continue
        else:
            while True:
                b = input('Variable b:\n')                            #Вводимо число "b" 
                try:                                                    
                    number_b=float(b)                                #Перевірка, що число "b" введено без помилки (іншого формату)                                                         
                    sum_of_numbers = number_a + number_b             #Операція додавання заданих чисел
                    difference_of_numbers = number_a - number_b      #Операція віднімання заданих чисел    
                    multiplication_of_numbers = number_a * number_b  #Операція множення заданих чисел
                    division_of_numbers =  number_a / number_b       #Операція ділення заданих чисел
                    exponentiation_of_number = number_a ** number_b  #Операція зведення до степеню
                except ValueError:                                   #Перевірка на помилку невірного формату значення (b==str)
                    print('Put the number!Try again...\n')
                    continue
                else:
                    print(f'a + b = {sum_of_numbers}')                   #Виводимо результат оперції додавання на консоль
                    print(f'a - b = {difference_of_numbers}')            #Виводимо результат оперції віднімання на консоль
                    print(f'a * b = {multiplication_of_numbers}')        #Виводимо результат оперції множення на консоль
                    print(f'a / b = {division_of_numbers}')              #Виводимо результат оперції діленняна консоль
                    print(f'a ** b = {exponentiation_of_number}')        #Виводимо результат зведення до степеню на консоль    
                    break
            break                                                      
operations_on_numbers()

def quastion_to_user():                                              #Функція щодо процесу діалогу з користувачем                          
    while True:                                                      #Перевірка щодо продовження або завершення виконання def operations_on_numbers()
        input_answer = input('Enter yes/no to continue\n')                  
        if input_answer=="yes" or input_answer=="Yes":
            operations_on_numbers()
            continue
        elif input_answer=="no" or input_answer=="No":
            break 
        else:
            print('Enter either yes/no\n')
quastion_to_user()

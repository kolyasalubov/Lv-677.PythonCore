def solution(number: int) -> int: 
    summa = 0   
    for element in range(3,number):
        if element % 3 == 0 or element % 5 == 0:
            summa += element
    return summa
  

def solution(number: int) -> int:
    return sum(element for element in range(3, number) if element % 3 == 0 or element % 5 == 0)
    

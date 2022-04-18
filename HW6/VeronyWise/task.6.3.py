def caunt_funk(count_symbols):
     '''
     Function that calculates the number 
     of characters included in a given string.
     '''
     result = {}
     for item in count_symbols:
          if item in result:
               continue
          else:
               result.update({str(item):count_symbols.count(item)})
     return result

count_symbols = input("Write symbols for calculating: ")
print(caunt_funk(count_symbols))
   

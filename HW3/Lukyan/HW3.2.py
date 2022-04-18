
a=input('Write four-digit number\n')
print("the product of number is ",int(a[0])*int(a[1])*int(a[2])*int(a[3]))
print("the number is reverse",a[-1]+a[-2]+a[-3]+a[-4])
a=list(a)
a.sort()
print('Sort number',"".join(a))

n = "2609"
n1 = list(map(int,str(n)))
list.sort(n1)
num1 = int(''.join(map(str,n1)))
list.sort(n1, reverse = True)
print(num1)  
num2 = int(''.join(map(str,n1)))
print(num2)
sub1 = num2 - num1    
print (sub1)

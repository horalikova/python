n = str(input("Type a four digit number: (please do not include with same numbers, like 2222 etc.)"))
n1 = list(map(int,str(n)))
list.sort(n1)
num1 = int(''.join(map(str,n1)))
list.sort(n1, reverse = True)
print(num1)
num2 = int(''.join(map(str,n1)))
print(num2)
sub1 = num2 - num1
print (sub1)

while sub1!=6147:
  sub=sub1
  n1 = list(map(int,str(sub)))
  list.sort(n1)
  num1 = int(''.join(map(str,n1)))
  list.sort(n1, reverse = True)
  print(num1)
  num2 = int(''.join(map(str,n1)))
  print(num2)
  sub1 = num2 - num1
  print (sub1)
  if sub1==6147:
     break

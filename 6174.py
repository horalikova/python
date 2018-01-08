def step(n):
  n1 = list(map(int,str(n)))
  list.sort(n1)
  num1 = int(''.join(map(str,n1)))
  list.sort(n1, reverse = True)
  print(num1)
  num2 = int(''.join(map(str,n1)))
  print(num2)
  sub1 = num2 - num1
  print (sub1)
  return sub1

n = str(input("Type a four digit number: (please do not include with same numbers, like 2222 etc.)"))
sub1 = step(n)

while sub1!=6174:
  sub1=step(sub1)
  


  #n1 = list(map(int,str(sub)))
  #list.sort(n1)
  #num1 = int(''.join(map(str,n1)))
  #list.sort(n1, reverse = True)
  #print(num1)
  #num2 = int(''.join(map(str,n1)))
  #print("num2:"+str(num2))
  #sub1 = num2 - num1
  #print ("sub1:" +str(sub1))
 

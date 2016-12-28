a = int(input("výška:"))
b = int(input("šířka:"))
c = int(input("délka:"))
myList=[a,b,c]
x=min(a,b,c)
print(x)
myList.remove(x)
print(myList)
z=min(myList)
print(z)



if (2*x+z)>100:
  print("nejde zabalit")
else:

  povrch= 2*(a*b+a*c+c*b)*1.2
  print("zabaleno s použitím %i cm2" %povrch)

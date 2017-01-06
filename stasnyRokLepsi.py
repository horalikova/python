year1 = input("from what year? (a four digit number please)")
year2 = input("to what year? (a four digit number please)")
digitis1= [int(d) for d in str(year1)]
print(digitis1)
digitis2=[int(d) for d in str(year2)]
print (digitis2)

sum1= sum(digitis1)
print (sum1)
sum2= sum(digitis2)
print (sum2)

digitis1Final= [int(d) for d in str(sum1)]
digitis2Final= [int(d) for d in str(sum2)]
sum1Final1=sum(digitis1Final)
print(sum1Final1)
sum2Final2=sum(digitis2Final)
print(sum2Final2)

if sum1Final1==1:
  print( "{} was/will be a lucky year".format(year1))

else:
  print ("{} was/will be unfourtunatly not a lucky year".format(year1))

if sum2Final2==1:
  print("{} was/will be was a lucky year".format(year2))
else:
  print ("{} was/will be unfourtunatly not a lucky year".format(year2))
  

year1 = int(input("from what year? (a four digit number please)"))
year2 = int(input("to what year? (a four digit number please)"))
for n in range(year1,year2 +1):
  print(n)
  digitis1= [int(d) for d in str(n)]
  sum1= sum(digitis1)
  print (sum1)
  while (sum1 > 9):
   sum1Digits= [int(d) for d in str(sum1)]
   sum1= sum(sum1Digits)
   print (sum1)

  if sum1==1:
    print( "{} will/was a lucky year".format(n))
  else:
    print ("{} will/was unfourtunatly not a lucky year".format(n))

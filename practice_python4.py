number=int(input("number: "))
for n in range(1,number +1):
  remainder= number% n
  if remainder==0:
    print(n)

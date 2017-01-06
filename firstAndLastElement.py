list1Str = input("please write the elements of the second list:(use commas)")
numbers1 = list1Str.split(",")
print(numbers1[0])
c=len(numbers1)
print(numbers1[c-1])
myList=[]
myList.append(numbers1[0])
myList.append(numbers1[c-1])
print(myList)

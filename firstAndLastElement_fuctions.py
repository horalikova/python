def elementAtIndex(list, index):
  return list[index]

list1Str = input("please write the elements of the second list:(use commas)")
numbers1 = list1Str.split(",")

myList=[]
#myList.append(numbers1[0])
myList.append(elementAtIndex(numbers1,0))

#myList.append(numbers1[c-1])
myList.append(elementAtIndex(numbers1,len(numbers1)-1))
print(myList)

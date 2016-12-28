list1Str = input("please write the elements of the first list:")
list2Str = input("please write the elements of the second list:")

numbers1 = list1Str.split(",")
numbers2 = list2Str.split(",")

print(numbers1)
print(numbers2)

for n in numbers1:
  if n in numbers2:
    print (n)

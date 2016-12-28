word = input("please write the elements of the first list:")
print(word[0])

for i in range(0,(int(len(word)/2)-1)):
  print("comparing {} with {}".format(word[i],word[len(word)-1-i]))
  if word[i]==word[len(word)-1-i]:
    print("same")

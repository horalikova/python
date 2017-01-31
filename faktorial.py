number= int(input("write a number:"))
result= 1
open_file = open('file_to_save.txt', 'a')
for i in range (1,number +1):
  result= result*i

open_file.write("Factorial of {} is  {}\n".format(number,result))
open_file.close()

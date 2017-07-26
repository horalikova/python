import codecs

path = 'C:\Users\evca\Desktop\DS\sloh.txt'
sloh_file = codecs.open(path,'r',"utf-8")
content=sloh_file.read()
print(content)

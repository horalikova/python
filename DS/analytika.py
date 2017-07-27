import codecs
import nltk 
from collections import Counter

from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

#path = 'C:\Users\evca\Desktop\DS\sloh.txt'
path = "security.txt"
sloh_file = codecs.open(path,'r',"utf-8")
content=sloh_file.read()
print(content)

words=content.split()
results=[]
for word in words:
     if word not in stop:
        results.append(word)
print(results)        


cntr = Counter(results)
print(cntr.most_common(10))



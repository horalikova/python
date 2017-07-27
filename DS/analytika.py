import codecs
import nltk 
from collections import Counter

from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

path="rocnikovka.txt"
#path = 'sloh.txt'
#path = 'algebra.txt'
#path = "security.txt"
#sloh_file = codecs.open(path,'r',"utf-8")
sloh_file = open(path,'r')
content=sloh_file.read().decode('utf-8','ignore').encode("utf-8")
print(content)

words=content.split()
results=[]
for word in words:
     if word not in stop:
        results.append(word.lower())
#print(results)        


cntr = Counter(results)
print(cntr.most_common(10))



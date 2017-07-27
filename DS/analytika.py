from nltk.corpus import stopwords
from collections import Counter
#path="sloh.txt"
path="rocnikovka.txt"
file=open(path, "r")
obsah=file.read().decode("utf-8", "ignore").encode("utf-8")
#print(obsah)

words=obsah.split()
#print(words)

#stop=set(stopwords.words("english"))
file2=open("czechStopwords.txt", "r")
obsah2=file2.read().decode("utf-8", "ignore").encode("utf-8")
stop=set(obsah2.split())
#print(stop)

clean=[]
for word in words:
  if word.lower() not in stop:
     clean.append(word.lower())
print(clean)     

cntr = Counter(clean)
print(cntr.most_common(10))

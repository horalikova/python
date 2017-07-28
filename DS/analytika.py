from nltk.corpus import stopwords
from collections import Counter
import sys
import pprint


'Argument List:', str(sys.argv)
path=str(sys.argv[1])
print(sys.argv[1])

#path="sloh.txt"
#path="rocnikovka.txt"
file=open(path, "r")
obsah=file.read().decode("utf-8", "ignore").encode("utf-8")
#print(obsah)

words=obsah.split()

if ("the" in words) and ("and" in words):
  language="english"
else:
  language="czech"

if  language=="english":
  stop=set(stopwords.words("english"))
else:
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
mostCommon=cntr.most_common(10)

#for most in mostCommon:
#	println (most)

pprint.pprint(mostCommon)
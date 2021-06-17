a = int(input())
b = int(input())
i = a 
r = 0
while i < b:
    r = r + i
    i = i + 2
print(r) 
#4875 9268

seq='que tranza carnal como andas que pasa por tu casa no te han hecho tranza'
seqsep= seq.split(' ')
dict={}
for word in seqsep:
    dict[word]=seqsep.count(word)
for key, value in dict.items():
    print(key, value)
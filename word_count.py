fname = input('Enter file name : ')
fhand = open(fname)

count = dict()
bigWord = []
bigCount = 0

for line in fhand:
    words = line.split()
    for word in words:
        #increment if word already exists in dict or create new pair
         count[word] = count.get(word, 0) + 1

#number of occurences of the most common word/words
for value in count.values():
    if value > bigCount:
        bigCount = value

#list of most common words
for key in count.keys():
    if count[key] == bigCount:
        bigWord.append(key)

#print(count)
print(bigWord, bigCount)
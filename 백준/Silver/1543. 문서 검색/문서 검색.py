document = input().rstrip()
word = input().rstrip()

result= 0
index = 0

while True:
    if index + len(word) > len(document):
        break
    for i in range(len(word)):
        if document[index+i] != word[i]:
            index+=1
            break
    else:
        result+=1
        index+=len(word)

print(result)
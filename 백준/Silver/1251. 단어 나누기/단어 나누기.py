word = input().rstrip()

result = []

for i in range(1,len(word)):
    for j in range(i+1,len(word)):
        tmp1 = word[:i][::-1]
        tmp2 = word[i:j][::-1]
        tmp3 = word[j:][::-1]
        result.append(tmp1+tmp2+tmp3)

result.sort()
print(result[0])

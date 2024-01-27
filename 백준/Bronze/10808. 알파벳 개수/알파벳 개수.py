word = input()
lst = [0 for _ in range(26)]

for i in word:
    lst[ord(i)-97] +=1
for i in lst:
    print(i, end=' ')
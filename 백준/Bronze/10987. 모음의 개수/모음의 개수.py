word = input()
lst = ['a','e','i','o','u']
cnt = 0
for i in word:
    if i in lst:
        cnt+=1
print(cnt)
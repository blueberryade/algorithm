x = input().rstrip()
cnt = 0

while len(x)>1:
    cnt+=1
    total = 0
    for i in x:
        total+=int(i)
    x = str(total)

print(cnt)

if int(x)%3 == 0:
    print("YES")
else:
    print("NO")
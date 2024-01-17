n = int(input())
for _ in range(n):
    s = input()
    total = 0
    num = 0
    for ox in s:
        if ox == 'O':
            num+=1 
            total+=num
        else:
            num = 0
    print(total)
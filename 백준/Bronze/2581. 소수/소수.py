m = int(input())
n = int(input())

lst = []
for num in range(m, n+1): 
    cnt = 0 
    if num > 1: 
        for i in range(2, num): 
            if num % i == 0: 
                cnt += 1 
                break
        if cnt == 0: 
            lst.append(num)

if len(lst) > 0:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)
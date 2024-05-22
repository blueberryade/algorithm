n = int(input())
m = int(input())
s = input()

cur,count,result = 0,0,0

while cur < (m-1):
    if s[cur:cur+3] == 'IOI':
        count+=1
        cur+=2
        if count == n:
            result+=1
            count-=1
    else:
        count = 0
        cur+=1
    
print(result)
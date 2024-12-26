import sys
input = sys.stdin.readline

N,H = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

start = 1
end = sys.maxsize*N
result = 0

while start<=end:
    mid = (start+end) // 2
    curHP,maxHP,atk = mid,mid,H
    
    for t,a,h in data:
        if t == 1:
            cnt = h//atk
            if h%atk !=0:
                cnt +=1 
            curHP -= a*(cnt-1)

            if curHP<=0:
                break
        else:
            atk+=a
            curHP = min(curHP+h,maxHP)


    if curHP <= 0:
        start = mid+1

    else:
        end = mid-1
        result = mid      

print(result)
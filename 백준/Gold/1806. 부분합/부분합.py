n,s = map(int,input().split())
data = list(map(int,input().split()))

left,right = 0,0
total = 0
result = 1e9

while True:
    if total >=s:
        result = min(result,right-left)
        total -= data[left]
        left+=1
    elif right == n:
        break
    else:
        total+= data[right]
        right+=1
        
if result == 1e9:
    print(0)
else:
    print(result)
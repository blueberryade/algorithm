t = int(input())
for _ in range(t):
    g,c,e = map(int,input().split())
    candy = e - c 
    result = 0
    if g == 1:
        result = 1*candy
    elif g == 2:
        result = 3*candy
    else:
        result = 5*candy
        
    if candy <=0:
        print(0)
    else:
        print(result)
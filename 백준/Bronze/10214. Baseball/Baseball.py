t = int(input())

for _ in range(t):
    yonsei = korea = 0
    for _ in  range(9):
        y,k = map(int,input().split())
        yonsei+=y
        korea+=k
    
    if yonsei == korea:
        print('Draw')
    elif yonsei > korea:
        print('Yonsei')
    else:
        print('Korea')
  
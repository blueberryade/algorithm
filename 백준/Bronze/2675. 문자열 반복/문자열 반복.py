t = int(input())
result = ''
for _ in range(t):
    r,string = input().split()
    for s in string:
        print(s*int(r),end ='')
    print()
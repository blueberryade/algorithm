t = int(input())
for _ in range(t):
    lst = list(map(int,input().split()))
    result = [i for i in lst if i%2==0]
    print(sum(result),min(result))
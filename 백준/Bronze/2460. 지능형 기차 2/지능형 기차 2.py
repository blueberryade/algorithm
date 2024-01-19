num = 0
max_num = 0
for _ in range(10):
    a,b = map(int,input().split())
    num+= b-a
    max_num = max(num, max_num)
    
print(max_num)

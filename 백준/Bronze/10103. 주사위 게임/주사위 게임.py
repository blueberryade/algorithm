n = int(input())
num1 = num2 = 100

for _ in range(n):
    a,b = map(int,input().split())
    if a == b:
        continue
    elif a > b:
        num2-=a
    else:
        num1-=b
print(num1)
print(num2)

n,b = map(int,input().split())
num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ''
while n !=0:
    result+=str(num[n%b])
    n//=b
print(result[::-1])
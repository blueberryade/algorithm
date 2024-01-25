def fibo(n):
    if n <=1:
        return n
    return fibo(n-2)+fibo(n-1)

num = int(input())
print(fibo(num))
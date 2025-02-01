import math

while True:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        print(0)
        continue
    result = n
    for p in range(2,int(math.sqrt(n))+1): 
        if n % p == 0: 
            result -=result/p 
            while n%p == 0: 
                n /= p
            
    if n > 1: 
        result -= result / n

    print(int(result))

    
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

sum = 0

A.sort()
B.sort(reverse=True)

for i in range(len(A)):
    sum+= A[i]*B[i]

print(sum)
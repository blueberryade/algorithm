N,K = map(int,input().split())
data = list(input())

result = 0

for i in range(N):
    if data[i] == 'P':
        for j in range(max(i-K,0),min(i+K+1,N)):
            if data[j] == 'H':
                result+=1
                data[j] = 0
                break
print(result)
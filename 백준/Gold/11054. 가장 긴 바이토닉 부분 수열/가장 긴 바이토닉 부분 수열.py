n = int(input())
data = list(map(int,input().split()))
reverse_data = data[::-1]

increase = [1]*n
decrease = [1]*n

for i in range(n):
    for j in range(i):
        if data[i] >data[j]:
            increase[i] = max(increase[i],increase[j]+1)

        if reverse_data[i] > reverse_data[j]:
            decrease[i] = max(decrease[i],decrease[j]+1)

max_length = 0
for i in range(n):
    max_length = max(max_length,increase[i]+decrease[n-i-1]-1)

print(max_length)

n = input()
result = 10
for i in range(1,len(n)):
    if n[i] == n[i-1]:
        result+=5
    else:
        result+=10
print(result)
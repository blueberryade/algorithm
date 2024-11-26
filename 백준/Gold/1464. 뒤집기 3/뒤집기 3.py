import sys
input = sys.stdin.readline

S = list(input().rstrip())
lst = S[0]

for i in range(1,len(S)):
    if lst[i-1] < S[i]:
        lst = S[i]+lst
    else:
        lst = lst+S[i]
        
print(lst[::-1])
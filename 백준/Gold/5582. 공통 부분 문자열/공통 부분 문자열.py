import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
answer = 0
prev_dp = [0]*(len(str2)+1)
cur_dp = [0]*(len(str2)+1)

for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        if str1[i-1] == str2[j-1]:
            cur_dp[j] = prev_dp[j-1]+1
            answer = max(answer,cur_dp[j])
        else:
            cur_dp[j] = 0
    prev_dp,cur_dp = cur_dp,[0]*(len(str2)+1)

print(answer)
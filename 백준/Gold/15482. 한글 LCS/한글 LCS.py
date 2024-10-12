import sys
input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()

dp = [0]*1000

for i in range(len(word1)):
    max_num = 0
    for j in range(len(word2)):
        if max_num < dp[j]:
            max_num = dp[j]
        elif word1[i]==word2[j]:
            dp[j] = max_num+1

print(max(dp))

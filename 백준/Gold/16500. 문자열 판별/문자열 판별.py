import sys
input = sys.stdin.readline

S = input().rstrip()
N = int(input())
words = []
for _ in range(N):
    word = input().rstrip()
    words.append(word)

dp = [0]*(len(S)+1)
dp[0] = 1

for i in range(len(S)):
    if not dp[i]:
        continue

    for word in words:
        if S[i:i+len(word)] == word:
            dp[i+len(word)] = 1

print(dp[len(S)])

import sys
input = sys.stdin.readline

s = list(input().rstrip())
q = int(input().rstrip())

cnt = [[0]*26]

for i,ch in enumerate(s):
    cnt.append(cnt[len(cnt)-1][:])
    cnt[i+1][ord(ch)-97] +=1


for _ in range(q):
    alpha,l,r = input().split()
    result = cnt[int(r)+1][ord(alpha)-97]-cnt[int(l)][ord(alpha)-97]
    print(result)

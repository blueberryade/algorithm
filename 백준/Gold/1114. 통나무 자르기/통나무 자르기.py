L,K,C = map(int,input().split())
data = [0]+sorted(list(map(int,input().split())))+[L]

pieces = [data[idx+1] - data[idx] for idx in range(K+1)]
longest = max(pieces)

def solve(mid):
    if longest > mid:
        return 10001,0

    total = 0
    count = 0

    for piece in pieces[::-1]:
        total+=piece
        if total > mid:
            total= piece
            count+=1
    return count, total if count == C else pieces[0]

start = 0
end = L

ans_longest = 0
ans_front = 0

while start <= end:
    mid = (start+end) //2

    count,front = solve(mid)
    if count <= C:
        ans_longest = mid
        ans_front = front
        end = mid-1

    else:
        start = mid+1

print(ans_longest,ans_front)

import heapq

def solution(scoville, K):
    answer = 0
    q = []
    for s in scoville:
        heapq.heappush(q,s)

    while q[0] < K:
        tmp1 = heapq.heappop(q) 
        tmp2 = heapq.heappop(q)
        heapq.heappush(q,tmp1+tmp2*2)
        answer+=1
        
        if len(q) == 1 and q[0] < K:
            return -1
    return answer
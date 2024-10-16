import heapq

def solution(n, works):
    q = []
    for i in works:
        heapq.heappush(q,-i)
        
    for _ in range(n):
        if q[0] == 0:
            break
        num = heapq.heappop(q)
        heapq.heappush(q,num+1)
    answer = sum([i**2 for i in q])
    
    return answer
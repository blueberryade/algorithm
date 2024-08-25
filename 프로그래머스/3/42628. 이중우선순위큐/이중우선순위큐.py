import heapq

def solution(operations):
    answer = []
    q = []
    for i in operations:
        o,num = i.split()
        num = int(num)
        if o == 'I':
            heapq.heappush(q,int(num))
        else:
            if q:
                if num == -1:
                    heapq.heappop(q)
                else:
                    q.sort()
                    q.pop()
    q.sort()                    
    
    if q:
        answer = [q[-1],q[0]]
    else:
        answer = [0,0]
                
    
    return answer
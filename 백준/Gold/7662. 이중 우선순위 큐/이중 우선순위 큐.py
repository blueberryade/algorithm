import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    visited = [False] * 1000001

    for i in range(k):
        o,num = input().split()
        if o == 'I':
            heapq.heappush(min_heap,(int(num),i))
            heapq.heappush(max_heap,(-int(num),i))
            visited[i] = True
        else:
            if num == '-1':
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            if num == '1':
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)  
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
        
    if len(min_heap) == 0 or len(max_heap) == 0:
        print('EMPTY')
    else:
        print(-max_heap[0][0],min_heap[0][0])
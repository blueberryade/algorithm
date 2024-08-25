import sys
import heapq
input = sys.stdin.readline

def getMedian(data,M):
    left_heap = []  
    right_heap = []
    result = []

    for i in range(M):
        num = data[i]
        
        if len(left_heap) == len(right_heap):
            heapq.heappush(left_heap,-num)
        else:
            heapq.heappush(right_heap,num)

        if right_heap and -left_heap[0] > right_heap[0]:
            max_left = -heapq.heappop(left_heap)
            min_right = heapq.heappop(right_heap)
            heapq.heappush(left_heap, -min_right)
            heapq.heappush(right_heap, max_left)

        if i%2 == 0:
            result.append(-left_heap[0])

    return result

T = int(input())
for _ in range(T):
    M = int(input())
    data = []
    for _ in range(M//10+1):
        data.extend(list(map(int,input().split())))

    cnt = M//2+1
    print(cnt)
    result = getMedian(data,M)
    for i in range(len(result)):
        if i> 0 and i%10 == 0:
            print()
        print(result[i],end=' ')
    print()
    

    

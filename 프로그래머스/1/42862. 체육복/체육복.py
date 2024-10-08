def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = 0
    
    for i in range(1,n+1):
        if i not in lost:
            answer+=1
        else:
            if i in reserve:
                answer+=1
                reserve.remove(i)
                lost.remove(i)
    
    for i in lost:
        if i-1 in reserve:
            answer+=1
            reserve.remove(i-1)
            
        elif i+1 in reserve:
            answer+=1
            reserve.remove(i+1)
            
    
    return answer
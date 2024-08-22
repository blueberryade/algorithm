def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    
    left = 0
    right = distance
    
    while left <= right:
        mid = (left+right) // 2
        cur = 0
        remove_cnt = 0
        
        for rock in rocks:
            if rock-cur < mid:
                remove_cnt += 1
            else:
                cur = rock
        
        if distance - cur < mid:
            remove_cnt +=1
        
        if remove_cnt > n:
            right = mid - 1
        
        else:
            answer = mid
            left = mid+1
        
    
    return answer
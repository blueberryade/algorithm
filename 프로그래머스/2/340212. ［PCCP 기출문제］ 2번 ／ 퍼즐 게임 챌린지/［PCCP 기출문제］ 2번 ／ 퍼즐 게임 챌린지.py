def solution(diffs, times, limit):
    answer = 0
    def get_time(mid):
        total = 0
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                total += times[i]
            else:
                total+=(diffs[i]-mid)*(times[i]+times[i-1])+times[i]
                
        return total   
    
    left = 1
    right = max(diffs)

    while left <= right:
        mid = (left+right) // 2
    
        if get_time(mid) <= limit:
            answer = mid
            right = mid-1
        else:
            left = mid + 1      
    
    return answer
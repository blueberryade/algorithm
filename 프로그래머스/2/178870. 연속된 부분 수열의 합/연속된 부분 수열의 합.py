def solution(sequence, k):
    answer = []
    cur_sum = 0
    l,r = 0,-1
    
    while True:
        if cur_sum < k:
            r+=1
            if r>=len(sequence):
                break
            cur_sum+=sequence[r]
        else:
            cur_sum-=sequence[l]
            if l>=len(sequence):
                break
            l+=1
        if cur_sum == k:
            answer.append([l,r])
    answer.sort(key=lambda x:x[1]-x[0])
    return answer[0]

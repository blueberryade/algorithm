def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        r = []
        for a in arr[s:e+1]:
            if a > k:
                r.append(a)
        answer.append(-1) if len(r)==0 else answer.append(min(r))
    return answer
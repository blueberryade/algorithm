def solution(arr, flag):
    answer = []
    for i,f in enumerate(flag):
        if f:
            answer.extend([arr[i]]*arr[i]*2)
        else:
            for j in range(arr[i]):
                answer.pop()
    return answer
def solution(array, commands):
    answer = []
    for c in commands:
        i,j,k = c
        arr = sorted(array[i-1:j])
        answer.append(arr[k-1])    
    return answer
def solution(array, n):
    answer = []
    array.sort()
    for i in array:
        answer.append(abs(n-i))
    idx =answer.index(min(answer))
    
    return array[idx]
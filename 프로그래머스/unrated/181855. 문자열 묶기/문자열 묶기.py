def solution(strArr):
    answer = {}
    for i in strArr:
        answer[len(i)] = answer.get(len(i),0)+1
    return max(answer.values())
def solution(a, d, included):
    answer = 0
    for i,e in enumerate(included):
        if e:
            answer += a+d*i
    return answer
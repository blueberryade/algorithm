def solution(my_string, n):
    answer = ''
    for c in list(my_string):
        answer += c*n
    return answer
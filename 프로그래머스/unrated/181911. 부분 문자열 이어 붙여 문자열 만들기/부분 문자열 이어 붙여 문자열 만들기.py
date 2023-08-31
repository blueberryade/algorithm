def solution(my_strings, parts):
    answer = ''
    for i,a in enumerate(my_strings):
        s,e = parts[i]
        answer+= a[s:e+1]
    return answer
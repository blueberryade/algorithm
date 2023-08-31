def solution(my_string, s, e):
    a = reversed(list(my_string[s:e+1]))
    return my_string[0:s]+''.join(a) +my_string[e+1:]
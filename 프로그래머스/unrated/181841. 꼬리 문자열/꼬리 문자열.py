def solution(str_list, ex):
    return ''.join([e for e in str_list if ex not in e])
def solution(num_list):
    e = 1
    for i in num_list:
        e*=i
    return int(e < sum(num_list)**2)
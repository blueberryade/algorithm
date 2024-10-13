def solution(data, ext, val_ext, sort_by):
    dic = {"code":0,"date":1,"maximum":2,"remain":3}
    answer = list(filter(lambda x: x[dic[ext]] < val_ext,data))
    answer.sort(key=lambda x: x[dic[sort_by]])     
    return answer
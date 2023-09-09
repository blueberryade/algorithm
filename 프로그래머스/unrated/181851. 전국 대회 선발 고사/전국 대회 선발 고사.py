def solution(rank, attendance):
    lst = sorted([(e,i) for i,e in enumerate(rank) if attendance[i]]) 
    return lst[0][1]*10000+ lst[1][1]*100+lst[2][1]
    
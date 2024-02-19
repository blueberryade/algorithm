def solution(clothes):
    dic = {}
    for i in clothes:
        a,b = i
        if b in dic:
            dic[b].append(a)
        else:
            dic[b] = [a]
    cnt = 1
    for k in dic:
        cnt*= len(dic[k])+1
    return cnt-1
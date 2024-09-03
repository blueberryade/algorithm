def solution(s):
    cnt = 0
    for i in s:
        if cnt < 0:
            break
        cnt+= 1 if i== '(' else -1


    return True if cnt == 0 else False
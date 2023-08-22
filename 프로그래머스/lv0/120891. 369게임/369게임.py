def solution(order):
    answer = 0
    for i in str(order):
        if int(i)!=0 and int(i)%3==0:
            answer+=1
    return answer
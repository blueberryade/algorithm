def solution(answers):
    answer = [0,0,0]
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    for idx,e in enumerate(answers):
        if e == one[idx%len(one)]:
            answer[0]+=1
        if e == two[idx%len(two)]:
            answer[1]+=1
        if e == three[idx%len(three)]:
            answer[2]+=1
            
    max_num = max(answer)
    result = []
    for idx,e in enumerate(answer):
        if e == max_num:
            result.append(idx+1)
    
    return result